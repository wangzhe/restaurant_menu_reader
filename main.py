import os

from flask import Flask, render_template

import config
from model import menu_processor

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return "This is for the test 1 sample"


@app.route("/ocrdev")
def ocrdev():
    # read the image from folders
    menus_dev_set = "./samples/devset"
    for menu_filename in os.listdir(menus_dev_set):
        print(menu_filename)
        menu_processor.ocr_menu(menu_filename)

    return render_template("about.html")


def main():
    # initialize_app(app)
    app.run(host='0.0.0.0', port=config.PORT, debug=True)


if __name__ == "__main__":
    main()
