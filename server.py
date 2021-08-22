from flask import Flask, request
from flask_cors import CORS
from flask_expects_json import expects_json

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
    if "age" in data:

    return "Success"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
