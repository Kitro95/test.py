import pymysql
from Config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

except Exception as ex:
    print("Connection refused")
    print(ex)
