#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/12 22:35'

"""

"""
import tkinter
from tkinter import Menu, Label


class HelpMenu(Menu):

    def __init__(self, master):
        self.master = master or tkinter.Tk()
        Menu.__init__(self, master)
        self.add_commands()

    def about(self):
        label = Label()
        label["text"] = """
        author: kute
        email: kutekute00@gmailc.om
        """
        label.pack(expand=1, side="top", fill="x")

    @property
    def label(self):
        return "Help"

    def add_commands(self):
        self.add_command(label="About", command=self.about)
        self.add_separator()
        self.add_command(label="Quit", command=self.quit)
