'''
通过数据库还原数据
'''
from page_object1910.func.conn_mysql.get_db_conn import Get_Db_Conn



def Delete_Record_Form_Db(addto):
    conn = Get_Db_Conn()
    curs  = conn.cursor() # 通过游标获取
    sql = "delete from hd_goods where name ='" + addto + "'"
    try:
        curs.execute(sql) # 尝试执行语句
        conn.commit()
    except Exception as e:
        conn.rollback() # rollback() 回滚  执行一半不成功进行回滚
        print('删除' + addto + '操作失败')
    finally:
        print('删除' + addto + '操作成功')
        conn.close()


