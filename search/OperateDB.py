# -*- coding: utf-8 -*-
#encoding=utf-8
__author__ = 'shishuangwei'

import MySQLdb

#import sae.const

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = '1234'
DBNAME = 'library'
CHARSET = 'utf8'

def initialize():

    """
    初始化数据库
    """
    try:
        conn = MySQLdb.connect(host = HOST,user = USER, passwd = PASSWORD, port = PORT, charset = CHARSET )
        cur = conn.cursor()
        cur.execute('create database if not exists '+DBNAME)
        conn.select_db(DBNAME)
        cur.execute('create table Author (AuthorID int not null ,\
                                         Name varchar(100),\
                                         Age int,\
                                         country varchar(100),\
                                         primary key (AuthorID))DEFAULT CHARSET=utf8;')
        cur.execute('create table Book (ISBN varchar(45) not null,\
                                        Title varchar(45),\
                                        AuthorID int,\
                                        Publisher varchar(45),\
                                        PublishDate varchar(45),\
                                        Price decimal(10,2),\
                                        primary key (ISBN),\
                                        foreign key(AuthorID) references Author(AuthorID)) DEFAULT CHARSET=utf8;')
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def drop_database():
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute('drop database '+DBNAME)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def read_author():
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute('select * from Author')
        info=cur.fetchall()
        result=[]
        for row in info:
            authorID = row[0]
            name = row[1]
            age = row[2]
            country = row[3]
            newnode = authorID,name,age,country
            result.append(newnode)
        cur.close()
        conn.close()
        return result
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def read_book():
     try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute('select * from Book')
        info=cur.fetchall()
        result=[]
        for row in info:
            ISBN = row[0]
            Title = row[1]
            AuthorID = row[2]
            Publisher = row[3]
            PublishDate = row[4]
            Price = row[5]
            newnode = ISBN,Title,AuthorID,PublishDate,Publisher,Price
            result.append(newnode)
        cur.close()
        conn.close()
        return result
     except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def write_author(authorinfo):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("insert into Author values(%s,%s,%s,%s)",authorinfo)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def write_book(bookinfo):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("insert into Book values(%s,%s,%s,%s,%s,%s)",bookinfo)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False

def search_authorid_by_name(name):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("select AuthorID from Author where name = "+name)
        info=cur.fetchone()
        cur.close()
        conn.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def search_author_by_id(id):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("select * from Author where AuthorID = "+str(id))
        info=cur.fetchone()
        cur.close()
        conn.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def search_book_by_authorid(id):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("select * from Book where AuthorID ="+str(id))
        info=cur.fetchall()
        cur.close()
        conn.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def update_book(choose,isbn,value):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        if choose == 1:
            cur.execute("update Book set Title= %s where ISBN = %s",(value,isbn))
        elif choose == 2:
            cur.execute("update Book set AuthorID= %s where ISBN = %s",(value,isbn))
        elif choose == 3:
            cur.execute("update Book set Publisher= %s where ISBN = %s",(value,isbn))
        elif choose == 4:
            cur.execute("update Book set PublishDate= %s where ISBN = %s",(value,isbn))
        elif choose == 5:
            cur.execute("update Book set Price= %s where ISBN = %s",(value,isbn))
        else:
            return False
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def delete_book(isbn):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("delete from Book where ISBN = "+ str(isbn))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def delete_author(id):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("delete from Author where AuthorID = "+ str(id))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def delete_book(isbn):
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("delete from Book where isbn = "+ isbn)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
def insertdata():
    authorinfo = [(1L, u'\u6751\u4e0a\u6625\u6811', 66L, u'\u65e5\u672c'), (2L, u'J.K.\u7f57\u7433', 50L, u'\u82f1\u56fd'), (3L, u'\u5357\u6d3e\u4e09\u53d4', 33L, u'\u4e2d\u679c'), (4L, u'\u8001\u820d', 67L, u'\u4e2d\u56fd'), (5L, u'\u83ab\u8a00', 60L, u'\u4e2d\u56fd'), (6L, u'\u9c81\u8fc5', 55L, u'\u4e2d\u56fd'), (7L, u'\u5a01\u5ec9.\u838e\u58eb\u6bd4\u4e9a', 52L, u'\u82f1\u56fd'), (8L, u'\u5723\u57c3\u514b\u82cf\u4f69\u91cc', 44L, u'\u6cd5\u56fd'), (9L, u'\u52a0\u897f\u4e9a\u9a6c\u5c14\u514b\u65af', 87L, u'\u54e5\u4f26\u6bd4\u4e9a')]
    bookinfo=[(u'0439784549', u'Harry Potter and the Half-blood Prince', 2L, u'2005-7', u'n', '122.60'), (u'9787532742929', u'\u632a\u5a01\u7684\u68ee\u6797', 1L, u'2007-7', u'n', '18.50'), (u'9787532742936', u'\u4e14\u542c\u98ce\u541f', 1L, u'2013-7', u'm', '10.90'), (u'9787532768776', u'\u6ca1\u6709\u5973\u4eba\u7684\u7537\u4eba\u4eec', 1L, u'2015-3', u't', '27.60'), (u'9787544264099', u'1Q84', 1L, u'2011-1', u'', '72.50')]
    for row in authorinfo:
        write_author(row)
    for row in bookinfo:
        write_book(row)
def getauthormaxnum():
    try:
        conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,port=PORT,db=DBNAME,charset=CHARSET)
        cur=conn.cursor()
        cur.execute("SELECT MAX(AuthorID) AS LargestOrderPrice FROM Author ")
        info=cur.fetchone()
        cur.close()
        conn.close()
        return info
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return False
initialize()