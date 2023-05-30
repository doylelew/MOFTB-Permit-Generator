import customtkinter as ctk


class GUI_App:
    def __init__(self, parent: ctk.CTk):
        self.parent = parent
        self.parent.geometry('250x200')
        self.parent.resizable(False, False)
        self.parent.wm_title('MOFTB NY Permit Generator')

        self.counter = '0'

        self.label = ctk.CTkLabel(self.parent, text=self.counter,
                                  font=('Helvetica bold', 26))
        self.label.place(relx=0.5, rely=0.4, anchor='center')

        self.inc_button = ctk.CTkButton(self.parent, text="increment", command=self.increment)
        self.inc_button.place(relx=0.5, rely=0.6, anchor='center')

        self.res_button: ctk.CTkButton | None = None

    def increment(self):
        if self.counter == '0':
            self.res_button = ctk.CTkButton(self.parent, text="Reset",
                                            command=self.reset,
                                            corner_radius=20,
                                            fg_color="red", hover_color="darkred")
            self.res_button.place(relx=0.5, rely=0.8, anchor='center')
        self.counter = str(int(self.counter) + 1)
        self.label.configure(text=self.counter)

    def reset(self):
        self.counter = '0'
        self.label.configure(text=self.counter)

        self.res_button.destroy()


def Start_GUI():
    window = ctk.CTk()
    gui = GUI_App(parent=window)
    window.mainloop()
    return gui
