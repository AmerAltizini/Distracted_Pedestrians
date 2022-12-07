# Distracted Pedestrians Dataset

Template needs to be modified

### About Dataset
The Distracted Pedestrians Dataset, a Human Activity Recognition (HAR) dataset, includes an inertial sensor-embedded smartphone on 10 study subjects performing activities of daily living (ADL), distracting activities. The purpose is to classify the six performed activities.
### Description of experiment
Experiments were conducted with a group of 10 volunteers ranging in age from 19 to 31 years. Each subject performed six activities (WALK, WALK UP, WALK DOWN, SIT, STAND, LAY) while using a smartphone (MOTO G100). Using the built-in accelerometer and gyroscope, we captured 3-axis linear acceleration and her 3-axis angular velocity at her constant 50 Hz rate. The experiment was videotaped to manually label the data. The resulting dataset was randomly divided into two sets, with 70% of volunteers selected for training data generation and 30% for test data.

Sensor signals (accelerometer, gyroscope, magnetometer) were preprocessed by applying a noise filter and sampled in sliding windows of fixed width of 2.56 s and 50% overlap (128 readings/window). A filter with a cutoff frequency of 0.3 Hz was used because gravity is considered to have only low-frequency components. A feature vector was obtained from each window by computing the time-domain and frequency-domain variables.

### Attribute information
For each record in the dataset, the following is provided:

1. Triaxial acceleration from the accelerometer.
2. Triaxial Angular velocity from the gyroscope.
3. Triaxial magnetometer
4. Its activity label.
5. An identifier of the subject who experimented.


## Prove Data

The Jupyter Notebook "AnalysisData.ipynb" can be used to visualize the data.
It reads in the data of one participant and shows all physiological sensor data separately.
This offers the opportunity to prove whether the data was correctly measured or not.

### Preprocessing

In the preprocessing, the data will be prepared for machine learning afterwards.

**Order for Preprocessing**:
1. Preprocessing_robotlogs.ipynb
   1. Create a merged log-file containing all triggers (gestures and speech) and change the time format to [ms].
2. Preprocessing_time.ipynb
   1. Changes the time format for e4 data to be in [ms] and removes the offset between NTP-Server and Wristband.
   2. Defines the baseline measurements in tag files.
   3. Offers to calculate the robots' speech time.
3. Preprocessing_questionnaire.ipynb
   1. Prepares the questionnaires to be used for labelling the data. - only affect information is used.
4. Preprocessing_labelData.ipynb
   1. Merge the merged robot log files with the questionnaire information.
   2. Merge the tag files.
   3. Merge sensors data with the ground_truth.
   4. Convert all csv file encoding to utf-8.

! After preprocessing, all files contain timestamps in milliseconds!

### Statistics

Evaluating dataset based on the GARAFED method, can be done by modifying the parameters in the data variable inside GARAFFED Radar Viz.html using text editor, then annotating the parameters using the drawio file.

### Machine Learning