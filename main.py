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


@app.route("/run", methods=["GET"])
def run_solution():
    middle_aoi = request.args.get('middleAOIswitch')
    aoi_bounding_box = request.args.get('boundingboxAOIswitch')
    print(middle_aoi)
    print(aoi_bounding_box)

    context = {
            "checkboxes" : {
                "middle_aoi": middle_aoi is not None,
                "aoi_bounding_box": aoi_bounding_box is not None,
                }
            }
    print(context)

    return render_template('index.html', context=context)


@app.route("/")
def index():

    context = {
            "checkboxes" : {
                "middle_aoi": False,
                "aoi_bounding_box": False,
                }
            }

    return render_template("index.html", context=context)
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
