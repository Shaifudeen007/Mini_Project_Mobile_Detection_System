

#  Mobile Detection System

A mini project that uses image processing and deep learning to detect the presence of mobile phones in a given environment and trigger alerts when detected. Ideal for classroom monitoring, exam halls, or secure areas where mobile usage is restricted.

##  Project Overview

The **Mobile Detection System** leverages the YOLOv8 (You Only Look Once) model to identify mobile phones in real-time from video feeds or images. Upon detection, the system sends an alert (such as a message or notification) to the concerned authority or system.

## Key Features

*  Real-time mobile phone detection using YOLOv8
*  Sends notification or alert when a mobile phone is detected
*  Uses state-of-the-art object detection with high accuracy
*  Logs and stores detection results with timestamps
*  Lightweight and easy to deploy on local systems

##  Tech Stack

| Component            | Technology Used               |
| -------------------- | ----------------------------- |
| Programming Language | Python                        |
| Deep Learning Model  | YOLOv8 (Ultralytics)          |
| Image Processing     | OpenCV                        |
| Alert System         | SMTP/Email/SMS (customizable) |
| Backend Logic        | Python Scripts                |
| Environment          | Jupyter Notebook / Script     |

##  How It Works

1. Capture live video or feed input.
2. Use YOLOv8 model to detect mobile phones in each frame.
3. If a phone is detected, trigger an alert.
4. Optionally log the detection time and frame.


##  Project Structure

```
mobile-detection-system/
│
├── detect_mobile.py         # Main detection script
├── requirements.txt         # Dependencies
├── yolov8_model/            # YOLOv8 weights and config
├── utils/                   # Helper functions
└── README.md                # Project documentation
```

##  Alert System

* Alerts can be customized via:

  * Email using SMTP
  * SMS using Twilio API
  * Push notifications (optional)

##  Team Members

* **Md Shaif** – Frontend & Model Integration
* **Guhan** – Alert System & Logging
* **Arul prasath** – Model Optimization & Testing





