# 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

from datetime import date
import hashlib

app_name = "red_alert_2"

def gen_activation_code(num, pwd):

    current_date = date.today().strftime("%Y-%m-%d")
    print("today: ", current_date)

    file_name = current_date + "-activation-code"
    file = open(file_name, "w")
    print("file open")

    for i in range(num):
        s = app_name + current_date + str(i) + pwd
        sha1_hash = hashlib.sha1(s.encode()).hexdigest()
        file.write(sha1_hash+"\n")
        print(s)
        print(sha1_hash)

    file.close()

gen_activation_code(200, "my_password")