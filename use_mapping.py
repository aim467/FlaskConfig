from flask import Flask


app = Flask(__name__)


configs = {
    "DEBUG": True,
    "SECRET_KEY": "Something"
}

mapping = (
    {
        "DEBUG": True,
        "SECRET_KEY": "Something"
    }
)

mappings = (
    ('DEBUG', True),
    ('TESTING', True)
)

app.config.from_mapping(mappings)

@app.route("/")
def index():
    return "Index Page, DEBUG=%s, SECRET_KEY=%s" % (app.config["DEBUG"], app.config["SECRET_KEY"])


if __name__ == "__main__":
    app.run(debug=True)
    print(app.config.items())