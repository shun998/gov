# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql


class GovPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='fww',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8')  # 编码方式
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql_str="""INSERT INTO gov (`type`,`located`,`body`,`time`,`address`,`process`,`material`,`CONDITION`,`method`)
	VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        self.cursor.execute(sql_str,
            (item['type'],  # item里面定义的字段和表字段对应
             item['located'],
             item['body'],
             item['time'],
             item['address'],
             item['process'],
             item['material'],
             item['condition'],
             item['method']))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回
