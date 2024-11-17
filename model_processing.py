import pickle
from keras.src import tree
import numpy as np
import pandas as pd
import random

with open('conditional_generator_model.pkl', 'rb') as file:
    loaded_generator = pickle.load(file)

with open('conditional_generator_model_32features.pkl', 'rb') as file:
    loaded_generator_32 = pickle.load(file)
    
def _generate_noise_with_outliers(shape, mean, outlier_probability=0.1, outlier_magnitude=20):
    """Generates multidimensional random noise with a Gaussian distribution and outliers.

    Args:
        shape: The shape of the noise array (e.g., (100, 5) for 100 samples with 5 features).
        mean: The mean value of the Gaussian noise.
        outlier_probability: The probability of a data point being an outlier.
        outlier_magnitude: The magnitude of the outliers (how far they deviate from the normal distribution).

    Returns:
        A NumPy array with the generated noise.
    """
    
    noise = np.random.normal(mean, 10, shape)  # Generate Gaussian noise
    outlier_mask = np.random.rand(*shape) < outlier_probability  # Randomly select outliers

    # Introduce outliers by scaling the selected values by the magnitude
    noise[outlier_mask] = noise[outlier_mask] + (noise[outlier_mask] - mean) * outlier_magnitude

    return noise

encoding = {'RightHandOpenClosePhysically' : [1, 0, 0],
            'RightHandOpenCloseImagine' : [0, 1, 0], 
            'CupPickupImagine' : [0, 0, 1],
            'GraspAndLift' : [1] }

four_col_encoding = ['TP9','AF7','AF8','TP10']
third_feat_encoding = ['Fp1','Fp2', 'F7', 'F3','Fz','F4','F8','FC5','FC1','FC2',
                       'FC6','T7','C3','Cz','C4','T8', 'TP9','CP5','CP1','CP2',
                       'CP6','TP10','P7','P3','Pz','P4','P8','PO9','O1','Oz','O2','PO10']

def get_prediction(txtlabel):
    # Get lable encoding 
    label = np.array(encoding[txtlabel]).reshape(1,-1)
    
    if txtlabel == 'GraspAndLift': # if its 32 features 
        mean = random.randint(-200, 200)
        noise = _generate_noise_with_outliers((1, 10), mean)
        prediction = pd.DataFrame(loaded_generator_32.predict([noise, label]).squeeze(), columns = third_feat_encoding)
    else: # if dataset is not the 32 features model
        mean = random.randint(500, 800)
        noise = _generate_noise_with_outliers((1, 2), mean)
        prediction = pd.DataFrame(loaded_generator.predict([noise, label]).squeeze(), columns = four_col_encoding)
        
    return prediction

if __name__ == '__main__':
    # Testing the function
    label = 'GraspAndLift'
    prediction = get_prediction(label)
    print(prediction)