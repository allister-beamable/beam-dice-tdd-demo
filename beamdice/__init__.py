from flask import Flask, jsonify
from . import dice


def create_app():
  app = Flask(__name__)

  @app.route('/dice')
  def dice_handler():
    return jsonify({'total': dice.roll()})

  return app
