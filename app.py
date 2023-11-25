# Step 2: Create a new Flask application
from flask import Flask, render_template

app = Flask(__name__)


# Step 2: Define routes for your pages
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


# Step 4: Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
