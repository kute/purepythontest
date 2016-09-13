#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/12 22:35'

"""

"""
import tkinter
from tkinter import Menu
from tkinter.messagebox import askokcancel, askquestion, askyesno, showwarning, showerror, showinfo


class TestMenu(Menu):

    def __init__(self, master):
        self.master = master or tkinter.Tk()
        Menu.__init__(self, master)
        self.add_commands()

    def ask_cancel(self):
        cancel = askokcancel(title="确定or取消", message="是否确定？")
        if not cancel:
            print("You click cancel")
        else:
            print("You click sure")

    def ask_yes_no(self):
        yes = askyesno(title="ask yes no", message="你喜欢吗？")
        if yes == "yes":
            print("You click yes")
        else:
            print("You click no")

    def ask_question(self):
        yes = askquestion(title="ask question", message="你喜欢问问题吗？")
        if yes == "yes":
            print("You click yes question")
        else:
            print("You click no question")

    def ask_retry_cancel(self):
        ask = askretrycancel(title="ask retry cancel", message="重试吧 ？")
        if ask:
            print("retry")
        else:
            print("cancel retry")

    def show_warning(self):
        show = showwarning(title="show warning title", message="ClassNotFound........")
        if show == "ok":
            print("show warning ok")

    @property
    def label(self):
        return "Test"

    def add_commands(self):
        self.add_command(label="确定or取消", command=self.ask_cancel)
        self.add_command(label="yes or no", command=self.ask_yes_no)
        self.add_command(label="ask question", command=self.ask_question)
        self.add_command(label="ask retry cancel", command=self.ask_retry_cancel)
        self.add_command(label="show warning", command=self.show_warning)
        self.add_separator()
        self.add_command(label="Quit", command=self.quit)
