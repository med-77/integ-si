from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # Import CORS
from OpenSSL import SSL

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["resto_db"]
collection = db["restaurants"]

@app.route("/api/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = list(collection.find({}, {"_id": 0}))  # Fetch all restaurants, excluding the _id field
    return jsonify(restaurants)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # For HTTP
