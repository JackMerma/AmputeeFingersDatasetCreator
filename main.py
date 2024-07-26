from config import *
from src.process.src import *
from src.gui.main import *
from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)
COMPLETED_UPLOAD_PATH = os.path.join(UPLOAD_FOLDER_BASE, UPLOAD_FOLDER_MAIN)
COMPLETED_TEMP_PATH = os.path.join(UPLOAD_FOLDER_BASE, TEMP_FOLDER)
app.config["UPLOAD_PATH"] = COMPLETED_UPLOAD_PATH

if not os.path.exists(COMPLETED_UPLOAD_PATH):
    os.makedirs(COMPLETED_UPLOAD_PATH)


@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': "No file part in the request"}), 400

    files = request.files.getlist('file')

    for file in files:
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        if file:
            if not os.path.exists(COMPLETED_UPLOAD_PATH):
                os.makedirs(COMPLETED_UPLOAD_PATH)
            file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))

    return jsonify({'message': 'Files successfully uploaded'}), 200


@app.route("/run", methods=["GET"])
def run_solution():

    # Reading AOI configs
    middle_aoi = request.args.get('middleAOIswitch')
    aoi_bounding_box = request.args.get('boundingboxAOIswitch')

    ###################
    # Processing data #
    ###################

    # 1. Filtering images and videos files
    image_paths, videos_paths = filter_images_and_videos(COMPLETED_UPLOAD_PATH)

    # 2. Process videos and transforming in images
    for video_path in videos_paths:
        image_paths += convert_video_to_images(COMPLETED_UPLOAD_PATH, video_path)

    # 3. Process images
    if middle_aoi != None or aoi_bounding_box != None:

        # Deleting existing output images
        remove_folder(os.path.join(UPLOAD_FOLDER_BASE, TEMP_FOLDER))

        # Processing images
        for image_path in image_paths:
            completed_path = os.path.join(COMPLETED_UPLOAD_PATH, image_path)
            process(src_type="img", file_path=completed_path, m_aoi=middle_aoi != None, bb_aoi=aoi_bounding_box != None)

    image_paths = None if image_paths != None and len(image_paths) == 0 else image_paths
    image_completed_paths = get_processed_files_paths()
    image_completed_paths = Nonen if len(image_completed_paths) == 0 else image_completed_paths

    # AOI configs and image files configs persistance
    context = {
            "checkboxes" : {
                "middle_aoi": middle_aoi is not None,
                "aoi_bounding_box": aoi_bounding_box is not None,
                },
            "files": image_paths,
            "processed_images": image_completed_paths
            }
    
    return render_template('index.html', context=context)


@app.route("/")
def index():

    context = {
            "checkboxes" : {
                "middle_aoi": False,
                "aoi_bounding_box": False,
                },
            "files": None,
            }

    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
