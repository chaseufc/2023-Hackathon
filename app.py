from flask import Flask, request, jsonify
from flask_cors import CORS
import calling_api

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=["POST"])
def call_all():
    try:
        text = request.json["text"]
    except KeyError:
        return jsonify({"error": "Invalid request body."}), 400
    
    try:
        final = calling_api.calling_all(text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    response = jsonify({"output": final})

    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
