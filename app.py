import types
import os
import yaml


from flask import Flask


app = Flask(__name__)


def from_yaml(self, filename, silent=False):
    filename = os.path.join(self.root_path, filename)
    try:
        with open(filename) as yaml_file:
            obj = yaml.load(yaml_file.read(), Loader=yaml.FullLoader)
    except IOError as e:
        if silent:
            return False
    return self.from_mapping(obj)


def from_properties(self, filename, silent=False, encode=None):
    filename = os.path.join(self.root_path, filename)
    try:
        with open(filename) as properties_file:
            obj = {}
            for line in properties_file:
                if line.find('=') > 0:
                    s = line.replace('\n', '').split("=")
                    obj[s[0]] = s[1]
    except IOError as e:
        if silent:
            return False
    return self.from_mapping(obj)

# 为 config 对象动态添加 from_yaml 方法
app.config.from_yaml = types.MethodType(from_yaml, app.config)
app.config.from_yaml("config.yaml")

# 为 config 对象动态添加 from_properties 方法
app.config.from_properties = types.MethodType(from_properties, app.config)
app.config.from_properties("config.properties")


@app.route("/")
def index():
    return "Index Page, DEBUG=%s, SECRET_KEY=%s" % (app.config["DEBUG"], app.config["SECRET_KEY"])


if __name__ == "__main__":
    app.run(debug=True)
    print(app.config.items())