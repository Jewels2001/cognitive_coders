import pickle
from keras.src import tree
import numpy as np
import pandas as pd
import random


with open('conditional_generator_model.pkl', 'rb') as file:
    loaded_generator = pickle.load(file)
    # print("Loaded Generator data type: ", type(loaded_generator))

# with open('conditional_discriminator_model.pkl', 'rb') as file:
#     loaded_discriminator = pickle.load(file)
#     print("Loaded Discriminator data type: ", type(loaded_discriminator))

# with open('conditional_gan_model.pkl', 'rb') as file:
#     loaded_gan = pickle.load(file)
#     print("Loaded GAN data type: ", type(loaded_gan))


def _generate_noise_with_outliers(shape, outlier_probability=0.1, outlier_magnitude=20):
    """Generates multidimensional random noise with a Gaussian distribution and outliers.

    Args:
        shape: The shape of the noise array (e.g., (100, 5) for 100 samples with 5 features).
        outlier_probability: The probability of a data point being an outlier.
        outlier_magnitude: The magnitude of the outliers (how far they deviate from the normal distribution).

    Returns:
        A NumPy array with the generated noise.
    """
    mean = random.randint(500, 800)

    noise = np.random.normal(mean, 10, shape)  # Generate Gaussian noise
    outlier_mask = np.random.rand(*shape) < outlier_probability  # Randomly select outliers

    # Introduce outliers by scaling the selected values by the magnitude
    noise[outlier_mask] = noise[outlier_mask] + (noise[outlier_mask] - mean) * outlier_magnitude

    return noise

encoding = {'RightHandOpenClosePhysically' : [1, 0, 0],'RightHandOpenCloseImagine' : [0, 1, 0],'CupPickupImagine' : [0, 0, 1],}

def get_prediction(label):
    noise = _generate_noise_with_outliers((1, 2))
    label = encoding[label]
    prediction = pd.DataFrame(loaded_generator.predict([noise, label]))