""" 
WW Search Engine Server 
By : Sebastian Mora (@bastian1110)
"""
from flask import Flask, request, jsonify, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from uuid import uuid4
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
app.config["CORS_HEADERS"] = "Content-Type"
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
    except:
        return jsonify({"message": "Error, no file received", "error": True}), 403

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
                        "lines": len(lines),
                        "id": file_name,
                        "error": False,
                    }
                ),
                200,
            )
        os.remove(f"./temp/{file_name}.csv")
        return (
            jsonify({"message": "Missing header <modelo>", "error": True}),
            402,
        )


@app.route("/cancel", methods=["POST"])
def cancel():
    file = request.values.get("file_id")
    if not file:
        return jsonify({"message": "Error, no file key received", "error": True}), 403

    try:
        os.remove(f"./temp/{file}.csv")
    except:
        return jsonify({"message": "Error deleting the file", "error": True}), 404


@socketio.on("start-processing")
def handle_start_processing(data):
    with open(f'./temp/{data["fileId"]}.csv', "r") as f:
        for i, line in enumerate(f):
            emit("progress", {"number": i})
            socketio.sleep(0.01)
    os.remove(f'./temp/{data["fileId"]}.csv')


if __name__ == "__main__":
    socketio.run(app, port=8080, debug=True)
