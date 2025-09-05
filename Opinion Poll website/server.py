from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

JSON_DATA_FILE = "data.json"

if not os.path.exists(JSON_DATA_FILE):
    with open(JSON_DATA_FILE, "w") as f:
        json.dump([], f)

def read_data():
    with open(JSON_DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(JSON_DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    all_data = read_data()
    all_data.append(data)
    write_data(all_data)
    return jsonify({"message": "Survey submitted!"}), 200

@app.route("/results")
def results():
    all_data = read_data()
    return render_template("results.html", answers=all_data)

if __name__ == "__main__":
    app.run(debug=True)
