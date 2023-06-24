from __future__ import  annotations

import requests
import customtkinter as ctk

class SubFrameTemplate:
    """
    A class that acts as the base class for frames in your GUI application. Subframes are not meant to be used as their own class but instead as a base. E.g. HomePage(SubFrameTemplate).
    """
    def __init__(self, parent: MainWindow, next_frame_name: str | None = None):
        """
        constructor for SubframeTemplate
        :param parent: The application frame you would like to attach this frame to
        :param next_frame_name: The frame you would like to open next from within this frame when moving on.
        """
        self.parent_wrapper = parent
        self.parent = self.parent_wrapper.getParentFrame()
        self.frame = ctk.CTkFrame(self.parent)
        self.next_frame_name = next_frame_name

    def open(self):
        """
        Renders the frame and it's children to the screen using the pack method. Add an override method to a class that uses this as a base that renders the individual child elements. End that overriode with super() command.
        :return: None
        """
        self.frame.pack(fill='both', expand=True)

    def close(self):
        """removes the frame and it's children from the screen"""
        self.frame.pack_forget()


class LoadingPage(SubFrameTemplate):
    """
    A base frame that can be used to display info and can be called by any child of Mainframe
    """
    def __init__(self, parent:ctk.CTk):
        """
        constructor for LoadingPage object
        :param parent: Mainframe object
        """
        super().__init__(parent, None)
        self.message = ""
        self.header = ctk.CTkLabel(self.frame, text=self.message)

    def open(self):
        """
        Adds a header with information to the SubFrame Template open method and supers it's method
        :return: None
        """
        self.header.place(relx=0.5, rely=0.2, anchor='center')
        super().open()

    def setMessage(self, message:str):
        """
        Set the message that displays on loading page
        :param message: String of the message to display
        :return: None
        """
        self.message = message
        self.header.configure(text=self.message)

class MainWindow:
    """
    This is the window that controls the app and the window that runs the main loop for the application. It is a class that wraps the ctk.CTK() class that controlls the tkinter frame handling

    """
    def __init__(self, parent: ctk.CTk, session:requests.Session):
        """
        constructor for the Mainwindow
        :param parent: The CTK class from customTkinter
        :param session: The Requests session so child frames can access request data and make requests
        """
        self.parentFrame = parent
        self.session = session

        self.parentFrame.geometry('900x720')
        self.parentFrame.resizable(False, False)
        self.parentFrame.wm_title('Unofficial MOFTB NY Permit Generator')

        self.frames: dict[str: ctk.CTkFrame] | None
        self.loading_frame = LoadingPage(parent=self)

    def build(self, dict_of_frames):
        """
        Defiine your application frames as an argument for this function.
        :param dict_of_frames: A dictionary of the frames that will be made accessible to the childframes
        :return: None
        """
        self.frames = dict_of_frames

    def loadingStart(self, loading_message:str):
        """
        Render the loading screen to the frame
        :param loading_message: String that displays a message to user
        :return: None
        """
        self.loading_frame.setMessage(loading_message)
        self.loading_frame.open()

    def loadingEnd(self):
        """
        Hide the loading screen to the frame
        :return: None
        """
        self.loading_frame.close()

    def jumpToFrame(self, page_name:str):
        """
        allows a child frame to open another frame that is held by this object
        :param page_name: The string name of the frame you want to jump to in this object's dictionary of frames defined in the build() function
        :return:
        """
        if self.frames[page_name] == None:
            raise Exception(f"Frame labeled {page_name} does not exist please be sure to add it to build() dictionary")
        self.frames[page_name].open()

    def run(self, startFrame:str):
        """
        runs the main loop and tells the parent_wrapper frame which of its children frames to open first
        :param startFrame: The string name of the frame you want to start with in this object's dictionary of frames defined in the build() function
        :return:
        """
        if self.frames[startFrame] == None:
            if self.frames == None:
                raise Exception("There are no Frames attached to MainWindow. Please use Main window build function to attach frames")
            raise Exception(f"{startFrame} is not a frame in MainWindow please add it to your dictionary of frames in the build function")
        self.frames[startFrame].open()
        self.parentFrame.mainloop()

    def getParentFrame(self):
        """
        Safely retrieve the CTK root frame
        :return: ctk.CTK object
        """
        return self.parentFrame
