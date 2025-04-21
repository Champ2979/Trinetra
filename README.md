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
## Create .env file:
```bash
OPENWEATHER_API_KEY="your_api_key_here"
```

## Follow notebook steps to:

- Train model on historical data
- Save trained model
- Get 5-day forecasts
- Make predictions using the saved model

## API Key Setup
- Get free API key from OpenWeatherMap

- Add to .env file:
```bash
OPENWEATHER_API_KEY="your_actual_key_here"
```
## Model Performance
- Training Accuracy: 85.42%
- Testing Accuracy: 84.74%

### Confusion Matrix visualization included

## Dependencies
- Python 3.8+

- scikit-learn

- pandas

- matplotlib

- requests

- python-dotenv

- joblib

## License
- MIT License

## Acknowledgements
- Dataset: Seattle Weather Dataset
- Weather API: OpenWeatherMap

