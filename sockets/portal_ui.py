# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/portal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-19
# VERSION:	10.04.02
# PURPOSE:  New version leaves out intended operation of a reactive hanus model of control, only leaving it for development for the Meta data widget and for mediation with data. 
# NOTE:     This module defines a modular, multi-view graphical user interface framework built with Tkinter. It provides a top-level `Portal` class that manages multiple `ViewFrame` subframes, each rendering its own independent canvas scene and set of interactive PNG-based buttons. Each `ViewFrame` instance contains: A canvas visual defined by a dedicated scene-builder function & A collection of `PNGButton` instances, each constructed from externally-specified configuration data (image path, size, position, and message value).

import tkinter as tk
from command_line import CommandLine
try:
    from PIL import Image, ImageTk   # optional but used for clean resizing
    _PIL_OK = True
except Exception:
    _PIL_OK = False

buttons_feed: list[list[dict]] = [
    [  # View 0
        {"path": "assets/imgs/Syst.png",     "size": (292, 292), "pos": (319, 113),  "message": "nav;app:Syst"},
    ],
    [  # View 1
        {"path": "sockets/imgs/HID.png",   "size": (32, 32), "pos": (1094, 674),  "message": "nav;app:HID"},
        {"path": "sockets/imgs/HOD.png",   "size": (32, 32), "pos": (1094, 6),  "message": "nav;app:HOD"},
        {"path": "sockets/imgs/MSN.png",   "size": (32, 32), "pos": (6, 6),  "message": "nav;app:HOD"},
        {"path": "sockets/imgs/workflow.png",   "size": (72, 72), "pos": (5, 141),  "message": "nav;app:workflow"},
        {"path": "sockets/imgs/profile.png",   "size": (72, 72), "pos": (5, 179),  "message": "nav;app:profile"},
        {"path": "sockets/imgs/archive.png",   "size": (72, 72), "pos": (5, 217),  "message": "nav;app:archive"},
        {"path": "sockets/imgs/analysis.png",   "size": (72, 72), "pos": (5, 255),  "message": "nav;app:analysis"},
        {"path": "sockets/imgs/calendar.png",   "size": (72, 72), "pos": (5, 293),  "message": "nav;app:calendar"},
        {"path": "sockets/imgs/meta.png",   "size": (72, 72), "pos": (5, 331),  "message": "nav;app:meta"},
    ],
    [   # View 2
        {"path": "assets/imgs/HID.png",     "size": (45, 45), "pos": (8, 10),  "message": "nav;app:Syst"},
    ],
    [   # View 3
        {"path": "assets/imgs/HOD.png",     "size": (45, 45), "pos": (8, 672),  "message": "nav;app:Syst"},
    ],
    [   # View 4
        {"path": "assets/imgs/MSN.png",     "size": (45, 45), "pos": (1092, 672),  "message": "nav;app:Syst"},
    ],
]

class PNGButton:
    def __init__(self, parent_frame: tk.Frame, img_path: str,
                 size: tuple[int, int] | None, pos: tuple[int, int], message: str):
        self.parent_frame = parent_frame
        self.img_path = img_path
        self.size = size
        self.pos = pos
        self.message = message

        if _PIL_OK:
            img = Image.open(self.img_path)
            if self.size:
                img = img.resize(self.size, Image.LANCZOS)
            self._photo = ImageTk.PhotoImage(img)
        else:
            self._photo = tk.PhotoImage(file=self.img_path)

        self.widget = tk.Button(
            parent_frame,
            image=self._photo,
            command=self._on_click,
            bd=0, relief="flat",
            highlightthickness=0,
            cursor="hand2",
            takefocus=0
        )
        x, y = self.pos
        self.widget.place(x=x, y=y, anchor="nw")

    def _on_click(self):
        on_submit(self.message)

    def enable(self):  self.widget.configure(state="normal")
    def disable(self): self.widget.configure(state="disabled")


W, H      = 1100, 700
BG        = "#dedbec"
OUT       = "#3f403a"
FILL      = "#b9b8ac"
BAR_H     = 19
M         = 8
COL_W     = 52
R_COL     = 8
NBOX      = 6

def _base_canvas(parent):
    c = tk.Canvas(parent, width=W, height=H, bg=BG, highlightthickness=0, bd=0)
    # bottom bar
    c.create_rectangle(0, H - BAR_H, W, H, fill=OUT, outline="")
    return c

def _left_column_right_rounded(c):
    x0, x1 = M, M + COL_W
    y0, y1 = M, H - M - BAR_H

    c.create_rectangle(x0, y0, x1, y1, fill=FILL, outline=OUT, width=2)
    # carve right corners with BG, then redraw outline
    c.create_arc(x1 - 2*R_COL, y0,           x1, y0 + 2*R_COL, start=0,   extent=90,  fill=BG,  outline=BG)
    c.create_arc(x1 - 2*R_COL, y1 - 2*R_COL, x1, y1,           start=270, extent=90,  fill=BG,  outline=BG)
    c.create_arc(x1 - 2*R_COL, y0,           x1, y0 + 2*R_COL, start=0,   extent=90,  style="arc", outline=OUT, width=2)
    c.create_line(x1, y0 + R_COL, x1, y1 - R_COL, fill=OUT, width=2)
    c.create_arc(x1 - 2*R_COL, y1 - 2*R_COL, x1, y1,           start=270, extent=90,  style="arc", outline=OUT, width=2)

    step = (y1 - y0) / NBOX
    for i in range(1, NBOX):
        y = y0 + i * step
        c.create_line(x0, y, x1, y, fill=OUT, width=2)


def scene_top_left_quarter(parent):
    c = _base_canvas(parent)
    _left_column_right_rounded(c)
    R = 120
    c.create_oval(-2*R, -2*R, 2*R, 2*R, fill=FILL, outline=OUT, width=2)
    return c

def scene_bottom_left_quarter(parent):
    c = _base_canvas(parent)
    _left_column_right_rounded(c)
    R = 120
    c.create_oval(-2*R, H - BAR_H - 2*R, 2*R, H - BAR_H, fill=FILL, outline=OUT, width=2)
    return c

def scene_bottom_right_quarter(parent):
    c = _base_canvas(parent)
    _left_column_right_rounded(c)
    R = 120
    c.create_oval(W - 2*R, H - BAR_H - 2*R, W + 2*R, H - BAR_H, fill=FILL, outline=OUT, width=2)
    return c

def scene_large_panel(parent):
    c = _base_canvas(parent)
    _left_column_right_rounded(c)

    L = M + COL_W + 40
    T = M
    Rr = W - M
    Bb = H - BAR_H
    RTL = 230
    RBR = 140

    c.create_line(L + RTL, T,    Rr, T,        fill=OUT, width=2)
    c.create_line(Rr, T,         Rr, Bb - RBR, fill=OUT, width=2)
    c.create_line(Rr - RBR, Bb,  L,  Bb,       fill=OUT, width=2)
    c.create_line(L,  Bb,        L,  T + RTL,  fill=OUT, width=2)
    c.create_arc(L - 2*RTL, T - 2*RTL, L, T,         start=0,   extent=90, style="arc", outline=OUT, width=2)
    c.create_arc(Rr, Bb, Rr + 2*RBR, Bb + 2*RBR,     start=180, extent=90, style="arc", outline=OUT, width=2)
    c.create_arc(L - 2*RTL, T - 2*RTL, L, T,         start=180, extent=90, fill=FILL, outline="")
    c.create_arc(Rr, Bb, Rr + 2*RBR, Bb + 2*RBR,     start=0,   extent=90, fill=FILL, outline="")
    return c

def scene_beige_plate_with_dot(parent):
    c = tk.Canvas(parent, width=W, height=H, bg=OUT, highlightthickness=0, bd=0)
    Rbig = 120
    pad = 0
    c.create_rectangle(pad + Rbig, pad, W - pad - Rbig, H - pad, fill=FILL, outline="")
    c.create_rectangle(pad, pad + Rbig, W - pad, H - pad - Rbig, fill=FILL, outline="")
    c.create_oval(pad, pad, 2*Rbig, 2*Rbig, fill=FILL, outline="")
    c.create_oval(W - 2*Rbig - pad, pad, W - pad, 2*Rbig + pad, fill=FILL, outline="")
    c.create_oval(pad, H - 2*Rbig - pad, 2*Rbig + pad, H - pad, fill=FILL, outline="")
    c.create_oval(W - 2*Rbig - pad, H - 2*Rbig - pad, W - pad, H - pad, fill=FILL, outline="")
    # center dot
    rc = 70
    cx, cy = W // 2, H // 2
    c.create_oval(cx - rc, cy - rc, cx + rc, cy + rc, fill=OUT, outline="")
    return c

class ViewFrame(tk.Frame):
    def __init__(self, parent, view_id: int, scene_builder, buttons: list[dict] | None = None):
        super().__init__(parent)
        self.view_id = view_id

        # build the scene canvas inside this frame
        self.canvas = scene_builder(self)
        self.canvas.pack(fill="both", expand=True)

        # build buttons (if any)
        self.buttons: list[PNGButton] = []
            
        for btn in buttons_feed:
            btn = PNGButton(
                buttons_feed[btn] # Where buttons_feed is a list of list of specs to build buttons.
            )
            self.buttons.append(btn)

class Portal:
    def __init__(self, app_state=None):
        self.app = app_state
        self.root = tk.Tk()
        self.root.title(getattr(self.app, "title", "Portal"))
        self.root.geometry(f"{W}x{H}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Put your 5 scene builders in order:
        scene_builders = [
            scene_beige_plate_with_dot,
            scene_bottom_right_quarter,
            scene_bottom_left_quarter,
            scene_top_left_quarter,
            scene_large_panel,
        ]

        self.views: list[ViewFrame] = []
        for i in range(5):
            btn_specs = buttons_feed[i] if i < len(buttons_feed) else None
            vf = ViewFrame(self.main_frame, view_id=i, scene_builder=scene_builders[i], buttons=btn_specs)
            self.views.append(vf)

        self.current_view = 0
        for i, v in enumerate(self.views):
            if i == self.current_view:
                v.pack(fill="both", expand=True)
            else:
                v.pack_forget()
        
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

    def switch_view(self, index: int):
        if 0 <= index < len(self.views) and index != self.current_view:
            self.views[self.current_view].pack_forget()
            self.views[index].pack(fill="both", expand=True)
            self.current_view = index

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    Portal().start()
