import tkinter
import tkinter.messagebox
import customtkinter
import function

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Cognitive Coders GUI Masterclass")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Cognitive Coders",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Light", "Dark"],
                                                                       command=lambda values:
                                                                       function.change_appearance_mode_event(self, values))
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=lambda values: function.change_scaling_event(
                                                                   self, values))
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        

        # Sidebar for File selection and Label

        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        self.sidebar_frame2.grid(row=0, column=3, rowspan=4, sticky="nsew", padx=(20, 0), pady=(0, 10))
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        # File selection
        filetypes = (("all files", "*.*"), ('csv files', '*.csv'), ('Excel files', '*.xlsx'))
        self.filetypes = filetypes
        self.filename = "NO FILE SELECTED"

        # Set the title
        self.title = customtkinter.CTkLabel(self.sidebar_frame2, text="Select File location to Dowload", fg_color="transparent", corner_radius=6)
        self.title.grid(row=0, column=3, pady=(10, 0), sticky="nsew")

        # Chosen file name display
        self.file_name_display = customtkinter.CTkLabel(self.sidebar_frame2, text=function.get_filename(self),
                                                        fg_color="transparent")
        self.file_name_display.grid(row=2, column=3, pady=(10, 0), sticky='nsew')

        # Choose file button
        self.file_button = customtkinter.CTkButton(self.sidebar_frame2, text="Choose Destination Folder: ",
                                                   command=lambda: function.pick_folder(self))
        self.file_button.grid(row=1, column=3, padx=20, pady=10, sticky='nsew')

        # Option Menu
        self.drop_down_label = customtkinter.CTkLabel(self.sidebar_frame2, text="Select EEG: ", anchor="w")
        self.drop_down_label.grid(row=3, column=3, padx=20, pady=(40, 0))
        self.drop_down_label_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame2, values=["Right", "Left"],
                                                                       command=lambda values:
                                                                       function.set_label(self, values))
        self.drop_down_label_option_menu.set('Select a Label')
        self.drop_down_label_option_menu.grid(row=4, column=3, padx=20, pady=(0, 140))

        # Generate Button
        self.generate_button = customtkinter.CTkButton(self.sidebar_frame2, text="Generate EEG",
                                                       command=lambda: function.set_data(self, function.get_label(self)))
        self.generate_button.grid(row=5, column=3, padx=20, pady=(20, 10))

        # Download button
        self.Download_button = customtkinter.CTkButton(self.sidebar_frame2, text="Download",
                                                       command=lambda: function.download(self, function.get_label(self), function.get_folder(self), function.get_label(self)), state='disabled')
        self.Download_button.grid(row=6, column=3, padx=20, pady=(10, 20))

        # Show Plots button
        self.Show_Plot_button = customtkinter.CTkButton(self.sidebar_frame2, text="Open EEG Plots", command=lambda: function.plot(self, function.get_data(self)), state='disabled')
        self.Show_Plot_button.grid(row=7, column=3, padx=20)

        # Project Description
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0",
                            "Introduction\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"
                                                 " sed diam nonumy eirmod tempor invidunt ut labore et dolore"
                                                 " magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.textbox.configure(state='disabled')