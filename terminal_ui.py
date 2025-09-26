# Copyright [2025] [Dylan Montgomery]
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/terminal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-09-26
# VERSION:	9.03.04
# PURPOSE:  HERE
# NOTES:    HERE

import tkinter as tk

def round_rect(canvas, x1, y1, x2, y2, r, **kw):
    r = max(0, min(r, (x2-x1)/2, (y2-y1)/2))
    canvas.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90, style="pieslice", **kw)
    canvas.create_arc(x2-2*r, y1, x2, y1+2*r, start=0,  extent=90, style="pieslice", **kw)
    canvas.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90, style="pieslice", **kw)
    canvas.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90, style="pieslice", **kw)
    canvas.create_rectangle(x1+r, y1,   x2-r, y2,   **kw)
    canvas.create_rectangle(x1,   y1+r, x2,   y2-r, **kw)

class App:
    def __init__(self, root):
        self.last_input = None

        root.title("MSS Control Gate")
        root.geometry("1100x700")

        # palette
        self.C_BG        = "#201c22"
        self.C_PANEL     = "#8f7a7a"
        self.C_BORDER    = "#141219"
        self.C_TILE      = "#4e5a64"
        self.C_TILE_ST   = "#3a444c"
        self.C_STATUS    = "#4a3d49"
        self.C_STATUS_TXT= "#d8ccd8"

        # --- TOP CANVAS ---
        self.canvas = tk.Canvas(root, bg=self.C_BG, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Configure>", self._on_canvas_resize)

        # --- BOTTOM COMMAND BAR ---
        self.bottom = tk.Frame(root, bg=self.C_STATUS)
        self.bottom.pack(side="bottom", fill="x")

        self.idle_label = tk.Label(
            self.bottom,
            text="/ENTER COMMAND OR 'Q' TO QUIT",
            fg=self.C_STATUS_TXT, bg=self.C_STATUS
        )
        self.idle_label.pack(side="left", padx=(10, 8), pady=6)

        self.entry = tk.Entry(
            self.bottom, bg=self.C_STATUS, fg=self.C_STATUS_TXT,
            highlightthickness=0, insertbackground=self.C_STATUS_TXT,
            relief="flat", justify="left"
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=6)
        self.entry.bind("<KeyRelease>", self._on_type)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()

        root.after_idle(self.draw)

    # ----- placeholder behavior -----
    def _hide_placeholder(self):
        if self.idle_label.winfo_manager():
            self.idle_label.pack_forget()
            self.entry.pack_forget()
            self.entry.pack(side="left", fill="x", expand=True, padx=10, pady=6)

    def _show_placeholder(self):
        if not self.idle_label.winfo_manager():
            self.idle_label.pack(side="left", padx=(10, 8), pady=6)
            self.entry.pack_forget()
            self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=6)

    def _on_type(self, _event):
        if self.entry.get():
            self._hide_placeholder()
        else:
            self._show_placeholder()

    def _on_enter(self, event):
        txt = self.entry.get().strip()
        self.last_input = txt
        self.entry.delete(0, tk.END)
        self._show_placeholder()
        if txt.lower() == "q":
            event.widget.winfo_toplevel().destroy()

    # ----- drawing -----
    def draw(self):
        c = self.canvas
        c.delete("all")
        w = c.winfo_width()  or 1100
        h = c.winfo_height() or 660

        m  = int(min(w, h) * 0.018)
        r  = int(min(w, h) * 0.14)
        bw = int(min(w, h) * 0.035)

        x1, y1 = m, m
        x2, y2 = w - m, h - m

        round_rect(c, x1, y1, x2, y2, r, fill=self.C_BORDER, outline="")
        round_rect(c, x1+bw, y1+bw, x2-bw, y2-bw, max(0, r-bw), fill=self.C_PANEL, outline="")

        d   = int(min(w, h) * 0.055)
        pad = int(min(w, h) * 0.01)
        for cx, cy in [(x1+pad+d//2, y1+pad+d//2),
                       (x2-pad-d//2, y1+pad+d//2),
                       (x2-pad-d//2, y2-pad-d//2)]:
            c.create_oval(cx-d//2, cy-d//2, cx+d//2, cy+d//2,
                          fill=self.C_PANEL, outline=self.C_BORDER, width=3)

        inset = int(min(w, h) * 0.10)
        gx1, gy1 = x1 + inset, y1 + inset
        gx2, gy2 = x2 - inset, y2 - inset

        rows, cols = 4, 5
        gap   = int(min(w, h) * 0.03)
        cell_w = (gx2 - gx1 - gap*(cols-1)) / cols
        cell_h = (gy2 - gy1 - gap*(rows-1)) / rows
        size = int(max(8, min(cell_w, cell_h)))
        rr   = int(size * 0.18)

        total_w = size*cols + gap*(cols-1)
        total_h = size*rows + gap*(rows-1)
        ox = gx1 + (gx2 - gx1 - total_w)/2
        oy = gy1 + (gy2 - gy1 - total_h)/2

        for r_i in range(rows):
            for c_i in range(cols):
                sx1 = int(ox + c_i*(size+gap))
                sy1 = int(oy + r_i*(size+gap))
                sx2 = sx1 + size
                sy2 = sy1 + size
                round_rect(c, sx1, sy1, sx2, sy2, rr,
                           fill=self.C_TILE, outline=self.C_TILE_ST)

    def _on_canvas_resize(self, _event):
        self.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

