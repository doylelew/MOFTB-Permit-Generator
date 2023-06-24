import time

import customtkinter as ctk
import requests

from .GUI_Framework import SubFrameTemplate, MainWindow
from WebDriver import login


#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"
Test404 = "https://photos.google.com/meory/"


class LoginPage(SubFrameTemplate):
    def __init__(self, parent: MainWindow | ctk.CTk, next_frame_name: str | None):
        self.login_data: tuple[str,str] | None
        self.frame: ctk.CTkFrame | None
        super().__init__(parent, next_frame_name)

        self.header = ctk.CTkLabel(self.frame,
                                   text="Please enter your MOFTB Login information and choose a prefered broswer")

        self.browser_values = ["Firefox", "Chrome"]
        self.browser_choicebox = ctk.CTkOptionMenu(self.frame, values=self.browser_values,
                                                   command=self.changeBroswerOption, width=300, height=40)
        self.browser_choice = self.browser_values[0]

        self.login_text = ctk.CTkLabel(self.frame, text="Email Address")

        self.login_entry = ctk.CTkEntry(self.frame, width=300, height=40)

        self.password_text = ctk.CTkLabel(self.frame, text="MOFTB password")

        self.password_entry = ctk.CTkEntry(self.frame, show="*", width=300, height=40)

        self.sumbit_button = ctk.CTkButton(self.frame, text="Submit", command=self.submit, fg_color="blue",
                                           hover_color="lightblue")


    def open(self):

        self.header.place(relx=0.5, rely=0.15, anchor='center')

        self.browser_choicebox.place(relx=0.5, rely=0.2, anchor='center')
        self.browser_choicebox.set( self.browser_choice)

        self.login_text.place(relx=0.5, rely=0.25, anchor='center')

        self.login_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.password_text.place(relx=0.5, rely=0.35, anchor='center')

        self.password_entry.place(relx=0.5, rely=0.4, anchor='center')

        self.sumbit_button.place(relx=0.5, rely=0.5, anchor='center')

        super().open()


    # def close(self):
    #     # self.header.place_forget()
    #     # self.browser_choicebox.place_forget()
    #     # self.login_text.place_forget()
    #     # self.login_entry.place_forget()
    #     # self.password_text.place_forget()
    #     # self.password_entry.place_forget()
    #     # self.sumbit_button.place_forget()
    #     super().close()

    def changeBroswerOption(self, choice):
        self.browser_choice = choice

    def submit(self):
        self.login_data = (self.login_entry.get(), self.password_entry.get())
        self.close()

        self.parent_wrapper.loadingStart("Loading...\n Please wait while we receive information from MOFTB website")

        try:
            success, response =login(session=self.parent_wrapper.session, username=self.login_data[0], password=self.login_data[1])
        except:
            self.header.configure(text="username or password was incorrect please check both and try again", text_color='red')
            self.parent_wrapper.loadingEnd()
            self.open()
            return
            #todo seperate out types of exceptions and responses

        if success:
            self.parent_wrapper.jumpToFrame(self.next_frame_name)
            self.parent_wrapper.loadingEnd()
            return
        self.header.configure(text="something mysterious happend please try again",
                              text_color='red')
        self.open()
        return




        # if 'ctkframe' not in str(self.browser_choice):
        #     self.login_data = (self.login_entry.get(), self.password_entry.get())
        #     self.close()
        #     self.routes['error'].open("Loading data from MOFTB website please wait")
        #     self.browser = OpenBrowser(starting_url=MOFTBUrl, browser_type=self.browser_choice)
        #     try:
        #         Login(self.browser, self.login_data[0], self.login_data[1])
        #     except:
        #         self.routes['error'].close()
        #         self.open()
        #         self.header.configure(text="There was a problem logging in, please check your email and password ")
        #     return



