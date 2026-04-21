import shutil
from pathlib import Path

import json
from pathlib import Path


def create_data_yaml(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)

    notes_file = input_path / "notes.json"

    if not notes_file.exists():
        raise FileNotFoundError("notes.json not found")

    with open(notes_file, "r") as f:
        data = json.load(f)

    categories = data.get("categories")
    if not categories:
        raise ValueError("No 'categories' field in notes.json")

    # Sort by id to ensure correct order
    categories = sorted(categories, key=lambda x: int(x["id"]))

    # Build YAML manually
    lines = [
        f"path: {output_path.resolve()}",
        "train: images/train",
        "val: images/val",
        "test: images/test",
        "",
        "names:"
    ]

    for cat in categories:
        lines.append(f"  {cat['id']}: {cat['name']}")

    with open(output_path / "data.yaml", "w") as f:
        f.write("\n".join(lines))

    print("data.yaml created")

def split_and_copy(input_path, output_path="candy_dataset"):
    input_path = Path(input_path)
    output_path = Path(output_path)

    images_src = input_path / "images"
    labels_src = input_path / "labels"

    # Destination folders
    splits = ["train", "test", "val"]
    for split in splits:
        (output_path / "images" / split).mkdir(parents=True, exist_ok=True)
        (output_path / "labels" / split).mkdir(parents=True, exist_ok=True)

    # Get all image files
    image_files = sorted([f for f in images_src.iterdir() if f.is_file()])
    total = len(image_files)

    if total == 0:
        print("No images found.")
        return

    # Compute split indices
    # -> 80% train
    # -> 10% test
    # -> 10% val
    train_end = int(0.8 * total)
    test_end = int(0.9 * total)

    for i, img_file in enumerate(image_files):
        stem = img_file.stem

        # Find matching label (any extension)
        label_file = None
        for f in labels_src.glob(stem + ".*"):
            if f.is_file():
                label_file = f
                break

        # Decide split
        if i < train_end:
            split = "train"
        elif i < test_end:
            split = "test"
        else:
            split = "val"

        # Copy image
        dest_img = output_path / "images" / split / img_file.name
        shutil.copy2(img_file, dest_img)

        # Copy label if exists
        if label_file:
            dest_lbl = output_path / "labels" / split / label_file.name
            shutil.copy2(label_file, dest_lbl)
        else:
            print(f"No label found for {img_file.name}")

    print(f"Done. Copied {total} images.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="Path to dataset root")
    parser.add_argument("--output", default="candy_dataset")

    args = parser.parse_args()

    split_and_copy(args.input_path, args.output)
    create_data_yaml(args.input_path, args.output)