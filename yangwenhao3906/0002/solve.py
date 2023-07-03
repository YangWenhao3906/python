# 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

from datetime import date
import hashlib

import pandas as pd
import pymysql

app_name = "red_alert_2"

def gen_activation_code_to_file(num, pwd):

    current_date = date.today().strftime("%Y-%m-%d")
    print("today: ", current_date)

    file_name = current_date + "-activation-code.csv"
    file = open(file_name, "w")
    print("file open")
    file.write("n,activation_code\n")

    for i in range(num):
        s = app_name + current_date + str(i) + pwd
        sha1_hash = hashlib.sha1(s.encode()).hexdigest()
        file.write(str(i)+","+sha1_hash+"\n")
        print(s)
        print(sha1_hash)

    file.close()

    return file_name

def store_activation_code_to_mysql(file_name):
    data = pd.read_csv(file_name)

    connection = pymysql.connect(
        host='localhost',
        user='myuser',
        password='password',
        database='pyexercise'
    )

    cursor = connection.cursor()

    for index, row in data.iterrows():
        sql = "INSERT INTO ex0002 (n, activation_code) VALUES (%s, %s)"
        values = (row['n'], row['activation_code'])
        cursor.execute(sql, values)

    # 提交更改
    connection.commit()

    # 关闭游标和连接
    cursor.close()
    connection.close()

file_name = gen_activation_code_to_file(200, "my_password")

store_activation_code_to_mysql(file_name)