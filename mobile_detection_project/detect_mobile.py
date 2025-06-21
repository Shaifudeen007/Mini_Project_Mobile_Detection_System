# Import necessary libraries
import cv2
from ultralytics import YOLO
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Email Alert Function
def send_alert_email(timestamp, image_path):
    sender_email = "shaifshaif144@gmail.com"
    receiver_email = "shaifudeen55@gmail.com"
    password = "tkew qjpv unmw kqjj"  # Replace with actual Gmail App Password

    subject = "🚨 Mobile Phone Detected!"
    body = f"A mobile phone was detected on {timestamp}.\nCheck the attached image for reference."

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    # Attach the image
    with open(image_path, 'rb') as f:
        img_data = f.read()
        msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename=image_path)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        print("[EMAIL] Alert email sent successfully!")
    except Exception as e:
        print("[EMAIL ERROR]", e)

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Start video capture
cap = cv2.VideoCapture(0)

class_names = model.names
mobile_detected = False

print("[INFO] Starting video stream...")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("[ERROR] Failed to grab frame.")
        break

    results = model(frame, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = class_names[cls_id]

            if label == "cell phone":
                mobile_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                # Log detection with timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[ALERT] Mobile Phone Detected at {timestamp}")

                # Save the frame
                image_path = f"detected_{timestamp.replace(':', '-')}.jpg"
                cv2.imwrite(image_path, frame)

                # Send Email Alert
                send_alert_email(timestamp, image_path)

                break  # Exit detection loop after one detection

    cv2.imshow("Mobile Detection", frame)

    if mobile_detected:
        print("[INFO] Ending detection after phone found.")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
