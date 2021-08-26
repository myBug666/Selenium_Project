'''
获取数据库连接
'''
import pymysql

def Get_Db_Conn():
    conn = pymysql.connect(
        host='127.0.0.1',user='root',password='root',database='pirate',port=3306)
    return conn



