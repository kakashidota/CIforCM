from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/dev")
def dev():
    return "This is the dev enviorment"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
