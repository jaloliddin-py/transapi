import flask
from flask import request, jsonify
from translate import translate  # Assuming translate function is defined in `translate` module
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return flask.jsonify({"message": "Hello, World!"})

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    src = data.get("src")
    dest = data.get("dest")
    
    # Call the translate function from your imported module
    result = translate(text, src, dest)
    
    return jsonify({"translated_text": result}), 200

if __name__ == "__main__":
    app.run(debug=True)
