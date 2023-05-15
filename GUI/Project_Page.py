import customtkinter as ctk

from .GUI_Framework import SubFrameTemplate

from WebDriver import ProjectList

class ProjectPage(SubFrameTemplate):
    def __init__(self, parent:ctk.CTk):
        super().__init__(parent)

    def open(self):
        super().open()


        self.frame.pack(fill='both', expand=True)

    def close(self):
        super().close()