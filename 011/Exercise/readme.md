# What is haar cascade
Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier. Positive images – These images contain the images which we want our classifier to identify. Negative Images – Images of everything else, which do not contain the object we want to detect.
 It is an Object Detection Algorithm used to identify faces in an image or a real time video. The algorithm uses edge or line detection features proposed by Viola and Jones in their research paper “Rapid Object Detection using a Boosted Cascade of Simple Features” published in 2001. The algorithm is given a lot of positive images consisting of faces, and a lot of negative images not consisting of any face to train on them. The model created from this training is available at the OpenCV GitHub repository https://github.com/opencv/opencv/tree/master/data/haarcascades.
The repository has the models stored in XML files, and can be read with the OpenCV methods. These include models for face detection, eye detection, upper body and lower body detection, license plate detection etc.

# Exercise goal
* The goal of this algorithm is to detect the face using OpenCV and Haarcascade


# Data
 * Any simple image to detect the face using opencv
OpenCV comes with these pre-trained cascade files(https://github.com/opencv/opencv/tree/master/data/haarcascades)

# Task
* Import the required libraries
* Import the pretrained haarcascade
* script to detect the faces
