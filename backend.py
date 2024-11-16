import numpy as np
import pandas as pd
import os


# Step 1a - input file path to data we want to generate

# Step 1b - input label of data we want to generate

# Step 2 - output data corresponding to label to file path

class fileGenerator:
    
    # Constructor
    def __init__(self):
        
        
        # example datasets for the different labels - final product will export datasets produced by ML model
        self.datasets = {
                    'Select a Label': pd.read_csv('experiment.csv'),
                    'Left fist': pd.read_csv('experiment.csv'), 
                    'Right fist': pd.read_csv('experiment.csv'),
                    'Both fists': pd.read_csv('experiment.csv'), 
                    'Left foot': pd.read_csv('experiment.csv'),
                    'Right foot': pd.read_csv('experiment.csv'),
                    'Both feet': pd.read_csv('experiment.csv'), }
        
    # Step 1a - Take GUI input to file path to data we want to generate
    def _set_filepath(self, filepath):
        self.filepath = filepath
    # Step 1b - Take GUI input to label of data we want to generate
    def _set_label(self, label):
        self.label = label
    #step1c- Take GUI input to the name of the file we want to generate
    def _set_filename(self, filename):
        self.filename = filename
    # Step 2 - output data corresponding to label to file path
    def _output_data(self, filename):
        data_to_output = self.datasets[self.label]
        self._set_filename(filename)
        data_to_output.to_csv(self.filepath + '/' + self.filename + '.csv')
        
    def generate_data(self, label, filepath, filename):
        self._set_filepath(filepath)
        self._set_label(label)
        self._output_data(filename)
        
        # open file explorer to show the user the file location
        os.startfile(filepath)
        
    def getData(self):
        return self.datasets[self.label]