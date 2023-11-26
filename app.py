# Standard libary
import os
from datetime import datetime

# Third party library
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    start_date = datetime(2021, 1, 1)
    current_date = datetime.now()
    years_exp = current_date.year - start_date.year
    if (current_date.month, current_date.day) < (start_date.month, start_date.day):
        years_exp -= 1
    return render_template("home.html", years_exp=years_exp)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
