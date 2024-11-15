import numpy as np
import pandas as pd
import os


# Step 1a - input file path to data we want to generate

# Step 1b - input label of data we want to generate

# Step 2 - output data corresponding to label to file path

class fileGenerator:
    
    # Constructor
    def __init__(self):
        
        self.datasets = {
                    'Select a Label': pd.read_csv('experiment.csv'),
                    'Left fist': pd.read_csv('experiment.csv'), 
                    'Right fist': pd.read_csv('experiment.csv'),
                    'Both fists': pd.read_csv('experiment.csv'), 
                    'Left foot': pd.read_csv('experiment.csv'),
                    'Right foot': pd.read_csv('experiment.csv'),
                    'Both feet': pd.read_csv('experiment.csv'), }
        
    # Step 1a - Take GUI input to file path to data we want to generate
    def set_filepath(self, filepath):
        self.filepath = filepath
    # Step 1b - Take GUI input to label of data we want to generate
    def set_label(self, label):
        self.label = label
    # Step 2 - output data corresponding to label to file path
    def output_data(self):
        data_to_output = self.datasets[self.label]
        data_to_output.to_csv(self.filepath + '/output.csv')
        
    def generate_data(self, label, filepath):
        self.set_filepath(filepath)
        self.set_label(label)
        self.output_data()
        # open file explorer to show the user the file location
        os.startfile(filepath)
        # open the file
        os.startfile(filepath + '/output.csv')