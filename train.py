from ultralytics import YOLO

def main():
    model = YOLO("best.pt")

    model.train(
        data="candy_dataset/data.yaml",
        epochs=50,
        imgsz=640,
        # enable GPU-processing
        device=0
    )

if __name__ == "__main__":
    main()