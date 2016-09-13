#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: SampleApplication.py
@ __mtime__: 2016/9/13 10:18

"""

import tkinter
from tkinter import Frame, Menu
from com.kute.gui.tkinter import test_menu, file_menu


class SampleApplication(tkinter.Frame):
    """"""
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.menubar = Menu(master=self.master)

        self.set_tk_size()
        self.set_tk_title()
        self.init_memnubar()

    def set_tk_size(self, size=None):
        self.master.geometry(size or "670x600")

    def set_tk_title(self, title="Sample Application"):
        self.master.title(title)

    def init_memnubar(self):
        """
        初始化菜单
        """
        filemenu = file_menu.FileMenu(master=self.menubar)
        self.menubar.add_cascade(label=filemenu.label, menu=filemenu)
        testmenu = test_menu.TestMenu(master=self.menubar)
        self.menubar.add_cascade(label=testmenu.label, menu=testmenu)
        # 加载菜单
        self.master.config(menu=self.menubar)


def main():
    root = tkinter.Tk()
    app = SampleApplication(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
