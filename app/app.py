from functools import wraps

import jsonschema
import werkzeug
from flask import Flask, jsonify, request

from model import LangClassifier

classifier = LangClassifier()

schema = schema = {
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
        }
    },
    "required": ["text"],
}


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            jsonschema.validate(request.json, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            return jsonify({"error": e.message})
        return f(*args, **kwargs)

    return wrapper


app = Flask(__name__)


@app.route("/predict/", methods=["POST"])
@validate_json
def predict():
    data = request.get_json()
    return classifier.predict(data["text"])


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return jsonify({"error": "bad request!"}), 400


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
