# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db,mongo_port):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.port = mongo_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_port=crawler.settings.get('MONGO_PORT')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_uri,port=self.port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert_one(dict(item))
        print("正在存储。。。。", item["url"])
        return item


class mysqlPipeline(object):

    conn = None
    cursor = None

    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='root',db='amazon_text',charset='utf8')

    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into amazon_text values("%s","%s","%s","%s")'%(item["url"],item["asin"],item["rank_big"],item["rank_small"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()