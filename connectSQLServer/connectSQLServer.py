print('---python操作SQLServer数据库记录---')
'''
一、使用模块介绍及安装
    1、Python操作sqlserver所使用的模块是pymssql。
    2、pymssql安装，直接使用pip install pymssql进行安装。
二、Python操作sqlserver介绍
    1、数据库连接类及参数介绍
        pymssql.connect()：sqlserver连接的连接类。
            server/host（str）：需要连接的数据库主机和实例。如：ip、ip\SQLEXPRESS、.\SQLEXPRESS等。
            user（str）：连接数据库的用户名。如：sa、test等。
            password（str）：连接数据库对应用户名的密码。
            database（str）：需要操作的数据库。
            timeout（int）：在几秒钟内查询超时，默认值为0无限等待。
            login_timeout（int）：连接超时和登录超时时间，默认值为60。
            charset（str）：连接数据库使用的字符集。
            as_dict（bool）：是否作为字典返回，默认为元组。
    2、数据库连接对象的方法
        connection.close()：关闭数据库连接。
        connection.cursor()：返回一个游标对象，该对象可以用于查询并从数据库中获取结果。
        connection.commit()：提交当前事务。你必须调用这个方法来确保你的数据执行。
        connection.autocommit()：那里的状况是一个布尔值。该方法将决定自动提交模式打开或关闭。
    3、Cusor 对象方法
        Cursor.close()：关闭游标对象，该游标对象无法再使用。
        Cursor.execute()：操作字符串和参数。
        Cursor.fetchall()：returning a list of tuples, or a list of dictionaries
        Cursor.fetchone()： returning a tuple, or a dictionary
        Cursor.fetchmany(size=None)： returning a list of tuples, or a list of dictionaries
官方文档地址:http://www.pymssql.org/en/stable/ref/pymssql.html#connection-class

'''
import pymssql
conn = pymssql.connect(server='172.17.230.210',database='hd_3355',user='sa',password='123456')

print('查询数据库测试...')
cursor = conn.cursor()
cursor.execute("select * from warehouse;")

rows = cursor.fetchall()
for row in rows:
    print(row)


