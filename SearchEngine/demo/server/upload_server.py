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
import csv
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
app.config["CORS_HEADERS"] = "Content-Type"
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

DATABASE_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("TARGET_DB")


@app.route("/upload", methods=["POST"])
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
        if "modelo" in headers or "Modelo" in headers:
            return (
                jsonify(
                    {
                        "message": "File saved successfully!",
                        "lines": len(lines) - 1,
                        "id": file_name,
                        "error": False,
                    }
                ),
                200,
            )
        os.remove(f"./temp/{file_name}.csv")
        return (
            jsonify({"message": "Missing header <modelo>", "error": True}),
            400,
        )


@app.route("/cancel", methods=["POST"])
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
    temp_reader = Reader(DATABASE_URI, DATABASE_NAME, embed, make_sentence)
    with open(f'./temp/{data["fileId"]}.csv', "r") as f:
        dict_reader = csv.DictReader(f)
        line = 1
        for row in dict_reader:
            temp_reader.read_row(row, "0")
            emit("progress", {"number": line})
            line += 1
    temp_reader.push_to_db()
    os.remove(f'./temp/{data["fileId"]}.csv')
    del temp_reader


if __name__ == "__main__":
    socketio.run(app, port=8080, debug=True)
