from __future__ import  annotations

import requests
import customtkinter as ctk

class SubFrameTemplate:
    def __init__(self, parent: MainWindow, next_frame_name: str | None):
        self.master = parent
        self.parent = self.master.getParentFrame()
        self.frame = ctk.CTkFrame(self.parent)
        self.next_frame_name = next_frame_name

    def open(self):
        self.frame.pack(fill='both', expand=True)

    def close(self):
        self.frame.pack_forget()


class LoadingPage(SubFrameTemplate):
    def __init__(self, parent:ctk.CTk):
        super().__init__(parent, None)
        self.message = ""
        self.header = ctk.CTkLabel(self.frame, text=self.message)

    def open(self):
        self.header.place(relx=0.5, rely=0.2, anchor='center')
        super().open()

    def setMessage(self, message:str):
        self.message = message
        self.header.configure(text=self.message)

class MainWindow:
    def __init__(self, parent: ctk.CTk, session:requests.Session):
        self.parentFrame = parent
        self.session = session

        self.parentFrame.geometry('900x720')
        self.parentFrame.resizable(False, False)
        self.parentFrame.wm_title('Unofficial MOFTB NY Permit Generator')

        self.frames: dict[str: ctk.CTkFrame] | None
        self.loading_frame = LoadingPage(parent=self)

    def build(self, dict_of_frames):
        self.frames = dict_of_frames

    def loadingStart(self, loading_message:str):
        self.loading_frame.setMessage(loading_message)
        self.loading_frame.open()

    def loadingEnd(self):
        self.loading_frame.close()

    def jumpToFrame(self, page_name:str):
        if self.frames[page_name] == None:
            raise Exception(f"Frame labeled {page_name} does not exist please be sure to add it to build() dictionary")
        self.frames[page_name].open()

    def run(self, startFrame:str):
        if self.frames[startFrame] == None:
            if self.frames == None:
                raise Exception("There are no Frames attached to MainWindow. Please use Main window build function to attach frames")
            raise Exception(f"{startFrame} is not a frame in MainWindow please add it to your dictionary of frames in the build function")
        self.frames[startFrame].open()
        self.parentFrame.mainloop()

    def getParentFrame(self):
        return self.parentFrame
