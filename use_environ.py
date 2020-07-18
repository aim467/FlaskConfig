import os


from flask import Flask


app = Flask(__name__)

# 设置环境变量
os.environ.setdefault("Flask_Config", "settings.py")

# 从环境变量中获取配置文件名
app.config.from_envvar("Flask_Config")


@app.route("/")
def index():
    return "Index Page, DEBUG=%s, SECRET_KEY=%s" % (app.config["DEBUG"], app.config["SECRET_KEY"])


if __name__ == "__main__":
    app.run(debug=True)
    print(app.config.items())

