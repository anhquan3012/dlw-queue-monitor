# Vision-based Queue Monitoring System
A real-time people counting system for queue management at supermarkets, malls and public areas.

## Setting up
### Prerequisites
Please first install mmdetection library (```mmdet```) by following the instructions at https://mmdetection.readthedocs.io/en/latest/get_started.html#.

If you have problems with building ```pycocotools``` when trying to install ```mmdet```, please install ```pycocotools``` first by running this command.
```bash
conda install -c conda-forge pycocotools
```
After that you may install ```mmdet``` as per instructed.
```bash
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
```

### Clone the repo
```bash
git clone https://github.com/anhquan3012/dlw-queue-monitor.git
cd dlw-queue-monitor
```

### Install other dependencies
```bash
pip install -r requirements.txt
```

## Running demo on webcam
You could run the demo on webcam by running ```webcam_queue_monitor.py```.
```bash
python webcam_queue_monitor.py
```

You will a this window like this.
