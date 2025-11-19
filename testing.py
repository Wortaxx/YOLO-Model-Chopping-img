from ultralytics import YOLO
import cv2
from pathlib import Path



model = YOLO("model.pt")


INPUT_DIR  = Path("Raw") 
OUTPUT_DIR = Path("Post")   
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
VALID_EXTS = {".jpg", ".jpeg", ".png"}


for img_path in INPUT_DIR.glob("*"):
    if img_path.suffix.lower() not in VALID_EXTS:
        continue

    results = model(str(img_path))[0]
    img = cv2.imread(str(img_path))

    if len(results.boxes) == 0:
        continue

    biggest = max(results.boxes, key=lambda b: (b.xyxy[0][2] - b.xyxy[0][0]) * (b.xyxy[0][3] - b.xyxy[0][1]))
    x1, y1, x2, y2 = map(int, biggest.xyxy[0])

    cropped = img[y1:y2, x1:x2]

    out_path = OUTPUT_DIR / f"{img_path.stem}_crop.png"
    cv2.imwrite(str(out_path), cropped)
