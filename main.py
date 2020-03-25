from flask import Flask, render_template

import config

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sample")
def sample():
    return "This is for the test 1 sample"


@app.route("/about")
def about():
    return render_template("about.html")


def main():
    # initialize_app(app)
    app.run(host='0.0.0.0', port=config.PORT, debug=True)


if __name__ == "__main__":
    main()
