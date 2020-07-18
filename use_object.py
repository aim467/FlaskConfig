from flask import Flask


from config import DevelopmentConfig

app = Flask(__name__)

# 使用真实的类
# app.config.from_object(DevelopmentConfig)

# 使用模块字符串
app.config.from_object("MyConfig.config.BaseConfig")


@app.route("/")
def index():
    return "Index Page, DEBUG=%s, SECRET_KEY=%s" % (app.config["DEBUG"], app.config["SECRET_KEY"])


if __name__ == "__main__":
    app.run(debug=True)
    print(app.config.items())