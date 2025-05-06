from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

@app.route('/data', methonds=['GET'])
def get_data():
    json_path  = '../codes/nnct_news_data.json'
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            data = f.read()
        return jsonify(json.loads(data))
    else:
        return jsonify({"erroe": "File is not found"}), 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)