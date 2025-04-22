# Trinetra - Drowsiness Detection System 🚨👀

## Overview
A **real-time drowsiness and yawning detection system** using **Python, OpenCV, and Dlib**. This project detects when a driver (or user) is sleepy, drowsy, or yawning and triggers an alarm sound to alert them.

## Features
- Real-time face detection using Dlib's facial landmarks
- Eye Aspect Ratio (EAR) to detect closed eyes (sleeping) 😴
- Drowsiness detection (semi-closed eyes) 🥱
- Yawn detection using Mouth Aspect Ratio (MAR) 🫢
- Alarm sound when drowsiness, sleeping, or excessive yawning is detected 🔈
- Visual alerts (text + bounding boxes) on the screen 🖥️

## Installation ⚙️
1. Prerequisites:
- `Python 3.8+`

- `Alarm .wav file`

## Clone the repository
```bash
git clone https://github.com/Champ2979/Trinetra.git
cd Trinetra
```

## Install Dependencies
```bash
pip install -r requirements.txt
```
## Download the facial landmark predictor
- Download ```shape_predictor_68_face_landmarks.dat``` from [Dlib's model](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat).
- Extract and place it in the project folder.


## Add your alarm sound

- Place a ```.wav file``` (e.g., alarm.wav) in the project folder.

## Run the program
- python main.py

## How It Works 🔍
- Captures video from the webcam.

- Detects facial landmarks (eyes & mouth).

- Calculates EAR (Eye Aspect Ratio) to check if eyes are closed.

- Calculates MAR (Mouth Aspect Ratio) to detect yawning.

- Triggers an alarm if:
  - Eyes are closed for too long (sleeping).
  - Eyes are partially closed (drowsy).
  - Mouth is open wide (yawning).

## License
- MIT License

### If there is any issues related to project you can contact me on my Linkedin or mail me. I would be happy to solve your queries. Both links are in my bio.