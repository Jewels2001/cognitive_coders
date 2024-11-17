import numpy as np
import pandas as pd
import os

from model_processing import get_prediction



# Step 1a - input file path to data we want to generate

# Step 1b - input label of data we want to generate

# Step 2 - output data corresponding to label to file path

class fileGenerator:
    
    # Constructor
    def __init__(self):
        
        
        # example datasets for the different labels - final product will export datasets produced by ML model
        self.datasets = {}
        
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
        print(self.label)
        data_to_output = get_prediction(self.label)
        self._set_filename(filename)
        output_success = False
        output_attempts = 0
        while (output_success == False):
            try:
                data_to_output.to_csv(self.filepath + '/' + self.filename + '(' + str(output_attempts) + ')' + '.csv', mode='x')
                output_success = True
            except:
                output_attempts+=1
            print(output_attempts)
            if output_attempts == 10:
                print('Failed to generate data after 10 attempts.')
                return
            
        
    def generate_data(self, label, filepath, filename='file'):
        self._set_filepath(filepath)
        self._set_label(label)
        self._output_data(filename)
        
        # open file explorer to show the user the file location
        os.startfile(filepath)
        
    def getData(self):
        return self.datasets[self.label]