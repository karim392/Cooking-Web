from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Recipes page
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

