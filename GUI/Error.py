import customtkinter as ctk
from .GUI_Framework import SubFrameTemplate

class ErrorPage(SubFrameTemplate):
    def __init__(self):
        super().__init__()

    def open(self, message: str):
        super().open()
        header = ctk.CTkLabel(self.frame, text=message)
        header.place(relx=0.5, rely=0.2, anchor='center')

        self.frame.pack(fill='both', expand=True)

    def close(self):
        header.destroy()
        super().close()