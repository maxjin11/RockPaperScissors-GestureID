# Rock, Paper, Scissors, AI?

This set of scripts identifies human gestures using OpenCV and Mediapipe, while identifying them with Scikit-Learn's RandomForestClassifier model.
Currently, this script + dataset combination is limited to identifying the gestures used in the Rock, Paper, Scissors game that we all know and love, but by making changes to image_processor.py, running it, and running create_dataset.py before running the remaining files, the script can detect other gestures as well.

This set of scripts uses hand landmarks and their X/Y coordinates to successfully identify the gesture.

This project was inspired by Felipe's (Computer Vision Engineer) video on Sign Language Detection. Go check him out!
Below I have linked his video and his github repository.
Repository: https://github.com/computervisioneng/sign-language-detector-python/tree/master
Youtube Video: https://youtu.be/MJCSjXepaAM?si=p3f2DFY8xj4G3NqZ

Repository created by Max Jin, May 2024.
Last edited May 5th, 2024.
