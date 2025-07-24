import torch

class ThreatDetector:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = results.xyxy[0].numpy()  # [x1, y1, x2, y2, conf, cls]
        return detections