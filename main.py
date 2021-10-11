import os
from flask import Flask, jsonify, request
from transformers import pipeline

model_path = "./model"

app = Flask(__name__)

@app.route("/")
def run():
    api_key=str(request.args.get('api_key'))
    text=str(request.args.get('text'))
    if(api_key=="julmo123"):
        classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
        return classify(text)[0]
    else:
        return print("Wrong Api key")

if __name__ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))