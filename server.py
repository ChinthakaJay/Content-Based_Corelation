from flask import Flask, request
from flask_cors import CORS
from flask_expects_json import expects_json

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
    # if "age" in data:

    return "Success"


if __name__ == '__main__':
    logger.info("Starting application using profile: %s", config['PROFILE']['name'])
    app.run(host=config['SERVER']['host'], port=int(config['SERVER']['port']), debug=True)
