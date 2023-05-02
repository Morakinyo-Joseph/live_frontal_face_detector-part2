<h1>Live Frontal Face Detector</h1>
<p>This is a real-time video stream that detects and captures faces using trained data</p>

<h2>How to Start</h2>

<ol>
  <li>
    Make sure your computer and phone are connected to the same network
  </li>

  <li>
    Clone this repo into your computer in terminal <em>"git clone https://github.com/Morakinyo-Joseph/live_frontal_face_detector.git"</em>
  </li>
  
   <li>
    Navigate to the cloned project directory in your terminal. 
  </li>
  
  <li>
    Run the requirements.txt file in terminal <em>"pip install -r requirements.txt"</em>
  </li>
  
  <li>
    With your Android phone, navigate to playstore and download "ip webcam"
  </li>
  
  <li>
    After installing, open the app and scroll down to "start server"
  </li>
  
  <li>
    Take note of the ip address and port number you see during the video stream. e.g "192.168.8.104.8080" 
  </li>
  
  <li>
    On your computer, run <em>"python manage.py runserver"</em>
  </li>
  
  <li>
    Once the runserver is successful, go to your browser and search for "127.0.0.1:8000"
  </li>

  <li>
    Input your ip address and port number and click start
  </li>

</ol>


<h3>Also note, any face captured will be saved in a folder named "media" in the root directory</h3>
