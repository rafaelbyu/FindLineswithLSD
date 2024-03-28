import cv2
import numpy as np

src = ""

video = cv2.VideoCapture(src)

lsd = cv2.createLineSegmentDetector()

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    scale_percent = 50  # )percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lines, _, _, _ = lsd.detect(gray)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.flatten()
            x1 = int(x1)
            x2 = int(x2)
            y2 = int(y2)
            y1 = int(y1)
            c1 = (x1, y1)
            c2 = (x2, y2)
            print(x1, y1, x2, y2)
            cv2.line(frame, c1, c2, (0, 255, 0), 2)
            cv2.imshow('Lines Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
