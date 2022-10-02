# Vision-based Queue Monitoring System

Watch the demo video here: https://youtu.be/gUTV3HvWWVg.

## Setting up

### Clone the repo
```bash
git clone https://github.com/anhquan3012/dlw-queue-monitor.git
cd dlw-queue-monitor
```

### Install mmdetection
Please install mmdetection library (```mmdet```) by following the instructions at https://mmdetection.readthedocs.io/en/latest/get_started.html#installation.

If you have problems with building ```pycocotools``` when trying to install ```mmdet```, please install ```pycocotools``` first it by running this command.
```bash
conda install -c conda-forge pycocotools
```
After that you may install ```mmdet``` as per instructed.
```bash
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
```

### Install other dependencies
```bash
pip install -r requirements.txt
```

### Install model configs and model weight
Our model use YOLOv3 with DarkNet53 Backbone with mixed precision training. Download the model configs and weights by running this command.
```bash
mim download mmdet --config  yolov3_d53_fp16_mstrain-608_273e_coco --dest .
```

You may use any model from mmdetection Model Zoo (https://mmdetection.readthedocs.io/en/latest/model_zoo.html#baselines). However, you will need to change the model file path inside the python files ```webcam_demo.py```, or ```video_demo.py``` (which ever files you are going to use).

## Running demo on webcam
You could run the demo on webcam by running ```webcam_demo.py```.
```bash
python webcam_demo.py
```

## Running demo on video
You could run the demo on a video by running ```video_demo.py``` (please lower the video frame rates and resolution before running).
```bash
python video_demo.py
```
