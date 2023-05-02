from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.shortcuts import render, redirect
import cv2
import os
from django.contrib import messages


# detect faces in a video and saves it .
def get_face_frame():

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('trained/haarcascade_frontalface_default.xml')

    # Initialize the filename increment to 0
    filename_increment = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # Draw a rectangle around each detected face
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            
            # Crop the face from the frame
            face = frame[y:y+h, x:x+w]
            
            # Construct the filename for the captured face
            filename = f"face_{filename_increment}.jpg"
            
            # Save the face as an image
            cv2.imwrite(os.path.join('media', filename), face)
            print(f"Face has being captured ({filename_increment})")
            
            # Increment the filename increment
            filename_increment += 1
        
        # Encode the frame as a JPEG image
        frame = cv2.resize(frame, (640, 480))
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

        if cv2.waitKey(1) == ord('q'):
            break

@gzip.gzip_page
def capture_face(request):
    return StreamingHttpResponse(get_face_frame(), content_type='multipart/x-mixed-replace; boundary=frame')
