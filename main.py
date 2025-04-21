import cv2
import numpy as np
import dlib
from imutils import face_utils
import winsound
import time

cap = cv2.VideoCapture(0) #camera initialization

# Load Dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


sleep = 0
drowsy = 0
active = 0
yawn_count = 0
status = ""
color = (0, 0, 0)

EYE_DROWSY_THRESH = 0.25
EYE_SLEEP_THRESH = 0.21
YAWN_THRESH = 0.75


last_alarm_time = 0
ALARM_COOLDOWN = 3  
ALARM_SOUND = "alarm.wav" 

def play_alarm():
    try:
        winsound.PlaySound(ALARM_SOUND, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sound: {e}")

def compute(ptA, ptB): # Compute Euclidean distance
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f): # Eye aspect ratio (EAR) function
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > EYE_DROWSY_THRESH:
        return 2  # open
    elif EYE_SLEEP_THRESH < ratio <= EYE_DROWSY_THRESH:
        return 1  # drowsy
    else:
        return 0  # closed

# Mouth aspect ratio (MAR) function
def mouth_aspect_ratio(mouth):
    A = compute(mouth[2], mouth[10])  # 63, 67
    B = compute(mouth[4], mouth[8])   # 65, 61
    C = compute(mouth[0], mouth[6])   # 60, 64
    mar = (A + B) / (2.0 * C)
    return mar

# Main loop
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # Eye blinking detection
        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], 
                             landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44],
                              landmarks[47], landmarks[46], landmarks[45])

        # Yawn detection
        mouth = landmarks[48:68]
        mar = mouth_aspect_ratio(mouth)

        if mar > YAWN_THRESH:
            yawn_count += 1
            cv2.putText(frame, "Yawning!", (100, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        else:
            yawn_count = 0

        # Eye-based state detection
        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "Active :)"
                color = (0, 255, 0)

        # Trigger Yawn alert too
        if yawn_count >= 10:
            status = "Yawning - Take a break!"
            color = (0, 0, 255)

        # Play alarm if status indicates drowsiness, sleeping, or yawning
        if status in ["SLEEPING !!!", "Drowsy !", "Yawning - Take a break!"]:
            current_time = time.time()
            if (current_time - last_alarm_time) > ALARM_COOLDOWN:
                play_alarm()
                last_alarm_time = current_time

       
        cv2.putText(frame, status, (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for (x, y) in landmarks:
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

  
    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()