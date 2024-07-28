# Amputee Finger Dataset Creator

## Table of contents

1. [Introduction] (#intro)
2. [Installation] (#installation)
3. [How to use] (#usage)
    1. [Upload data] (#upload)
    2. [Configure the processing] (#configure)
    3. [Processing results] (#results)
4. [Notes] (#notes)


## Introduction

In this project, a system is created for the rapid labeling of areas of interest (AOI) on main elements (EOI) in RGB images. To achieve this, a local web project is developed, providing the necessary functionalities to adjust parameters, ranges, options, etc., in order to generate a list of JSON files for each image to be labeled. This is done because there are currently tools like VGG Annotator that allow for manual image labeling (placing keypoints on images, areas, objects, etc.). Additionally, there are other methods that combine AI to automate manual labeling. For example, a small percentage of the images to be processed are labeled manually, and the rest are predicted using deep learning models. Data augmentation can also be used to increase the number of images or data.

Now, this project aims to configure the areas of interest so they can be automatically processed and labeled using computer vision algorithms. Specifically, thresholding is used to identify two colors (one for the AOI and one for the EOI). The resulting output includes images with the initial thresholding (for both the EOI and AOI separately), which can be used in the future as part of training data, and a JSON file with the estimated position of the amputation (AOI). This is currently the key point of interest compared to areas that are not of interest, such as fingers without amputations, the wrist, etc. Finally, it is necessary to indicate that this work focuses on labeling the middle phalanx of the index finger, but any AOI and EOI could be used, even if it is not a hand.

## Installation <a name="installation"></a>

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

## How to use? <a name="usage"></a>

This app was made in Flask, and you need to run the project locally using:

``` bash
python main.py
```

After that, you need to open your browser and paste the given URL (e.g., http://127.0.0.1:5000). Now, you are enabled to use functionalities like:

### Upload your own data <a name="upload"></a>

You can use the Drag & Drop left section to upload files. You can load any kind of data (images, videos, and others), and the system will filter just images (png, jpg, and jpeg) and videos (mp4) files. If you upload videos, they will be automatically processed to create new images (video frames), and all of this data will be updated and processed in the `static/upload/` folder.

This section is shown in the following image:

![Upload section](https://github.com/JackMerma/AmputeeFingersDatasetCreator/blob/master/images/uploadSection.png)

### Configure the processing <a name="configure"></a>

You have the option to configure the AOI and EOI ranges and the visual feedback configurations for the AOI results, such as showing the bounding box or not, and showing the middle identified point or not. Regarding the ranges, you can configure them by modifying the sliders (you can review this source to modify the ranges: [HSV ranges](https://stackoverflow.com/questions/47483951/how-can-i-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-ima)).

This section is shown in the following image:

![Config section](https://github.com/JackMerma/AmputeeFingersDatasetCreator/blob/master/images/configsSection.png)

### Show the results <a name="results"></a>

Finally, you can review the results in the last section by scrolling through the images. Currently, the system shows all images, including the processed images, the binary EOI thresholding mask, and the AOI threshold mask.

Additionally, you can review the labeling images JSONs in the `datasets/` folder (with the same image file name). Here, you can obtain the coordinates of the middle point of the AOI and the bounding box points of the AOI as well.

This section is shown in the following image with some results:

![Result section](https://github.com/JackMerma/AmputeeFingersDatasetCreator/blob/master/images/resultSection.png)

## Note <a name="notes"></a>

The web system is slow at processing a lot of images. In the next versions, the app will run as a desktop program or use a parser (with commands).
