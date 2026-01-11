# Symbols-Classifier
For ABU Robocon 2026

Problem statement


For the ABU Robocon 2026, we need a code that will identify the input of the camera and classify it into three: Robocon logo, Oracle bone symbols and Random or Fake symbols. To do this, I have utilised CNN.


Project report


**NONE OF THE CODE SUBMITTED HERE IS AI GENERATED**


I have used tensorflow, keras, mobilenet, numpy, skimage, onnx, onnxruntime, opencv, matplotlib, torch, yolo and os packages in this journey. In my first attempt, I wrote a code using opencv and tensorflow, keras and mobilenet. My searches on the internet told me that mobilenet was the lightest CNN and thus would be a good choice for this project. In this try, the training and deployment was happening in the same code file. I converted all the images to grayscale so that output was good, toggled with the model specs and updated the data files mutliple times to impove predictions. The accuracy is good for robocon logo and oracle bone symbols. No model was being exported and loaded. 
Since my initial attempt was working successfully, I tried to improve the model further. I explored torchvision but decided to stick to mobilenet in the end. I improved my understanding of image classification and object detection and tried to understand how a CNN works. I explored using a more custom model intead of Imagenet. I also tried to train and predict in different code files by saving the model. My model was in keras and then was converted into onnx. The keras model saved 1000 classes since my I modified ImageNet to give predictions. Keras model does not have the capability to save the class indices while saving the model. They have to be saved separately and referred in the inference script. Another problem was that my onnx model was not running with my inference script.
Since I didnt want to use AI, I read the docs of mobilenet, keras, torchvision, tensorflow and onnx and information given by google and microsoft, several blogs, searched stack overflow and reddit, searched in ML for dummies and Deep Learning (Goodfellow), watched videos on opencv and image classification. I found that onnx doesnt support .predict() function and needs a different inference script as compared to the keras model. Also, saving the classes in a separate file for the keras model and then using it to only get one of three outputs is an option. However, I am unsure of how that will translate in the onnx model. 

The final submitted code is the amalgamtion of all my attempts.


Things to work on


try data augmentation
try to give less robocon images and make it decide more between real and fake symbols
improve accuracy of classification of fake symbols.
try image processing to boost output
try to make it work with onnx and keras saved models
give confidence score


To deploy


Create a folder
Download the zip file containing the data on which the model is trained in that folder. Extract the data.
Download the code in the same folder
Download tensorflow, opencv, numpy, skimage, keras
Run the code

It's that simple.

I am also attaching the inference script that should work with an onnx model which i will use once i have figured out the issues. The keras model and the onnx model are also uploaded
