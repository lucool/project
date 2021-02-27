import pymysql

from HomeworkApp.po import Fruit

# 获取数据库连接
def get_conn():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='mydb',
        charset='utf8'
    )
    return conn

# 查询所有水果信息
def select_fruits():
    fruits = []
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select id,name,price from fruits"
    try:
        cursor.execute(sql)
        items = cursor.fetchall()
        conn.commit()
        for item in items:
            fruit = Fruit(item[0],item[1],item[2])   # 将数据库中查出的数据封装到Fruit对象中
            fruits.append(fruit)
        return fruits
    except Exception as e:
        print("查询所有水果异常，失败原因：",e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# 根据ID查询单个水果
def select_single_fruit(id):
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select id,name,price from fruits where id='{}'".format(id)
    try:
        cursor.execute(sql)
        item = cursor.fetchone()
        conn.commit()
        fruit = Fruit(item[0], item[1], item[2])  # 将数据库中查出的数据封装到Fruit对象中
        return fruit
    except Exception as e:
        print("查询单个水果异常，失败原因：", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()