import cv2
from ultralytics import YOLO
 
# Modell laden (Pfad anpassen!)
model = YOLO("./runs/detect/train7/weights/best.pt")
 
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    raise RuntimeError("Could not open webcam")
 
while True:
    ret, frame = cap.read()
    if not ret:
        break
 
    # YOLO Prediction
    results = model(frame)
 
    # Ergebnisse visualisieren
    annotated_frame = results[0].plot()
 
    # Anzeigen
    cv2.imshow("YOLO Candy Detection", annotated_frame)
 
    # Beenden mit 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()