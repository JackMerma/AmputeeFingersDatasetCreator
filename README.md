# Amputee Finger Dataset Creator

## Installation

First, please create a virtual environment (optional), for example:

``` bash
virtualenv venv
```

Then, create a `src` folder and clone this repository inside it:

``` bash
mkdir src
cd src/
git clone git@github.com:JackMerma/AmputeeFingersDatasetCreator.git .
```

Install the required libraries:

``` bash
pip install -r requirements.txt
```

## How to use?

This app was made in Flask, and you need to run the project locally using:

``` bash
python main.py
```

After that, you need to open your browser and paste the given URL (e.g., http://127.0.0.1:5000). Now, you are enabled to use functionalities like:

### Upload your own data

You can use the Drag & Drop left section to upload files. You can load any kind of data (images, videos, and others), and the system will filter just images (png, jpg, and jpeg) and videos (mp4) files. If you upload videos, they will be automatically processed to create new images (video frames), and all of this data will be updated and processed in the `static/upload/` folder.

This section is shown in the following image:

![Upload section](#)

### Configure the processing

You have the option to configure the AOI and EOI ranges and the visual feedback configurations for the AOI results, such as showing the bounding box or not, and showing the middle identified point or not. Regarding the ranges, you can configure them by modifying the sliders (you can review this source to modify the ranges: [HSV ranges](https://stackoverflow.com/questions/47483951/how-can-i-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-ima)).

This section is shown in the following image:

![Config section](#)

### Show the results

Finally, you can review the results in the last section by scrolling through the images. Currently, the system shows all images, including the processed images, the binary EOI thresholding mask, and the AOI threshold mask.

Additionally, you can review the labeling images JSONs in the `datasets/` folder (with the same image file name). Here, you can obtain the coordinates of the middle point of the AOI and the bounding box points of the AOI as well.

This section is shown in the following image with some results:

![Result section](#)

## Note

The web system is slow at processing a lot of images. In the next versions, the app will run as a desktop program or use a parser (with commands).
