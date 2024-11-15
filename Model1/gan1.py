# !pip install tensorflow

import tensorflow as tf
import pandas as pd

import random

import glob
# import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from tensorflow.keras import layers
import time

#from IPython import display


"""
Adds fake labels to the Muse S data set from 
https://www.kaggle.com/datasets/muhammadatefelkaffas/eeg-muse2-motor-imagery-brain-electrical-activity?resource=download
"""


df = pd.read_csv("./data/museMonitor_2024-06-02--09-47-17_5812437961079996628.csv")

print(df.head())

fake_labels = ["left_leg", "left_arm", "right_leg", "right_arm"]

# np.random.randint(1, 6, df1.shape[0])

# gender_series = df.gender.apply(lambda x: random.choice(['male', 'female']) ) 

df['labels'] = ""
df['labels'] = df['labels'].apply(lambda x: random.choice(fake_labels))

print(df.head())

print(df['labels'].value_counts(dropna=False))

df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='ISO8601')


df.drop(['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10',
       'Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10', 'Alpha_TP9',
       'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10', 'Beta_TP9', 'Beta_AF7',
       'Beta_AF8', 'Beta_TP10', 'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8',
       'Gamma_TP10','AUX_RIGHT',
       'Mellow', 'Concentration', 'Accelerometer_X', 'Accelerometer_Y',
       'Accelerometer_Z', 'Gyro_X', 'Gyro_Y', 'Gyro_Z', 'HeadBandOn',
       'HSI_TP9', 'HSI_AF7', 'HSI_AF8', 'HSI_TP10', 'Battery', 'Elements'], axis=1, inplace=True)

#grouped_secs = df.groupby(pd.Grouper(key='TimeStamp', axis=0,freq='min'))
#df.groupby(pd.Grouper(key='TimeStamp', axis=0,freq='min')).mean(numeric_only=True)

# df.groupby([pd.Grouper(key='TimeStamp', axis=0,freq='min'), 'labels']).mean(numeric_only=True).reset_index()

grouped_secs = df.groupby([pd.Grouper(key='TimeStamp', axis=0,freq='min'), 'labels']).mean(numeric_only=True).reset_index()

print(df['TimeStamp'].value_counts())




"""
Columns: 'TimeStamp', 'Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10',
       'Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10', 'Alpha_TP9',
       'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10', 'Beta_TP9', 'Beta_AF7',
       'Beta_AF8', 'Beta_TP10', 'Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8',
       'Gamma_TP10', 'RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10', 'AUX_RIGHT',
       'Mellow', 'Concentration', 'Accelerometer_X', 'Accelerometer_Y',
       'Accelerometer_Z', 'Gyro_X', 'Gyro_Y', 'Gyro_Z', 'HeadBandOn',
       'HSI_TP9', 'HSI_AF7', 'HSI_AF8', 'HSI_TP10', 'Battery', 'Elements',
       'labels'],
"""


### Currently treating each RAW location a dimension (ie, 4 dimensions)
# using: 'RAW_TP9', 'RAW_AF7', 'RAW_AF8', 'RAW_TP10'


"""
GAN:
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(, y, test_size=0.20, random_state=6)



def make_generator():
    model = tf.keras.Sequential()
    model.add(layers.Dense(4))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    
    model.add(layers.Conv1D)