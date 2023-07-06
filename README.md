
<body>
  <h1>Class Guardian</h1>

  <p>Class Guardian is a Python program developed using tkinter, face_recognition, and cv2 libraries. It enables the automatic capture of student attendance using a camera.</p>

  <h2>Features</h2>
  <ul>
    <li>Automatic student attendance capture using facial recognition</li>
    <li>Real-time camera feed with face detection</li>
    <li>Simple and intuitive user interface</li>
    <li>Works in Anaconda environment</li>
  </ul>
<h2>Output</h2>h2>
<img width="959" alt="image" src="https://github.com/uditsah098/class-guardian/assets/133565971/7e048795-8083-4b10-9c8d-87000e5eee55">
<img width="959" alt="image" src="https://github.com/uditsah098/class-guardian/assets/133565971/22c05bdb-cf75-416d-aeda-234e4173ee17">
<img width="959" alt="image" src="https://github.com/uditsah098/class-guardian/assets/133565971/115ae9f9-71e0-4508-be0e-6f1566a2d907">
<img width="959" alt="image" src="https://github.com/uditsah098/class-guardian/assets/133565971/0a1bfc7f-a958-4913-8eb2-eda712961e9d">
  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Anaconda environment</li>
    <li>tkinter library</li>
    <li>face_recognition library</li>
    <li>cv2 library</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository or download the source code.</li>
    <li>Create a new Anaconda environment:</li>
  </ol>
  <pre><code>conda create --name class-guardian python=3.x</code></pre>
  <ol start="3">
    <li>Activate the Anaconda environment:</li>
  </ol>
  <pre><code>conda activate class-guardian</code></pre>
  <ol start="4">
    <li>Install the required libraries:</li>
  </ol>
  <pre><code>pip install tkinter face_recognition opencv-python</code></pre>

  <h2>Usage</h2>
  <ol>
    <li>Make sure your camera is properly connected to your system.</li>
    <li>Open a terminal or command prompt and navigate to the project directory.</li>
    <li>Activate the Anaconda environment:</li>
  </ol>
  <pre><code>conda activate class-guardian</code></pre>
  <ol start="4">
    <li>Run the program:</li>
  </ol>
  <pre><code>python class_guardian.py</code></pre>
  <ol start="5">
    <li>The Class Guardian application will open.</li>
    <li>Adjust the camera settings, if necessary.</li>
    <li>Click on the "Start Attendance" button to begin capturing student attendance.</li>
    <li>The program will detect faces and match them with registered students.</li>
    <li>The attendance will be recorded and stored in a file.</li>
  </ol>

  <h2>Customization</h2>
  <ul>
    <li>You can customize the program by modifying the settings and appearance in the <code>class_guardian.py</code> file.</li>
    <li>Add student images and details to the <code>students</code> directory to register them for attendance.</li>
  </ul>

  <h2>License</h2>
  <p><a href="LICENSE">MIT License</a></p>

  <h2>Contributing</h2>
  <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>The program utilizes the face_recognition and cv2 libraries for facial recognition and image processing.</li>
  </ul>

