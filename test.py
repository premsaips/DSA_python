import cv2
import time
import winsound
import numpy as np

# ---------------- PARAMETERS ----------------
DROWSY_FRAMES = 15

# ---------------- LOAD HAAR CASCADES ----------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# ---------------- VARIABLES ----------------
closed_frames = 0
drowsy = False
drowsy_event_count = 0
drowsy_start_time = None
total_drowsy_duration = 0.0
session_start_time = time.time()

# ---------------- GRAPH DATA ----------------
graph_points = []

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)
print("Driver Drowsiness Detection | Press Q to Exit")

while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ---------------- EYE DETECTION ----------------
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
    eyes_detected = len(eyes) > 0

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # ---------------- FACE DETECTION ----------------
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    face_detected = len(faces) > 0

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # ---------------- DROWSINESS LOGIC ----------------
    if not eyes_detected:

        closed_frames += 1

        if closed_frames >= DROWSY_FRAMES:

            if not drowsy:
                drowsy = True
                drowsy_start_time = time.time()
                drowsy_event_count += 1

            winsound.Beep(2500,200)

    else:

        if drowsy:
            total_drowsy_duration += time.time() - drowsy_start_time

        closed_frames = 0
        drowsy = False
        drowsy_start_time = None

    # ---------------- METRICS ----------------
    elapsed_minutes = (time.time() - session_start_time) / 60

    eye_closure_frequency = (
        drowsy_event_count / elapsed_minutes
        if elapsed_minutes > 0 else 0
    )

    # ---------------- DISPLAY STATUS ----------------
    y0 = 30
    dy = 30

    cv2.putText(frame,f"Drowsy Events: {drowsy_event_count}",
                (20,y0),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

    cv2.putText(frame,f"Drowsy Duration: {total_drowsy_duration:.1f} sec",
                (20,y0+dy),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

    cv2.putText(frame,f"Eye Closure Frequency: {eye_closure_frequency:.2f}/min",
                (20,y0+2*dy),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

    # STATUS 1
    status1 = "DROWSY" if drowsy else "NOT DROWSY"
    color1 = (0,0,255) if drowsy else (0,255,0)

    cv2.putText(frame,f"STATUS 1: {status1}",
                (20,y0+3*dy),cv2.FONT_HERSHEY_SIMPLEX,0.9,color1,2)

    # STATUS 2
    status2 = "FACE" if face_detected else "NO FACE"
    color2 = (0,255,0) if face_detected else (0,255,255)

    cv2.putText(frame,f"STATUS 2: {status2}",
                (20,y0+4*dy),cv2.FONT_HERSHEY_SIMPLEX,0.9,color2,2)

    # ---------------- GRAPH FRAME ----------------
    graph = np.zeros((300,600,3), dtype=np.uint8)

    # store drowsy state
    graph_points.append(1 if drowsy else 0)

    if len(graph_points) > 100:
        graph_points.pop(0)

    # draw graph
    for i in range(1,len(graph_points)):
        x1 = (i-1)*6
        y1 = 250 - graph_points[i-1]*200

        x2 = i*6
        y2 = 250 - graph_points[i]*200

        cv2.line(graph,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.putText(graph,"Live Drowsiness Graph",(180,30),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.putText(graph,"1 = Drowsy  |  0 = Alert",(180,60),
                cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),1)

    # ---------------- SHOW WINDOWS ----------------
    cv2.imshow("Driver Drowsiness Detection",frame)
    cv2.imshow("Drowsiness Graph",graph)

    if cv2.waitKey(1) & 0xFF in [ord('q'),ord('Q')]:
        break

cap.release()
cv2.destroyAllWindows()