# YOLO5 train on custom dataset (Object detection)

UNDER CONSTRUCTION

**This has been created as a repo for students to show abaility of [YOLO](https://www.v7labs.com/blog/yolo-object-detection)**

1. Data have been labeled in [Label Studio](https://labelstud.io/)
   - recommendations 1000-2000 examples for every class
   - to save training time I used just ~50 images for 3 classes (recognition of Bosch logo, DIGI@JhP logo and eyes detection)
   - I used YOLO5 nano model which has 3.7 MB and 1.7 mio parameters
2. After finishing, data export in YOLO format is needed for next step
3. Training and evaluation of model
4. Testing in Python w/ OpenCV
   
![demo](/image/demo.jpg)

---
Credit goes to [Ultralytics](https://github.com/ultralytics/yolov5)
