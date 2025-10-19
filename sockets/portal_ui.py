# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/portal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-18
# VERSION:	10.03.09
# PURPOSE:  This current version leaves out most of the intended operation of a reactive hanus model of control, only leaving it for development for the Meta data widget and for mediation with data. 

import tkinter as tk
from command_line import CommandLine

class ImageSlot(tk.Frame):
    def __init__(self, parent: tk.Widget, img_path, view_lbl):
        super().__init__(parent, bg="#000000")
        view_lbl = tk.Label(self, bd=0, highlightthickness=0, bg="#000000")
        view_lbl.pack(fill="both", expand=True)
        self.img_photo = tk.PhotoImage(file=img_path)
        view_lbl.configure(image=self.img_photo)

class ViewDeck(tk.Frame):
    def __init__(self, parent: tk.Widget):
        super().__init__(parent, bg="#000000")
        self.paths = ["assets/imgs/view0.png", "assets/imgs/view1.png", "assets/imgs/view2.png", "assets/imgs/view3.png", "assets/imgs/view4.png"]
        self.lbls = ["Splash", "System", "Configuration", "Interface", "Network"]
        self.slots: list[ImageSlot] = []
        for p in paths:
            slot = ImageSlot(self, p, self.lbls[p])
            slot.place(x=0, y=0, relwidth=1.0, relheight=1.0)
            self.slots.append(slot)
        self._current = None

    def show(self, idx):
        if not (0 <= idx < len(self.slots)):
            idx = 0
        if idx != self._current:
            self.slots[idx].tkraise()
            self._current = idx

class Portal:
    def __init__(self, app_state):
        self.app = app_state
        self.root = tk.Tk()
        self.root.title(self.app.title)
        self.root.geometry(str(self.app.ui_rows)+"x"+str(self.app.ui_cols))
        
        top = tk.Frame(self.root, bg="#000000")
        top.pack(side="top", fill="both", expand=True)
        
        self.deck = ViewDeck(top, self.paths)
        self.deck.pack(fill="both", expand=True)
        
        bottom = tk.Frame(self.root)
        bottom.pack(side="bottom", fill="x")

        def on_submit(text: str):
            self.app.enqueue_hid(text.encode("utf-8"))
            self.app.hid_flag = True

        self.cmd = CommandLine(
            bottom, on_submit=on_submit,
            font=("Courier New", 12),
            relief="sunken", bd=1,
        )
        
        self.cmd.pack(side="left", fill="x", expand=True, padx=8, pady=8)
        self.root.after(0, self.cmd.focus_set)  # keep focus on cmd
        
        def on_click_left(x: int, y: int):
            self.app.enqueue_hid(("inv" + str(x) + ", " + str(y)).encode("utf-8"))
            self.app.hid_flag = True
        
        def on_click_right(x: int, y: int):
            self.app.enqueue_hid(("inv" + str(x) + ", " + str(y)).encode("utf-8"))
            self.app.enqueue_hid(("med" + str(x) + ", " + str(y)).encode("utf-8"))
            self.app.hid_flag = True
        
        self.mouse = MsCrsr(
            parent_widget=self.deck,  # or the specific frame/canvas/label showing the PNG
            on_left=lambda x, y: self.on_click_left(x, y),
            on_right=lambda x, y: self.on_click_right(x, y),
        )
        
        self.root.after(self.app.poll_ms, self._tick)
        
    def _tick(self):
        flags = getattr(self.app, "update_flag", False)
        if flags:
            self.deck.show(int(getattr(self.app, "hanus_attention", 0)))
        self.root.after(self.app.poll_ms, self._tick)

    def start(self):
        self.root.mainloop()
