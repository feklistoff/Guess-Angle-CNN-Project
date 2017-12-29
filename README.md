# Guess-Angle-CNN Project

## Overview
---
This is a test project where I train, validate and test a model using CNN. 

The model takes a plain white picture with draw rectangles that is randomly rotated between -10 and 10 degrees and predicts an angle of picture rotation.

**Goals of this Project:**

* Develop a pipeline for generating dataset of 11000 training pictures:
  * size of the picture 128x128
  * each picture contains one to five random rectangles
  * width/height of each rectangle is between 0.1 and 1 of width/height of the picture
  * the center point of rectangle is randomly chosen from 128x128 area
  * after drawing rectangles the picture itself is randomly rotated between -10 and 10 degrees
* Write a network in TensorFlow that predicts picture's rotation angle
* Write a function that uses the output of the network to rotate given picture back
* Visualize the result

## Files:
* `model_b.h5` - Saved model
* `dataset_generator.ipynb` - Notebook used to create the dataset
* `model_notebook.ipynb` - Notebook visualizing building steps and data preprocessing pipeline

## Dependencies
This project requires:

[CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The project enviroment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

or Python 3.5 and the following libraries installed:

* [Jupyter](http://jupyter.org/)
* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)
* [scikit-learn](http://scikit-learn.org/)
* [OpenCV](http://opencv.org/)
* [TensorFlow](http://tensorflow.org)
* [Keras](https://keras.io/)
