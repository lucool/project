import pymysql

# 获取数据库连接
def get_conn():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='mydb1',
        charset='utf8'
    )
    return conn

# 查询所有水果
def get_fruits():
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select id,name,price from fruits"
    try:
        cursor.execute(sql)
        fruits = cursor.fetchall()
        conn.commit()
        return fruits
    except Exception as e:
        print("查询水果出错，错误原因：",e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# 查询所有国家
def get_countries():
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select id,name,address from countries"
    try:
        cursor.execute(sql)
        countries = cursor.fetchall()
        conn.commit()
        return countries
    except Exception as e:
        print("查询国家出错，错误原因：", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()