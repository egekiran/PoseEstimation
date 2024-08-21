import cv2
from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")  # importing the YOLOv8n model specified for pose detection.


def is_laying(keypoints):
    if len(keypoints) >= 13:
        shoulder_avg_y = (keypoints[5][1] + keypoints[6][1]) / 2
        hip_avg_y = (keypoints[11][1] + keypoints[12][1]) / 2

        threshold = 20
        if abs(shoulder_avg_y - hip_avg_y) < threshold:
            return True
    return False


def is_sitting(keypoints):
    if len(keypoints) >= 15:
        shoulder_avg_y = (keypoints[5][1] + keypoints[6][1]) / 2
        hip_avg_y = (keypoints[11][1] + keypoints[12][1]) / 2
        knee_avg_y = (keypoints[13][1] + keypoints[14][1]) / 2

        if shoulder_avg_y < hip_avg_y < knee_avg_y:
            return True
    return False


def is_walking(keypoints):
    if len(keypoints) >= 17:
        left_knee_x = keypoints[13][0]
        right_knee_x = keypoints[14][0]
        left_foot_x = keypoints[15][0]
        right_foot_x = keypoints[16][0]

        walking_threshold = 50
        if abs(left_knee_x - right_knee_x) > walking_threshold or abs(left_foot_x - right_foot_x) > walking_threshold:
            return True
    return False


def detect_pose(keypoints):
    if is_laying(keypoints):
        return "Laying"
    elif is_sitting(keypoints):
        return "Sitting"
    elif is_walking(keypoints):
        return "Walking"
    else:
        return "Unknown"


cap = cv2.VideoCapture("test.mp4")  # sample footage

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    for result in results:
        keypoints = result.keypoints.xy[0] if result.keypoints else []

        pose = detect_pose(keypoints)

        if result.boxes:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, pose, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Pose Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
