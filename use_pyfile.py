from flask import Flask


app = Flask(__name__)

# 从 python 文件导入配置
app.config.from_pyfile("settings.py")

@app.route("/")
def index():
    return "Index Page, DEBUG=%s, SECRET_KEY=%s" % (app.config["DEBUG"], app.config["SECRET_KEY"])


if __name__ == "__main__":
    app.run(debug=True)
    print(app.config.items())