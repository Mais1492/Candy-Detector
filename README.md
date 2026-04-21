# Candy Detector (YOLO)

This project trains a YOLO-based object detection model to detect candy objects using a custom dataset.

---

## Project Structure

- `train.py` – trains the YOLO model
- `extract_yolo.py` – splits dataset into train/val/test and generates `data.yaml` (
- `augment_desaturate.py` – creates augmented (desaturated) dataset images
- `cam.py` – runs real-time webcam detection
- `candy_dataset/` – dataset folder (images + labels), generated from label-studio, set up by `extract_yolo.py`
- `best.pt` trained YOLO model
