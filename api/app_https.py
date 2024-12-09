# app_https.py

from flask import Flask, jsonify
import ssl
from pymongo import MongoClient
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes and all origins
CORS(app)


client = MongoClient("mongodb://localhost:27017/")
db = client["resto_db"]
collection = db["restaurants"]
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = list(collection.find({}, {"_id": 0}))  # Fetch all restaurants, excluding the _id field
    return jsonify(restaurants)

if __name__ == '__main__':
    # Path to your SSL certificate and key
    context = ('/mnt/c/Users/21651/projet_integ_si/nginx/ssl/nginx.crt', 
               '/mnt/c/Users/21651/projet_integ_si/nginx/ssl/nginx.key')
    
    app.run(debug=True, host="0.0.0.0", port=4443, ssl_context=context)
