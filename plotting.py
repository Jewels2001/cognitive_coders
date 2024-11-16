import customtkinter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotWidget(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title='Data'):
        super().__init__(master)
        self.master = master
        self.title = title

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
    
    def plot(self, data):
        self.data = data
        ncolumns = len(data.columns)
        self.fig, self.ax = plt.subplots(ncols=ncolumns, figsize=(5*ncolumns, 5))
        for i, column in enumerate(data.columns):
            self.ax[i].plot(data[column])
            self.ax[i].set_title(column)
        plt.tight_layout()
        plt.grid()
        plt.show()