# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/portal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-07
# VERSION:	10.02.05
# PURPOSE:  A tkinter module that serves as both a simple input and output interface for my main program. The tkinter window acts like a front end. It’s a blank window that takes all the user’s keyboard input when it’s in focus and passes that input back to the main program as variables or events. Then the main program does whatever processing it needs and can send output data back to the tkinter module, which will display it in the window.

import tkinter as tk
from datetime import datetime
from command_line import CommandLine
from window_renderer import WindowRenderer

class Portal:
    def __init__(self, app_state, title="Input"):
        self.app = app_state

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("1100x700")

        # Top area: renderer container
        top = tk.Frame(self.root)
        top.pack(side="top", fill="both", expand=True)

        # Bottom: command line
        bottom = tk.Frame(self.root)
        bottom.pack(side="bottom", fill="x")

        # Wire command line -> HID enqueue (line-based)
        def on_submit(text: str):
            self.app.enqueue("hid", text.encode("utf-8"), ts=datetime.utcnow())

        self.cmd = CommandLine(
            bottom,
            on_submit=on_submit,
            font=("Courier New", 12),
            relief="sunken",
            bd=1,
        )
        self.cmd.pack(side="left", fill="x", expand=True, padx=8, pady=8)

        # Plug in renderer
        self.renderer = WindowRenderer(parent=top, app_state=self.app)
        self.renderer.container.pack(fill="both", expand=True)

        # Kick focus to the command line; start renderer polling
        self.root.after(0, self.cmd.focus_set)
        self.renderer.start(self.root)

    def start(self):
        self.root.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

