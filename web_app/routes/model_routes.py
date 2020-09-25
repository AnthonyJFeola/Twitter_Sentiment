# web_app/routes/model_routes.py

from flask import Blueprint, request, jsonify, render_template

import numpy as np
import pickle

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

import spacy

maxlen = 500

restored_model = load_model('web_app/Twitter_Sentiment_Classification.h5')

with open('web_app/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

nlp = spacy.load('web_app/en_core_web_md/en_core_web_md-2.3.1')

def spacy_cleaning(df_col):
  doc = nlp(df_col)
  clean_doc = [token.lemma_ for token in doc if (token.is_stop != True) and (token.is_punct != True)]
  return clean_doc

def predict_on_new(input, tokenizer=tokenizer, restored_model=restored_model, maxlen=maxlen):
  i = spacy_cleaning(input)
  j = ' '.join(i)
  X_pred_seq = tokenizer.texts_to_sequences([j])
  X_pred = sequence.pad_sequences(X_pred_seq, maxlen)
  pred = restored_model.predict(X_pred)
  sentiment = np.argmax(pred, axis=1)[0]
  if sentiment == 0:
    sentiment = 'Negative'
  elif sentiment == 1:
    sentiment = 'Neutral'
  elif sentiment == 2:
    sentiment = 'Positive'
  return sentiment

model_routes = Blueprint("model_routes", __name__)

@model_routes.route("/predict", methods=["POST"])
def predict():
    tweet_text = request.form["tweet_text"]
    sentiment = predict_on_new(tweet_text)
    return render_template("prediction_results.html",
        tweet_text=tweet_text,
        sentiment=sentiment,
        model_summary=restored_model.summary()
    )