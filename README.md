# Social-distancing-tracker

It is a python script enabling user to ensure social distancing from a video input. Here a pre-recorded video is given as an input and number of people in a frame and distance between them is calculated using Computer Vision and Digital Image Processing.

<br>The script given one of the best solution for video captured from a single camera, reducing the problem of capturing video from multiple perspective for 3D depth. It uses Digital Image processing to transform the given perspective video feed to 2D for better tracking.

<br>A ROI (Region Of Interest) is to be selected where we want to check social distancing is maintained or not. This script is currently taking a pre-recorded video as input but we can tweak the code to make it work with live camera feed of a device.

## How to run the project

1. Clone the repo into your local system.
2. Run the main.py file, 2 basic input videos are provided with the files in the "data" folder but you can change the input video by placing desired video file in "data" folder and changing the video file name in main.py
3. After running you will see the first frame in the video in which you will be prompted to select seven points.
4. First 4 will be denoting the Region of Interest and the remaining three would be denoting the mapping of 6 feet horizontal and vertical distance.
5. Then the detection would be performed on the input video file.
