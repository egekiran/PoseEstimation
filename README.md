# Pose Estimation using YOLOv8
This repository contains a pose estimation project built using OpenCV and the YOLOv8 model. The implementation detects and classifies human poses, such as laying, sitting, and walking, based on the position of key body landmarks.
# Introduction
This project uses the YOLOv8 model for real-time pose detection. The model is fine-tuned for human pose estimation and can recognize several common human poses: laying, sitting, and walking. The detected poses are then annotated on the video feed with bounding boxes and labels.
# Dependencies
- OpenCV
- Ultralytics YOLOv8
# How It Works
The project uses key points from the YOLOv8 model to determine the pose of a person. The key points correspond to various body parts such as shoulders, hips, knees, and feet. Based on the relative positions of these key points, the following poses are detected:
- Laying: Identified when the shoulder and hip positions are at similar vertical levels.
- Sitting: Detected when the shoulders are above the hips, and the hips are above the knees.
- Walking: Recognized by analyzing the relative distances between knees and feet.
# Custom Video
You can replace the default 'test.mp4' video with your own video footage.
# Future Improvements
- Support for more pose classifications (e.g., standing, running).
- Enhanced accuracy by fine-tuning detection thresholds.
- Integration with a GUI for easier use.
# Contributing
This project is open for contributions! If you have any ideas or improvements, feel free to submit a pull request or open an issue. Suggestions are always welcome.
