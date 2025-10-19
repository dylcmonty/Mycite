# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/portal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-19
# VERSION:	10.04.01
# PURPOSE:  This current version leaves out most of the intended operation of a reactive hanus model of control, only leaving it for development for the Meta data widget and for mediation with data. 

import tkinter as tk
from command_line import CommandLine

class ViewFrame(tk.Frame):
    def __init__(self, parent, view_id):
        super().__init__(parent)
        self.parent_frame = parent

        # Add a canvas to each view frame
        self.canvas = tk.Canvas(self, bg=bg_color, self.parent_frame.app.ui_rows, self.parent_frame.app.ui_cols)
        self.canvas.pack(fill="both", expand=True)

class Portal:
    def __init__(self, app_state):
        self.app = app_state
        self.root = tk.Tk()
        self.root.title(self.app.title)
        self.root.geometry(str(self.app.ui_rows)+"x"+str(self.app.ui_cols))

        # Main container
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Create 5 view frames
        self.child_frame = []
        for i in range(5):
            child_frame = ViewFrame(self.main_frame, view_id=i, bg_color=color)
            self.child_frame.append(view)

        self.current_view = 0
        self.views[self.current_view].pack(fill="both", expand=True)

        # Input frame at the bottom (always visible)
        self.cmd = CommandLine(
            bottom, on_submit = on_submit,
            font=("Courier New", 12),
            relief="sunken", bd=1,
        )
        self.input_frame.pack(fill="x", side="bottom")
        
        def on_submit(text: str):
            self.app.enqueue_hid(text.encode("utf-8"))
            self.app.hid_flag = True
        
    def switch_view(self, index):
        if 0 <= index < len(self.views):
            self.views[self.current_view].pack_forget()
            self.views[index].pack(fill="both", expand=True)
            self.current_view = index
        
        self.root.after(self.app.poll_ms, self._tick)

    def start(self):
        self.root.mainloop()
