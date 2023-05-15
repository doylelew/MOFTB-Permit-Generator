import customtkinter as ctk

from .GUI_Framework import SubFrameTemplate

from WebDriver import OpenBrowser, Login

#################################################################
# Constants
#################################################################
MOFTBUrl = "https://nyceventpermits.nyc.gov/film/"
Test404 = "https://photos.google.com/meory/"


class BrowserLogin(SubFrameTemplate):
    def __init__(self):
        self.browser_choice: str | None = None
        self.login_data: tuple[str,str] | None
        super().__init__()


    def open(self):
        super().open()
        self.header = ctk.CTkLabel(self.frame, text="Please enter your MOFTB Login information and choose a prefered broswer")
        self.header.place(relx=0.5, rely=0.15, anchor='center')

        self.browser_values = ["Firefox", "Chrome"]
        self.browser_choicebox = ctk.CTkOptionMenu(self.frame, values= self.browser_values, command=self.changeBroswerOption, width= 300, height=40)
        self.browser_choicebox.place(relx=0.5, rely=0.2, anchor='center')
        self.browser_choicebox.set( self.browser_values[0])
        self.browser_choice =  self.browser_values[0]

        self.login_text = ctk.CTkLabel(self.frame, text="Email Address")
        self.login_text.place(relx=0.5, rely=0.25, anchor='center')

        self.login_entry = ctk.CTkEntry(self.frame, width= 300, height=40)
        self.login_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.password_text = ctk.CTkLabel(self.frame, text="MOFTB password")
        self.password_text.place(relx=0.5, rely=0.35, anchor='center')

        self.password_entry = ctk.CTkEntry(self.frame, show="*", width= 300, height=40)
        self.password_entry.place(relx=0.5, rely=0.4, anchor='center')

        self.sumbit_button = ctk.CTkButton(self.frame, text="Submit", command=self.submit, fg_color="blue", hover_color="lightblue")
        self.sumbit_button.place(relx=0.5, rely=0.5, anchor='center')

        self.frame.pack(fill='both', expand=True)

    def close(self):
        self.header.destroy()
        self.browser_choicebox.destroy()
        self.login_text.destroy()
        self.login_entry.destroy()
        self.password_text.destroy()
        self.password_entry.destroy()
        self.sumbit_button.destroy()

        super().close()

    def changeBroswerOption(self, choice):
        self.browser_choice = choice
        print(self.browser_choice)

    def submit(self):
        if 'ctkframe' not in str(self.browser_choice):
            self.login_data = (self.login_entry.get(), self.password_entry.get())
            self.close()
            self.routes['error'].open("Loading data from MOFTB website please wait")
            self.browser = OpenBrowser(starting_url=MOFTBUrl, browser_type=self.browser_choice)
            try:
                Login(self.browser, self.login_data[0], self.login_data[1])
            except:
                self.routes['error'].close()
                self.open()
                self.header.configure(text="There was a problem logging in, please check your email and password ")
            return

        #todo check that we land on the home page and there is not a login issue



