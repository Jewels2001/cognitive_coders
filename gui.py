import customtkinter
import widgets

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Cognitive Coders")
        
        # Default message for label selection menu
        self.defmessage = 'Select a Label'
        # Labels for the selection menu
        self.labels = ['Happy', 'Sad', 'Neutral', 'Angry']

        # Label Selection Menu
        self.labels_menu = widgets.SelectionMenu(self, title='Label', options=self.labels, default_message=self.defmessage)
        self.labels_menu.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nw')
        
        # Choose destination file path
        self.file_picker = widgets.FilePickerButton(self, title='Select File')
        self.file_picker.grid(row=1, column=0, padx=10, pady=(10,0), sticky='nw')
        
        # Submit button
        self.button = customtkinter.CTkButton(self, text="Generate Data", command=self.printOption)
        self.button.grid(row=0, column=1, padx=10, pady=20, sticky='nw')
    
    # Change this method to do whatever the submit button does - currently prints selected label
    def printOption(self):
        print(self.labels_menu.getSelected())

app = App()
app.mainloop()