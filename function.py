import tkinter
import tkinter.messagebox
import customtkinter
import os
import backend


def change_appearance_mode_event(app, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(app, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


def sidebar_button_event(app):
    # Placeholder event for sidebar buttons
    print("sidebar_button click")


def set_filename(app, filename):
    filename = os.path.basename(filename)
    app.filename = filename
    app.file_name_display.configure(text=filename)
    
def set_folder(app, folder):
    folder = os.path.abspath(folder)
    print(folder)
    app.folder = folder
    app.file_name_display.configure(text=folder)

def set_label(app, label):
    app.label = label

def get_label(app):
    return app.label

def set_data(app, label):
    fileGenerator = backend.fileGenerator()
    try:
        app.data = fileGenerator.datasets[label]
    except KeyError:
        app.data = None
        print("Label not found in datasets")

def pick_file(app):
    file = customtkinter.filedialog.askopenfilename(filetypes=app.filetypes)
    if file:
        set_filename(app, file)
        
def pick_folder(app):
    file = customtkinter.filedialog.askdirectory()
    if file:
        set_folder(app, file)
        print(file) # For debugging

# call this method as an input to any methods that require a file path for input
def get_filename(app):
    return app.filename

def get_folder(app):
    try:
        return app.folder
    except:
        print("No folder selected")

def download(self, label, filepath, filename):
    print(filepath)
    fileGenerator = backend.fileGenerator()
    fileGenerator.generate_data(label, filepath, filename)

def getSelected(app):
    return app.options.get()
