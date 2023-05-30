import tkinter

import customtkinter as ctk
import tkinter

from .GUI_Framework import SubFrameTemplate, MainWindow
from WebDriver import projectList, permitList


class PermitPage1(SubFrameTemplate):

    def __init__(self, parent: MainWindow | ctk.CTk, next_frame_name: str | None = None):
        super().__init__(parent, next_frame_name)

        self.permit_name_text = ctk.CTkLabel(self.frame, text="Permit Name")
        self.permit_name_entry = ctk.CTkEntry(self.frame, width=300, height=40)

        self.permit_codes = {
            "shooting": 39,
            "rigging": 40,
            "scouting": 41,
            "DCAS": 42,
            "Theater Load Outs": 44,
        }

        self.radio_val = tkinter.IntVar(master=self.frame, value=0)

        self.shoot_permit_radio = ctk.CTkRadioButton(self.frame, text="Shooting Permit",
                                                     command=self.permitTypeSelect,
                                                     variable=self.radio_val, value=self.permit_codes["shooting"])

        self.rigging_permit_radio = ctk.CTkRadioButton(self.frame, text="Rigging Permit",
                                                       command=self.permitTypeSelect,
                                                       variable=self.radio_val, value=self.permit_codes["rigging"])

        self.scouting_permit_radio = ctk.CTkRadioButton(self.frame, text="Scouting Permit",
                                                        command=self.permitTypeSelect,
                                                        variable=self.radio_val, value=self.permit_codes["scouting"])

        self.dcas_permit_radio = ctk.CTkRadioButton(self.frame, text="DCAS Permit",
                                                        command=self.permitTypeSelect,
                                                        variable=self.radio_val, value=self.permit_codes["DCAS"])

        self.theater_permit_radio = ctk.CTkRadioButton(self.frame, text="Theater Load Out Permit",
                                                        command=self.permitTypeSelect,
                                                        variable=self.radio_val, value=self.permit_codes["Theater Load Outs"])


    def open(self):
        self.permit_name_text.place(relx=0.5, rely=0.2, anchor='center')
        self.permit_name_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.shoot_permit_radio.place(relx=0.5, rely=0.4, anchor='center')
        self.rigging_permit_radio.place(relx=0.5, rely=0.45, anchor='center')
        self.scouting_permit_radio.place(relx=0.5, rely=0.5, anchor='center')
        self.dcas_permit_radio.place(relx=0.5, rely=0.55, anchor='center')
        self.theater_permit_radio.place(relx=0.5, rely=0.6, anchor='center')


        super().open()

    def permitTypeSelect(self):
        selected = ""
        for key in self.permit_codes:
            if self.permit_codes[key] == self.radio_val.get():
                selected = key
        print(f"Selected {selected} with code {self.radio_val.get()}")
