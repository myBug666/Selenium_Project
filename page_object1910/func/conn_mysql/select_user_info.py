'''
查询用户信息
'''

from page_object1910.func.conn_mysql.get_db_conn import Get_Db_Conn



# 通过username去查询
def Select_User_Info(addto):
    conn = Get_Db_Conn()

    # 通过数据库连接，获取数据库cursor()游标，方便通过游标执行SQL语句
    curs = conn.cursor()
    sql = "select * from hd_goods where name ='" + addto + "'"

    # select * from hd_user where username（数据库） = 'username(用户输入)'
    # select * from hd_user where username = ''or 1 = 1 '' sql注入

    try:
        curs.execute(sql)   # 尝试去连接数据库
        # fetchone() 函数返回值是单个元组，也就是一行记录，如果没有结果，返回null
        result = curs.fetchone()
        return result
    # 不成功返回E
    except Exception as E:
        raise E
    finally:
        conn.close()  # 关闭数据库连接诶

