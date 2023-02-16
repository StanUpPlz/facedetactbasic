import cv2

# Load the face cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the camera
cap = cv2.VideoCapture(0)

counter = 0

# Loop through frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('v'):
        face_roi = frame[y:y+h, x:x+w]
        cv2.imwrite('image'+str({counter})+'.jpg', face_roi)
        counter += 1

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
