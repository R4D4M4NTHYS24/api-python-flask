from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, origins=["http://localhost:4200"])

@app.route('/api/prices')
@cross_origin()
def get_prices():
    prices = {
        'bitcoin': 60589.12,
        'ethereum': 1973.26,
        'litecoin': 239.54
    }

    for key in prices:
        prices[key] = round(prices[key], 2)

    return jsonify(prices)


if __name__ == '__main__':
    app.run()
