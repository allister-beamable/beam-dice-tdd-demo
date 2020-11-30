from flask import Flask, jsonify


def create_app():
  app = Flask(__name__)

  @app.route('/dice')
  def dice_handler():
    return jsonify({'total': 6})

  return app
