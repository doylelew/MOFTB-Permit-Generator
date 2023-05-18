from __future__ import annotations

from selenium import webdriver

import customtkinter as ctk


class SubFrameTemplate:
    def __init__(self, parent: ctk.CTkFrame):
        self.parent = parent
        self.frame: ctk.CTkFrame | None = None
        self.browser: webdriver | None = None
        self.routes = {'success': None, 'error': None, 'back': None}

    def open(self):
        print("parent tried to open")
        self.frame = ctk.CTkFrame(self.parent)

    def close(self):
        self.frame.destroy()

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
