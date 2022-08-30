# Lane Detection

Driver support technology reduces the workload on the driver which includes intelligent or adaptive cruise control, lane-keeping assists, and hands-free capability. An autonomous car is a vehicle capable of sensing its environment and operating without human involvement.

The primary objective of this project is to perform camera based lane detection. Draw a comparitive study between traditional vision feature based method and deep learning-based method. And finally, highlight the differences and similarities between these implementations.

## Computer Vision approach

Tools and libraries: Python programming language, open-cv

The video is processed frame by frame as images, and a series of operations are carried out on each frame to identify the lanes in that frame.

Steps to identify the lanes include:

1. Canny edge detection

2. Masking the image not inside region of interest

3. Identifying all the lines inside the ROI using Hough transform

4. Averaging the lines to identify the left and right line

5. Displaying the lines on the frame

## Deep Learning approach

Tools and libraries: Python programming language, open-cv, Keras, matplotlib, numpy

A pre-trained CNN model has been used to make the lane markings on the image/video. The pre-trained model has the following layers:

1. Conv2D

2. MaxPooling2D

3. Conv2DTranspose

4. UpSampling2D

5. Dropout

An image is used as the input to the model. In case we want the lane markings to be made on a video, we divide the video into individual frames and pass each frame as the input to the model.

The following are the steps:

1. Take in the image of a road

2. Re-size the image to the size required by the model

3. Predict the lane to be drawn from the model in green color

4. Recreate an RGB image of a lane

5. Merge with the original road image

These steps are carried out for each incoming frame to detect lanes in a video.

<img width="360" alt="image" src="https://user-images.githubusercontent.com/38185827/187557763-9f4acf38-8bc0-46f7-bec1-aa7df3092393.png">

 

