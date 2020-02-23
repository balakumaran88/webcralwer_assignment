# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class BookmyshowPipeline(object):
#     def process_item(self, item, spider):
#         return item
import sqlite3;

class BookmyshowPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn=sqlite3.connect("bookmyshows.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS shows_tb""")
        self.curr.execute("""create table shows_tb(title text, language text, genre text, url text) """)


    def process_item(self, item, spider):
        self.store_item(item)
        return item
    
    def store_item(self, item):
        self.curr.execute("""insert into shows_tb values (?,?,?,?)""", (
            item['title'],
            item['language'],
            item['genre'],
            item['url']
        ))
        self.conn.commit()
