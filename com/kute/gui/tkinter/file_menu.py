#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/12 22:35'

"""

"""
import tkinter
from tkinter import Menu
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor


class FileMenu(Menu):

    def __init__(self, master):
        self.master = master or tkinter.Tk()
        Menu.__init__(self, master)
        self.add_commands()

    def new_window(self):
        print("New Winow")

    def open_file(self):
        """
        single file
        """
        filename = askopenfilename(filetypes=[("text", "*.txt"), ("xml", "*.xml")])
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                for line in f:
                    print(line)
        except Exception as e:
            print("Cannot open file:{}, error:{}".format(filename, e))

    def open_color(self):
        color = askcolor(title="颜色面板")
        print(color)  # ((255.99609375, 0.0, 0.0), '#ff0000')

    @property
    def label(self):
        return "File"

    def add_commands(self):
        self.add_command(label="New Window", command=self.new_window)
        self.add_command(label="Open File", command=self.open_file)
        self.add_separator()
        self.add_command(label="Open Color Chooser", command=self.open_color)
        self.add_separator()
        self.add_command(label="Quit", command=self.quit)
