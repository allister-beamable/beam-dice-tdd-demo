from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/dice')
def dice():
  return jsonify({'total': 6})
