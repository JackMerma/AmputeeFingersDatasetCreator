from config import *
from src.process.src import *
from src.gui.main import *
from flask import Flask, render_template, jsonify, request, redirect, url_for
import os

app = Flask(__name__)
COMPLETED_UPLOAD_PATH = os.path.join(UPLOAD_FOLDER_BASE, UPLOAD_FOLDER_MAIN)
COMPLETED_TEMP_PATH = os.path.join(UPLOAD_FOLDER_BASE, TEMP_FOLDER)
app.config["UPLOAD_PATH"] = COMPLETED_UPLOAD_PATH

if not os.path.exists(COMPLETED_UPLOAD_PATH):
    os.makedirs(COMPLETED_UPLOAD_PATH)


@app.route("/upload", methods=["POST"])
def upload_file():

    message = ""

    if 'file' not in request.files:
        message += "No file part in the request\n"

    files = request.files.getlist('file')

    # Cleaning files data
    if os.path.exists(COMPLETED_UPLOAD_PATH):
        remove_folder(os.path.join(UPLOAD_FOLDER_BASE, UPLOAD_FOLDER_MAIN))
    os.makedirs(COMPLETED_UPLOAD_PATH)

    for file in files:
        if file.filename == '':
            message += "No selected file\n"

        if file:
            file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))


    # Persistance
    middle_aoi = request.args.get('middleAOIswitch')
    aoi_bounding_box = request.args.get('boundingboxAOIswitch')

    image_paths, videos_paths = filter_images_and_videos(COMPLETED_UPLOAD_PATH)
    image_paths += videos_paths
    image_paths = None if image_paths != None and len(image_paths) == 0 else image_paths
    message = None if message == "" else message

    # AOI configs and image files configs persistance
    context = {
            "checkboxes" : {
                "middle_aoi": middle_aoi is not None,
                "aoi_bounding_box": aoi_bounding_box is not None,
                },
            "files": image_paths,
            "processed_images": None,
            "message": message,
            "aoiH": {"min": 0, "max": 179},
            "aoiS": {"min": 0, "max": 255},
            "aoiV": {"min": 0, "max": 255},
            "eoiH": {"min": 0, "max": 179},
            "eoiS": {"min": 0, "max": 255},
            "eoiV": {"min": 0, "max": 255},
            "files": image_paths,
            "processed_images": None,
            }

    print(context)
    
    return redirect(url_for('index', context=context))


@app.route("/run", methods=["GET"])
def run_solution():

    # Reading AOI configs
    middle_aoi = request.args.get('middleAOIswitch')
    aoi_bounding_box = request.args.get('boundingboxAOIswitch')

    # Getting HSV values for AOI and EOI
    aoi_h_min = request.args.get('aoiHMin')
    aoi_h_max = request.args.get('aoiHMax')
    aoi_s_min = request.args.get('aoiSMin')
    aoi_s_max = request.args.get('aoiSMax')
    aoi_v_min = request.args.get('aoiVMin')
    aoi_v_max = request.args.get('aoiVMax')

    aoi_values = [[aoi_h_min, aoi_h_max], [aoi_s_min, aoi_s_max], [aoi_v_min, aoi_v_max]]

    # Capturar eoiH, eoiS, eoiV
    eoi_h_min = request.args.get('eoiHMin')
    eoi_h_max = request.args.get('eoiHMax')
    eoi_s_min = request.args.get('eoiSMin')
    eoi_s_max = request.args.get('eoiSMax')
    eoi_v_min = request.args.get('eoiVMin')
    eoi_v_max = request.args.get('eoiVMax')

    eoi_values = [[eoi_h_min, eoi_h_max], [eoi_s_min, eoi_s_max], [eoi_v_min, eoi_v_max]]

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
            process(src_type="img", file_path=completed_path, m_aoi=middle_aoi != None, bb_aoi=aoi_bounding_box != None, aoi_values=aoi_values, eoi_values=eoi_values)

    image_paths = None if image_paths != None and len(image_paths) == 0 else image_paths
    image_completed_paths = get_processed_files_paths()
    image_completed_paths = None if len(image_completed_paths) == 0 else image_completed_paths

    # AOI configs and image files configs persistance
    context = {
            "checkboxes" : {
                "middle_aoi": middle_aoi is not None,
                "aoi_bounding_box": aoi_bounding_box is not None,
                },
            "aoiH": {"min": aoi_h_min, "max": aoi_h_max},
            "aoiS": {"min": aoi_s_min, "max": aoi_s_max},
            "aoiV": {"min": aoi_v_min, "max": aoi_v_max},
            "eoiH": {"min": eoi_h_min, "max": eoi_h_max},
            "eoiS": {"min": eoi_s_min, "max": eoi_s_max},
            "eoiV": {"min": eoi_v_min, "max": eoi_v_max},
            "files": image_paths,
            "processed_images": image_completed_paths,
            "message": ""
            }

    return render_template('index.html', context=context)


@app.route("/", methods=["GET"])
def index():

    context = request.args.get('context', None)

    if context:
        context = eval(context)  # convert string back to dict, not recommended for actual production use
    else:
        context = {
                "checkboxes" : {
                    "middle_aoi": False,
                    "aoi_bounding_box": False,
                    },
                "aoiH": {"min": 0, "max": 179},
                "aoiS": {"min": 0, "max": 255},
                "aoiV": {"min": 0, "max": 255},
                "eoiH": {"min": 0, "max": 179},
                "eoiS": {"min": 0, "max": 255},
                "eoiV": {"min": 0, "max": 255},
                "files": None,
                }

    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)
