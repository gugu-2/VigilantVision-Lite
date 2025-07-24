import cv2
from face_detector import FaceDetector
from threat_detector import ThreatDetector

def main():
    face_detector = FaceDetector('models/haarcascade_frontalface_default.xml')
    threat_detector = ThreatDetector('models/yolov5s.pt')

    cap = cv2.VideoCapture(0)  # 0 for webcam; replace with video file path if needed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_detector.detect(frame)
        threats = threat_detector.detect(frame)

        # Draw face detections
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Draw threat detections
        for *box, conf, cls in threats:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"{cls} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('VigilantVision', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()