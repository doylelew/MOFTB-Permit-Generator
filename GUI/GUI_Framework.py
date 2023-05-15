from __future__ import annotations

from selenium import webdriver

import customtkinter as ctk


class SubFrameTemplate:
    def __init__(self):
        self.frame: ctk.CTkFrame | None = None
        self.parent: ctk.CTk | None = None
        self.browser: webdriver | None = None
        self.routes = {'success': None, 'error': None, 'back': None}

    def addFrameToParent(self, parent:ctk.CTk):
        self.parent = parent
        return self

    def open(self):
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
        self.pages: []| None = None

    def run(self):
        self.parent.mainloop()

    def definePages(self, pages:[SubFrameTemplate]):
        self.pages = [page.addFrameToParent(self.parent) for page in pages]


def createWindow():
    app = ctk.CTk()
    window = MainWindow(parent=app)
    return window