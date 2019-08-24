import os
from flask import Flask,render_template, url_for, json,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "", "cards.json")
    data = json.load(open(json_url))
    return jsonify(data)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
