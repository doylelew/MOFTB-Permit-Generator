from __future__ import annotations

from selenium import webdriver

import customtkinter as ctk


class SubFrameTemplate:
    def __init__(self, parent: ctk.CTkFrame):
        self.parent = parent
        self.frame: ctk.CTkFrame | None = None
        self.browser: webdriver | None = None
        self.routes = {'success': None, 'error': None, 'back': None}

    def addFrameToParent(self, parent:ctk.CTk):
        self.parent = parent
        return self

    def open(self):
        print("parent tried to open")
        self.frame = ctk.CTkFrame(self.parent)

    def close(self):
        self.frame.destroy()

    def getFrame(self):
        return self.frame

    def defineRoutes(self, routes: list[tuple[str, SubFrameTemplate]]):
        for pair in routes:
            if pair[0] in self.routes:
                self.routes[pair[0]] = pair[1]
                continue
            raise Exception(f"{pair[0]} is not a deifined route type")

    def receiveBrowser(self, browser: webdriver):
        self.browser = browser

class MainWindow:
    def __init__(self, parent: ctk.CTk):
        self.parent = parent
        self.parent.geometry('900x720')
        self.parent.resizable(False, False)
        self.parent.wm_title('Unofficial MOFTB NY Permit Generator')

    def run(self):
        self.parent.mainloop()
