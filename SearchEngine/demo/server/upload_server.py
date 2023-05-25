""" 
WW Search Engine Upload Server 
By : Sebastian Mora (@bastian1110)
"""
from pipe.reader import Reader
from pipe.utils import embed, make_sentence
from flask import Flask, request, jsonify, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from uuid import uuid4
from dotenv import load_dotenv
import csv
import os


upload_server = Flask(__name__)
upload_server.config["SECRET_KEY"] = "secret!"
upload_server.config["CORS_HEADERS"] = "Content-Type"
socketio = SocketIO(upload_server, cors_allowed_origins="*")
CORS(upload_server)

load_dotenv()
DATABASE_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("TARGET_DB")
SQL_DATABASE = os.environ.get("SQL_FRIEND")


@upload_server.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
    except:
        return jsonify({"message": "Error, no file received", "error": True}), 400

    file_name = uuid4()
    file.save(f"./temp/{file_name}.csv")
    with open(f"./temp/{file_name}.csv", "r") as f:
        lines = f.readlines()
        headers = lines[0][:-1].split(",")
        headers = [word.lower() for word in headers]
        lines[0] = ",".join(headers) + "\n"

    with open(f"./temp/{file_name}.csv", "w") as f:
        f.writelines(lines)

    if "modelo" in headers:
        return (
            jsonify(
                {
                    "message": "File saved successfully!",
                    "lines": len(lines) - 1,
                    "attributes": headers,
                    "id": file_name,
                    "error": False,
                }
            ),
            200,
        )
    return (
        jsonify({"message": "Missing header <modelo>", "error": True}),
        400,
    )


@upload_server.route("/cancel", methods=["POST"])
def cancel():
    file = request.values.get("file_id")
    if not file:
        return jsonify({"message": "Error, no file key received", "error": True}), 400

    try:
        os.remove(f"./temp/{file}.csv")
        return jsonify({"message": "File deleted succesfully", "error": False}), 200
    except:
        return jsonify({"message": "Error deleting the file", "error": True}), 500


@socketio.on("start-processing")
def handle_start_processing(data):
    temp_reader = Reader(
        DATABASE_URI, SQL_DATABASE, DATABASE_NAME, embed, make_sentence
    )
    with open(f'./temp/{data["fileId"]}.csv', "r") as f:
        dict_reader = csv.DictReader(f)
        line = 1
        for row in dict_reader:
            temp_reader.read_row(row, data["agencyId"], data["make"], data["view"])
            emit("progress", {"number": line})
            line += 1
    temp_reader.push_to_db()
    os.remove(f'./temp/{data["fileId"]}.csv')
    del temp_reader


if __name__ == "__main__":
    socketio.run(upload_server, host="0.0.0.0", port=8082, allow_unsafe_werkzeug=True)
