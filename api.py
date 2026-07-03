from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stock")
def stock():
    return jsonify({
        "normal": [
            {"fruit": "Rocket", "price": 5000},
            {"fruit": "Spin", "price": 7500},
            {"fruit": "Spring", "price": 60000},
            {"fruit": "Bomb", "price": 80000}
        ],
        "mirage": [
            {"fruit": "Dragon", "price": 15000000}
        ]
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)