import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import load_env
from index_manager import initialize_index

load_env()

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

query_engine = initialize_index()

@app.route("/chats/<chatId>/query", methods=["GET"])
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
