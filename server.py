from flask import Flask, request
from flask_cors import CORS

from content_recommendation import Content, recommendation

app = Flask(__name__)
CORS(app)

@app.route('/item_recommendation', methods=['POST'])

def recommend_content():
        instance = request.get_json(silent=True)
        text1 = instance["text1"]
        text2 = instance["text2"]
        text3 = instance["text3"]
        content = Content(text1, text2, text3)

        return recommendation()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
