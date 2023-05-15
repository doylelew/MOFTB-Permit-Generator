import customtkinter as ctk
from .GUI_Framework import SubFrameTemplate

class BrowserLogin(SubFrameTemplate):
    def __init__(self):
        super().__init__()

    def open(self):
        super().open()
        header = ctk.CTkLabel(self.frame, text="Please enter your MOFTB Login info and choose a prefered broswer")
        header.place(relx=0.5, rely=0.2, anchor='center')

        self.frame.pack(fill='both', expand=True)

    def close(self):
        header.destroy()
        super().close()