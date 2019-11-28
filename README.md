# Bayes_Classifier_Face_Detection
In this Repo. I implement a baysian classifier to detect face in different picture. it was implemented in different section; The description that each part is implemented for will follow .    

Face Detection Problem: How Does Bayesian Decision Theory Handle It?    
Keywords: Classification Problem, Bayes Decision Rule, Confusion Matrix, Bayes Error, ROC Curve, Face Detection, RG Chromaticity  

So far you’ve probably got familiar enough with Bayesian Decision Theory to know what to expect from it. If the decision problem is posed in probabilistic terms and all relevant probability values are known, BDT allows to take optimal decisions that minimise errors by choosing the least risky class.Although in many practical classification problems, these conditions are not fulfilled and therefore BDT won’t be effective, there are still some applications where it may come in handy.
Face Detection (not to be mistaken with Face Recognition) is the process of identifying and locating human faces in digital images and videos. It is often the first step in many face-related machine vision applications such as face recognition, emotion detection, gender detection, etc. Now we are going to find out how BDT deals with this problem in practice.
You are given a customised dataset divided into ‘Train’ and ‘Test’ folders at ‘P7’ directory. The train set consists of 50 face images alongside the corresponding face masks in a separate folder. These masks indicate face pixels with black (or gray-level 0) and non-face pixels with white (or gray-level255).  
a. First assume images in the ‘Train’ directory. Considering two classes for each pixel, ‘face’ and ‘non-face’, use the provided masks to find the class priors.  
b. We want to model the class-conditional probability density of each class using a univariate Gaussian. Find the mean and variance of both class-conditional densities.  
c. Apply your classifier on the images provided in the ‘Test’ directory and display the results.Also report the test error using the given masks.  
d. Compute a confusion matrix for your classifier.  
e. Calculate the Bayes error.  
f. Draw a ROC curve to visualise the performance of your classifier.  
