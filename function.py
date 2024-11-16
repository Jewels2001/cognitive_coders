import tkinter
import tkinter.messagebox
import customtkinter
import os


def change_appearance_mode_event(app, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


def change_scaling_event(app, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


def sidebar_button_event(app):
    print("sidebar_button click")


def set_filename(app, filename):
    filename = os.path.basename(filename)
    app.filename = filename
    app.file_name_display.configure(text=filename)


def pick_file(app):
    file = customtkinter.filedialog.askopenfilename(filetypes=app.filetypes)
    if file:
        set_filename(app, file)


# call this method as an input to any methods that require a file path for input
def get_filename(app):
    return app.filename


def getSelected(app):
    return app.options.get()
