import cv2
import time
import mediapipe as mp
from playsound import playsound
import threading

mp_face_mesh = mp.solutions.face_mesh # type: ignore
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
cap = cv2.VideoCapture(0)

eye_closed_start = None
alarm_on = False


def play_alarm():
    playsound('alarm.mp3')


def eye_closed(landmarks):
    # land mark to eye up and down y point
    left_eye = [landmarks[159], landmarks[145]]
    right_eye = [landmarks[386], landmarks[374]]
    left_dist = abs(left_eye[0].y - left_eye[1].y)
    right_dist = abs(right_eye[0].y - right_eye[1].y)
    print(left_dist,right_dist)
    return (left_dist < 0.02) and (right_dist < 0.02)


while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    closed = False
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            lm = face_landmarks.landmark
            # Draw square on left eye center (landmark 159)
            lx, ly = int(lm[159].x * w), int(lm[159].y * h)
            cv2.rectangle(frame, (lx-5, ly-5), (lx+5, ly+5), (0, 255, 0), 2)
            # Draw square on right eye center (landmark 386)
            rx, ry = int(lm[386].x * w), int(lm[386].y * h)
            cv2.rectangle(frame, (rx-5, ry-5), (rx+5, ry+5), (0, 255, 0), 2)

            if eye_closed(lm):
                # Draw square on left eye center (landmark 159)
                cv2.rectangle(frame, (lx - 5, ly - 5), (lx + 5, ly + 5), (255, 0, 0), 2)
                # Draw square on right eye center (landmark 386)
                cv2.rectangle(frame, (rx - 5, ry - 5), (rx + 5, ry + 5), (255, 0, 0), 2)
                closed = True

    if closed:
        if eye_closed_start is None:
            eye_closed_start = time.time()
        elif time.time() - eye_closed_start >= 3 and not alarm_on:
            alarm_on = True
            threading.Thread(target=play_alarm, daemon=True).start()
    else:
        eye_closed_start = None
        alarm_on = False

    cv2.imshow('MediaPipe Eye Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
