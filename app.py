from flask import Flask, render_template

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


if __name__ == '__main__':
    # app.run() 有一些参数可以设置
    app.run(host='0.0.0.0', port=5000, debug=True)
