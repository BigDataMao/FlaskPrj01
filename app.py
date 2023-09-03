from flask import Flask, render_template, request
import pymysql

# app = Flask(__name__) 这是默认的写法
# 但是如果我们把这个文件放到了其他的文件夹下面，那么就需要指定一下
# __name__ 是当前文件的名字，也就是 app.py
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/get/news')
def get_news():
    return render_template('news.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        return render_template('account.html')
    user = request.form.get('user')
    passwd = request.form.get('passwd')
    name = request.form.get('name')
    gender = request.form.get("gender")
    city = request.form.get("city")
    email = request.form.get("email")

    print(user, passwd, name, gender, city, email)

    # 保存到数据库
    conn = pymysql.connect(host="txy", port=3306, user="root", password="mxw19910712@MYSQL", database="flask", charset="utf8")
    cursor = conn.cursor()
    sql = "insert into account values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, [user, passwd, name, 1, city, email])
    conn.commit()
    conn.close()

    return "提交成功"


if __name__ == '__main__':
    # app.run() 有一些参数可以设置
    app.run(host='0.0.0.0', port=5000, debug=True)
