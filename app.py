from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT provided by Render
    app.run(host='0.0.0.0', port=port)        # Bind to 0.0.0.0 for public access
