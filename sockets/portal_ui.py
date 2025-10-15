# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/portal_ui.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-14
# VERSION:	10.03.07
# PURPOSE:  Builds a top‑level window with two areas: a view area and a command‑line area. The command line stays hidden until the user presses Enter on the startup screen. Once shown, it’s permanently docked at the bottom, and each line the user enters is passed back to the application via app_state.enqueue.

import tkinter as tk
from typing import Optional
from command_line import CommandLine

class ImageSlot(tk.Frame):
    """A single, self-contained image view (Label + PhotoImage held)."""
    def __init__(self, parent: tk.Widget, img_path: str | None):
        super().__init__(parent, bg="#000000")
        self._photo: Optional[tk.PhotoImage] = None  # keep a ref to avoid GC
        lbl = tk.Label(self, bd=0, highlightthickness=0, bg="#000000")
        lbl.pack(fill="both", expand=True)
        if img_path:
            try:
                self._photo = tk.PhotoImage(file=img_path)
                lbl.configure(image=self._photo)
            except Exception:
                # simple fallback if a file is missing/bad
                lbl.configure(text=f"[missing image]\n{img_path or ''}",
                              fg="#dddddd", bg="#222222", font=("Courier New", 14))
class ViewDeck(tk.Frame):
    """Holds exactly 5 ImageSlots and can raise one by index."""
    def __init__(self, parent: tk.Widget, img_paths: list[str | None]):
        super().__init__(parent, bg="#000000")
        # normalize to exactly 5 entries
        paths = (list(img_paths) + [None]*5)[:5]
        self.slots: list[ImageSlot] = []
        for p in paths:
            slot = ImageSlot(self, p)
            # stack them all; we’ll tkraise the active one
            slot.place(x=0, y=0, relwidth=1.0, relheight=1.0)
            self.slots.append(slot)
        self._current = None

    def show(self, idx: int):
        if not (0 <= idx < len(self.slots)):
            idx = 0
        if idx != self._current:
            self.slots[idx].tkraise()
            self._current = idx

class Portal:
    def __init__(self, app_state, title="Input", geometry="1100x700", poll_ms=100):
        self.app = app_state
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)

        # --- Top (view deck) ---
        top = tk.Frame(self.root, bg="#000000")
        top.pack(side="top", fill="both", expand=True)

        # resolve image paths: prefer app_state.bg_paths else defaults
        paths = getattr(self.app, "bg_paths", [
            "assets/imgs/view0.PNG",
            "assets/imgs/view1.PNG",
            "assets/imgs/view2.PNG",
            "assets/imgs/view3.PNG",
            "assets/imgs/view4.PNG",
        ])
        self.deck = ViewDeck(top, paths)
        self.deck.pack(fill="both", expand=True)

        # --- Bottom (command line: always visible) ---
        bottom = tk.Frame(self.root)
        bottom.pack(side="bottom", fill="x")

        def on_submit(text: str):
            # HID socket: forward raw bytes; DirectiveEngine consumes it
            self.app.enqueue_hid(text.encode("utf-8"))

        self.cmd = CommandLine(
            bottom, on_submit=on_submit,
            font=("Courier New", 12),
            relief="sunken", bd=1,
        )
        self.cmd.pack(side="left", fill="x", expand=True, padx=8, pady=8)
        self.root.after(0, self.cmd.focus_set)  # keep focus on cmd

        # --- Polling (same timing model as your command loop) ---
        self._poll_ms = poll_ms
        self._last_hanus_attention = None
        # for “timed like the cmd loop”: also watch the same flags you use
        self._last_flags = False
        self.root.after(self._poll_ms, self._tick)

        # Initial paint
        self._raise_from_state(force=True)

    # ---- internal helpers ----
    def _raise_from_state(self, force=False):
        # read hanus_attention robustly
        try:
            idx = int(getattr(self.app, "hanus_attention", 0))
        except Exception:
            idx = 0
        if force or idx != self._last_hanus_attention:
            self.deck.show(idx)
            self._last_hanus_attention = idx

    def _tick(self):
        # Observe the same “timing” as your command loop:
        # only react when new work is present or state changed.
        flags = getattr(self.app, "hid_flag", False)
        if flags != self._last_flags:
            # flags changed -> the engine likely just processed something
            self._raise_from_state(force=False)
            self._last_flags = flags
        else:
            # also catch direct hanus_attention changes (if engine flips hanus_attention & view_dirty)
            self._raise_from_state(force=False)

        self.root.after(self._poll_ms, self._tick)

    def start(self):
        self.root.mainloop()
