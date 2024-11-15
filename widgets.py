import customtkinter

class SelectionMenu(customtkinter.CTkFrame):
    def __init__(self, master,  title='Options', options=[], default_message='Please Select an option:'):
        super().__init__(master)

        self.values = options
        self.grid_columnconfigure(0, weight=1)
        
        # Set the title
        self.title=title        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="transparent", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")
        
        self.options = customtkinter.CTkOptionMenu(self, values=self.values)
        self.options.set(default_message)
        self.options.grid(row=1, column=0, padx=10, pady=(10,0), sticky='new')
        
    def getSelected(self):
        return self.options.get()

class FilePickerButton(customtkinter.CTkFrame):
    def __init__(self, master, title='Select File', filetypes=(('csv files', '*.csv'), ('Excel files', '*.xlsx'), ("all files", "*.*"))):
        super().__init__(master)
        
        self.filetypes = filetypes
        self.filename = "NO FILE SELECTED"
        
        self.button = customtkinter.CTkButton(self, text="Select File", command=self.pick_file)
        self.button.grid(row=1, column=0, padx=10, pady=(10,0), sticky='new')
        
        self.filenamedisplay = customtkinter.CTkLabel(self, text="FileName: " + self.get_filename(), fg_color="transparent")
        self.filenamedisplay.grid(row=2, column=0, padx=10, pady=(10,0), sticky='new')
        
    def pick_file(self):
        file = customtkinter.filedialog.askopenfilename(filetypes=self.filetypes)
        if file:
            self.filename=file
            self.filenamedisplay.configure(text="FileName: " + self.get_filename())
            

    def get_filename(self):
        return self.filename
    

class VerticalRadiobuttonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,  title='Radio Buttons', values=[],):
        super().__init__(master)

        self.values = values
        self.radiobuttons = []
        self.grid_columnconfigure(0, weight=1)
        self.variable = customtkinter.StringVar(value="")
        
        # Set the title
        self.title=title        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky='w')
            self.radiobuttons.append(radiobutton)
    def get(self):
        return self.variable.get()
            
class CheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,  title='Checkboxes', values=[],):
        super().__init__(master)

        self.values = values
        self.checkboxes = []
        self.grid_columnconfigure(0, weight=1)
        
        # Set the title
        self.title=title        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky='w')
            self.checkboxes.append(checkbox)
    def get(self):
        return [checkbox.get() for checkbox in self.checkboxes]