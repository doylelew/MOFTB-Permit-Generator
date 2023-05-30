import customtkinter as ctk
from .GUI_Framework import SubFrameTemplate, MainWindow

class InfoPage(SubFrameTemplate):
    def __init__(self, parent: MainWindow| ctk.CTk):
        super().__init__(parent)

    def open(self, message: str):
        super().open()
        self.header = ctk.CTkLabel(self.frame, text=message)
        self.header.place(relx=0.5, rely=0.2, anchor='center')

        self.frame.pack(fill='both', expand=True)

    def close(self):
        self.header.destroy()
        super().close()