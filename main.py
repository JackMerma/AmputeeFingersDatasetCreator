from config import *
from src.process.src import *
from src.gui.main import *
from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = UPLOAD_FOLDER
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': "No file part in the request"}), 400

    files = request.files.getlist('file')

    for file in files:
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return jsonify({'message': 'Files successfully uploaded'}), 200


@app.route("/")
def index():

    return render_template("index.html")
    """
    # Getting parser
    args = load_parser()

    if args.process:
        process(src_type=args.type, file_path=args.file)
    else: # No args loads the user interface
        gui()
    """


if __name__ == "__main__":
    app.run(debug=True)
