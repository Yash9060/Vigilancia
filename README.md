# Vigilancia

Vigilancia is a video sureveillance system designed to assist security staff for identifying anomalous activities, events and items. This project is currently under development. It is a final year university project of a team consisting of four students.

## Disclaimer
Install it at your own risk. We are not responsible for any damage happens to your machine due to Vigilancia. We have tested this software on our laptop and it is working without any issues.

## Dependencies
Install following dependencies to get Vigilancia working for you.
* Python 3
* Tensorflow (GPU version recommended).
* Keras (with TF backend).
* PyQt 4
* OpenCV
* MongoDB
* PyMongo (Python wrapper for MongoDB).

We recommend that you use GPU for running Vigilancia as it uses deep learning for video surveillance. We have not tested its performance on CPU.

## Starting Vigilancia for first time
When starting Vigilancia for first time you have to do following steps. From subsequent runs go directly to Start Vigilancia tab.
1. Make sure that mongodb service is running. To enable mongodb service execute following command.
```
  sudo systemctl enable mongodb
```

2. Run following command from root directory of Vigilancia.
```
  bash scripts/generate_db.sh
```

## Start Vigilancia
To start Vigilancia open terminal in root directory of source code and then execute following command:
```
  bash scripts/start.sh
```
It will download all necessary files and data.
Once Viglancia has started it will ask for username and password. Default username is `admin` and password is `admin`.
Enter username and password to start Vigilancia.

## Datasets
We used following datasets to train various deep learning models used in Vigilancia:
* [WIDER Event Recogntion dataset](http://yjxiong.me/event_recog/WIDER/)
* [Unusual Activity Detection dataset](http://mha.cs.umn.edu/proj_events.shtml)
* [Firearm Detection dataset](http://sci2s.ugr.es/weapons-detection)

## Credits
We would like to give credits to following tools / libraries / implementations:
* [Darkflow](https://github.com/thtrieu/darkflow)
* [Keras](https://github.com/keras-team/keras)
* [TensroFlow](https://github.com/tensorflow/tensorflow)
* [YOLO](https://pjreddie.com/darknet/yolo/)

## References
* [Recognize Complex Events from Static Images by Fusing Deep Channels](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Xiong_Recognize_Complex_Events_2015_CVPR_paper.pdf)
* [Automatic Handgun Detection Alarm in Videos Using Deep Learning](https://arxiv.org/abs/1702.05147)
* [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242)
* [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)
