# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)
about_routes = Blueprint("about_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")

@about_routes.route("/about")
def about():
    return render_template("about.html")