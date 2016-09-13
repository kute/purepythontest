#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/12 22:35'

"""

"""
import tkinter
from tkinter import Menu


class FileMenu(Menu):

    def __init__(self, master):
        self.master = master or tkinter.Tk()
        Menu.__init__(self, master)
        self.add_commands()

    def new_window(self):
        print("New Winow")

    @property
    def label(self):
        return "File"

    def add_commands(self):
        self.add_command(label="New Window", command=self.new_window)
        self.add_separator()
        self.add_command(label="Quit", command=self.quit)
