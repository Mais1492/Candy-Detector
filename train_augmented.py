from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")

model.train(data="coco.yaml", epochs=100, hsv_h=0.03, hsv_s=0.6, hsv_v=0.5)

model.train(
    data="coco.yaml",
    epochs=100,
    hsv_h=0.0,
    hsv_s=0.0,
    hsv_v=0.0,
    translate=0.0,
    scale=0.0,
    fliplr=0.0,
    mosaic=0.0,
    erasing=0.0,
    auto_augment=None,
)

# Train the model
results = model.train(data="candy_dataset/data.yaml", epochs=50, imgsz=640)