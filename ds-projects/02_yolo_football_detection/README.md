# 🎯 Football Video Object Detection with YOLO

Running a YOLO object detector over a football (soccer) match video, frame by frame,
and saving a new video with bounding boxes drawn around players, the ball and other objects.

📓 Notebook: [`yolo_football_detection.ipynb`](yolo_football_detection.ipynb)

## What's inside

- **`FootballDetector` class** — wraps an [Ultralytics](https://docs.ultralytics.com/) YOLO model
- **`process_video()`**:
  1. reads the input video with OpenCV and copies its width, height and FPS
  2. runs YOLO detection on every frame
  3. draws the predicted boxes and labels (`results[0].plot()`)
  4. stamps a frame counter in the corner
  5. writes everything to an `.mp4` file, printing progress every 30 frames
- Run on a ~2,000-frame match clip using the pretrained **`yolo12n.pt`** (YOLOv12 nano) weights

## Tech stack
`ultralytics` (YOLO) · `opencv-python` · `numpy` · Google Colab

## How to run
```bash
pip install ultralytics
```
Put your video next to the notebook as `ds.mp4` (or change the path in the last lines),
then run the cells. The result is saved as `detected_output.mp4`.
Model weights are downloaded automatically on first use.

## Next steps
- Fine-tune YOLO on a labelled football dataset (players / goalkeepers / referees / ball)
- Add object tracking (e.g. ByteTrack) to follow players across frames
