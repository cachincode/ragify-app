import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import load_env
from index_manager import initialize_index

load_env()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["60 per hour", "240 per day"],
    storage_uri=os.getenv("MONGO_URI")
)

query_engine = initialize_index()

@app.route("/chats/<chatId>/query", methods=["GET"])
@limiter.limit("5 per minute")
def query_index(chatId):
    question = request.args.get("question")

    result = query_engine.query(question)

    return jsonify({
        "answer": result.response,
        "sources": result.get_formatted_sources()
    })

@app.route("/")
def home():
    return "Ragify App"
