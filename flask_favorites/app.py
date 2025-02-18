from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

#load json data
def load_favorite_things():
    with open("favorite_things.json") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")  #when the user visit the home page it renders the index.html file

@app.route("/activities")
def activities():
    data = load_favorite_things()
    return render_template("activities.html", activities=data[favorite_things])

@app.route("/api/activities")
def api_activities():
    data = load_favorite_things()
    return jsonify(data)

