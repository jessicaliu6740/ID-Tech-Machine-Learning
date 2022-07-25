# ID Tech Artificial Intelligence with NVIDIA Final Project
My project uses a retrained model and detectnet to detect faces within the view of a camera and block them out. <br />
![unnamed](https://user-images.githubusercontent.com/108949718/180885312-a1f92f94-042d-4141-80e9-acdef5307052.jpg) <br />
The idea behind this project is that it could help vloggers or other people on the internet that want to protect some of their privacy. <br />
Video introduction: https://drive.google.com/file/d/17yM0tAicQo-G549Q4o2dq61WvYV-NwLu/view?usp=sharing

## The Algorithm
The first two lines are there to import the needed modules for the code. <br />
![image](https://user-images.githubusercontent.com/108949718/180879736-c89528cf-50bb-46d5-aa38-215c10f579ea.png) <br />
<br />
The next few lines are for the initialization of the model, camera, and display. 
The first line loads the object detection model, which in this case is located in the models/face2 directory.
The next line connects to the camera device, V4L2 in this case, and creates an instance of the videoSource object.
The last line creates a video output interface using the videoOutput object. <br />
![image](https://user-images.githubusercontent.com/108949718/180879359-bcda7913-26b4-4b99-a8dd-6a04cc847a13.png) <br />
<br />
A while loop is created that will run until the users exits. <br />
![image](https://user-images.githubusercontent.com/108949718/180880517-cfd627d4-e333-4bc7-8841-313a80f41f2b.png) <br />
The next line captures the video frame and waits until the next one loads into the GPU memory. <br />
![image](https://user-images.githubusercontent.com/108949718/180880824-7157b0e2-08a1-4aaf-972d-fff0b6eb0fba.png) <br />
The line after that takes in the frame from the previous line and returns a list with all the detections found. <br />
![image](https://user-images.githubusercontent.com/108949718/180881006-03239d54-cf81-41fe-b67f-a04578112035.png) <br />
<br />
A for loop is then used to iterate through each detection found in the frame. <br />
![image](https://user-images.githubusercontent.com/108949718/180881142-9e6ab4fb-24a3-427f-b1a1-75eb82b1e649.png) <br />
Within the for loop is a nested for loop that iterates through each y-coordinate between the top and bottom of the bounding box, as well as each x-coordinate between the left and right of the bounding box. <br />
![image](https://user-images.githubusercontent.com/108949718/180881321-7675a584-5809-41ef-9df8-d1b7f977fc9d.png) <br />
From there, each pixel that is looped through gets converted to black or (0, 0, 0) in rgb values. <br />
![image](https://user-images.githubusercontent.com/108949718/180881450-df5cd389-45b6-4bde-85ea-f61f2f939b92.png) <br />
<br />
Finally, the image is rendered and visualized with OpenGL. The title of the window is updated to display the current performance. <br />
![image](https://user-images.githubusercontent.com/108949718/180881865-f3e0803a-5e1d-4f52-a442-c8c6e7a89ee3.png) <br />
<br />

## Running This Project
To run this project, you need a jetson nano as well as a V4L2 camera. Make sure you have SSD-Mobilenet-v2 and python3 installed. 
Also make sure that you're connected to a monitor, otherwise the display will no show up. 
After that just run the following command in the directory with 'face.py' and the 'models' directory and it will run the script: <br />
![image](https://user-images.githubusercontent.com/108949718/180883311-c7b5fd43-f1d6-4f05-905c-91bdcf48ac4d.png) <br />
***If it's the first time running, it will take a little while before starting.***
