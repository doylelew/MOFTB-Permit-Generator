import customtkinter as ctk

from .GUI_Framework import SubFrameTemplate, MainWindow
from WebDriver import projectList, permitList


class ProjectPage(SubFrameTemplate):
    def __init__(self, parent: MainWindow | ctk.CTk, next_frame_name: str | None = None):
        super().__init__(parent, next_frame_name)
        self.header = ctk.CTkLabel(self.frame, text="Please choose the project and permit you would like to work on")
        self.select_project = None
        self.select_permit = None

        self.project_label = ctk.CTkLabel(self.frame, text="Project Select")
        self.project_values = []
        self.project_choicebox = ctk.CTkOptionMenu(self.frame, values=self.project_values,
                                                   command=self.switchProject, width=300, height=40)

        self.permit_label = ctk.CTkLabel(self.frame, text="Permit Select")
        self.permit_values = []
        self.permit_choicebox = ctk.CTkOptionMenu(self.frame, values=self.permit_values,
                                                  command=self.select_permit, width=300, height=40)

        self.select_button = ctk.CTkButton(self.frame, text="Select Permit", command=self.submit, fg_color="blue",
                                           hover_color="lightblue")

    def open(self):
        self.header.place(relx=0.5, rely=0.2, anchor='center')

        self.project_label.place(relx=0.5, rely=0.3, anchor='center')
        self.project_dict, response = projectList(session=self.master.session)
        # todo add a try exception here
        self.project_values = list(self.project_dict.keys())
        self.project_choicebox.configure(values=self.project_values)
        self.project_choicebox.set(self.project_values[0])
        self.project_choicebox.place(relx=0.5, rely=0.4, anchor='center')

        self.select_project = self.project_values[0]

        self.permit_label.place(relx=0.5, rely=0.5, anchor='center')
        self.permit_dict, response = permitList(session=self.master.session,
                                                intended_url=self.project_dict[self.project_values[0]])
        # todo add a try exception here
        self.permit_values = list(self.permit_dict.keys())
        self.permit_values.insert(0, "Create New Permit")
        self.permit_choicebox.configure(values=self.permit_values)
        self.permit_choicebox.set(self.permit_values[0])
        self.permit_choicebox.place(relx=0.5, rely=0.6, anchor='center')

        self.select_permit = self.permit_values[0]

        self.select_button.place(relx=0.5, rely=0.8, anchor='center')

        super().open()

    def switchProject(self, choice):
        self.select_permit = choice
        self.permit_dict, response = permitList(session=self.master.session,
                                                intended_url=self.project_dict[self.select_permit])
        # todo add a try exception here
        self.permit_values = []
        if self.permit_dict:
            self.permit_values = list(self.permit_dict.keys())
        self.permit_values.insert(0, "Create New Permit")
        self.permit_choicebox.configure(values=self.permit_values)
        self.permit_choicebox.set(self.permit_values[0])

        self.select_permit = self.permit_values[0]

    def selectPermit(self, choice):
        self.select_permit = choice
        print(f"Selected {self.select_permit}")

    def submit(self):
        pass
