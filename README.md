# Race-Bias
Project to verify the racial bias in models (Vgg16, MobileNet, ResNet50) training with distincts databases (Fair Face, VggFace2, UTKFace)

## Dependencies
* python 3.10.12
* numpy 1.26.3
* tensorflow 2.15.0
* scikit-learn 1.4.0
* keras 2.15.0
  
## Data
The Data is available through the websites: 
* VMER - https://mivia.unisa.it/ethnicity-recognition-dataset/; 
* Fair Face - https://paperswithcode.com/dataset/fairface;
* UTKFace - https://susanqq.github.io/UTKFace/

## Obs
The Directorys:
* confusion_matrix
* Dataset_Fair_Face - Where's train fair face dataset
* Dataset_Fair_Face_test - Where's test fair face dataset for UTKFace trained models
* Dataset_Fair_Face_test_2 - Where's test fair face dataset for fair face trained models
* Dataset_Fair_Face_test_3 - Where's test fair face dataset for VMER trained models
* Dataset_VggFace2 -  Where's train VMER dataset
* UTKFace - Where's train UTKFace dataset
* models - Where's the save models
* confusion_matrix - Where's the confusion matrices

They must being created for the good use of the code
