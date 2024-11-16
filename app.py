import customtkinter
import widgets
import backend

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.file_generator = backend.fileGenerator()
        self.geometry("400x400")
        self.title("Cognitive Coders")
        
        # Default message for label selection menu
        self.defmessage = 'Select a Label'
        # Labels for the selection menu
        self.labels = ['Left fist', 'Right fist', "Both fists", 'Left foot', 'Right Foot', 'Both Feet']

        # Label Selection Menu
        self.labels_menu = widgets.SelectionMenu(self, title='Label', options=self.labels, default_message=self.defmessage)
        self.labels_menu.grid(row=1, column=0, padx=10, pady=(10,0), sticky='nw')
        
        # Choose destination file path
        self.file_picker = widgets.FilePickerButton(self, title='Destination Folder')
        self.file_picker.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nw')
        
        #text entry
        self.text_entry = widgets.TextEntry(self)
        self.text_entry.grid(row=0, column=1, padx=10, pady=(10,0), sticky='nw')
        
        # Submit button
        self.button = customtkinter.CTkButton(self, text="Generate Data", command=lambda: self.file_generator.generate_data(self.labels_menu.getSelected(), self.file_picker.get_filename(), self.text_entry.get()))
        self.button.grid(row=2, column=0, padx=10, pady=20, sticky='nw')
        

        