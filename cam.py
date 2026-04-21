import cv2
from ultralytics import YOLO

model = YOLO("best.pt")
 
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    raise RuntimeError("Could not open webcam")
 
while True:
    ret, frame = cap.read()
    if not ret:
        break
 
    # YOLO Prediction
    results = model(frame)
 
    # Plotting
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Candy-Detection", annotated_frame)
 
    # 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()