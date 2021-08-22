from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_expects_json import expects_json

from util import Recommender
from util.config_loader import config
from util.logger import get_logger

logger = get_logger("main")

app = Flask(__name__)
CORS(app)

schema = {
    "type": "object",
    "properties": {
        "item": {"type": "string"},
        "age": {"type": "number"},
        "gender": {"type": "string"}
    },
    "required": ["item", "gender"]
}


@app.route('/item_recommendation', methods=['POST'])
@expects_json(schema)
def recommend_content():
    data = request.get_json()
    logger.info("Received api call, payload: %s", data)
    if "age" in data:
        result = Recommender.recommend_with_age(data['item'], data['gender'], data['age'])
    else:
        result = Recommender.recommend(data['item'], data['gender'])
    return jsonify(result)


if __name__ == '__main__':
    logger.info("Starting application using profile: %s", config['PROFILE']['name'])
    app.run(host=config['SERVER']['host'], port=int(config['SERVER']['port']))
