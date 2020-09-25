# web_app/routes/model_routes.py

from flask import Blueprint, request, jsonify, render_template


model_routes = Blueprint("model_routes", __name__)

@model_routes.route("/predict", methods=["POST"])
def predict():
    tweet_text = request.form["tweet_text"]


    return render_template("prediction_results.html",
        tweet_text=tweet_text,
        screen_name_most_likely= result[0]
    )