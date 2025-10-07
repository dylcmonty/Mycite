# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/window_renderer.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-07
# VERSION:	10.02.05
# PURPOSE:  HERE

import tkinter as tk
from datetime import datetime
from typing import Optional

class WindowRenderer:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CLASS-LAYOUT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    POLL_MS = 33  # ~30 FPS polling for dequeue/render without blocking Tk

    def __init__(self, parent: tk.Widget, app_state):
        self.app = app_state

        # Public container you can pack/grid from the outside
        self.container = tk.Frame(parent)
        self.container.configure(background="#ffffff")

        # Area where views will be swapped in/out
        self.view_area = tk.Frame(self.container, bg="#ffffff")
        self.view_area.pack(side="top", fill="both", expand=True)

        # Keep last dequeued item, just for demo/status
        self._last_item: Optional[tuple[bytes, datetime]] = None

        # Track current view index to avoid unnecessary redraws
        self._current_view_idx: Optional[int] = None

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PERIODIC-LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def start(self, tk_root: tk.Tk):
        tk_root.after(self.POLL_MS, lambda: self._tick(tk_root))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INTERNAL-HEARTBEAT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _tick(self, tk_root: tk.Tk):
        # Try to consume one item to "inform" rendering. Leave scheduling to AppState.
        item = (
            self.app.try_dequeue("hid")
            or self.app.try_dequeue("net")
            or self.app.try_dequeue("peri")
        )

        if item is not None:
            self._apply_item(item)  # may update app.tm / local state, etc.

        # Decide which view to show (0..3). Minimal policy:
        #   Use app.cdzm[0] % 4, defaulting to 0 if unavailable.
        try:
            view_idx = int(self.app.cdzm[0]) % 4
        except Exception:
            view_idx = 0

        # (Re)render if the view changed or if we just processed a new item.
        if view_idx != self._current_view_idx or item is not None:
            self._render_view(view_idx)
            self._current_view_idx = view_idx

        # Schedule next tick
        tk_root.after(self.POLL_MS, lambda: self._tick(tk_root))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONSUME-ITEMS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _apply_item(self, item: tuple[bytes, datetime]):
        data, ts = item
        self._last_item = item

        # ---- PLACEHOLDER: begin your event-to-state mapping here ----
        # Example sketch (commented; implement your own rules):
        #
        # if data == b"\n":
        #     # maybe advance selection or confirm something
        #     self.app.cdslct[0] = (self.app.cdslct[0] + 1) % 10
        # elif data == b"\x1b":  # ESC
        #     # maybe switch to a different zone/view
        #     self.app.cdzm[0] = (self.app.cdzm[0] + 1) % 4
        # else:
        #     # update a "focus" counter or timestamp
        #     self.app.cdfcs[0] += 1
        #
        # Always safe to store the last time an input influenced the UI:
        self.app.tm = ts
        # ---- PLACEHOLDER: end your event-to-state mapping ----

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RENDERING-VIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _render_view(self, idx: int):
        """
        Swap in the view for idx in [0..3]. Each view has its own placeholder area
        and a block for per-view logic that may mutate aspects of the UI.
        """
        # Clear previous view widgets
        for w in self.view_area.winfo_children():
            w.destroy()

        if idx == 0:
            self._render_view0()
        elif idx == 1:
            self._render_view1()
        elif idx == 2:
            self._render_view2()
        else:
            self._render_view3()

    def _render_view0(self):
        root = tk.Frame(self.view_area, bg="#ffffff")
        root.pack(fill="both", expand=True)

        tk.Label(root, text="View 0", font=("Courier New", 16), bg="#ffffff").pack(
            anchor="w", padx=12, pady=8
        )

        # ---- PLACEHOLDER: per-view-0 logic that may use self.app.cdfcs, cdslct, tm ----
        # e.g., draw a list, highlight selected index = self.app.cdslct[0], etc.
        tk.Label(root, text="[placeholder: view 0 content]", bg="#ffffff").pack(
            anchor="w", padx=16, pady=4
        )

    def _render_view1(self):
        root = tk.Frame(self.view_area, bg="#ffffff")
        root.pack(fill="both", expand=True)

        tk.Label(root, text="View 1", font=("Courier New", 16), bg="#ffffff").pack(
            anchor="w", padx=12, pady=8
        )

        # ---- PLACEHOLDER: per-view-1 logic ----
        tk.Label(root, text="[placeholder: view 1 content]", bg="#ffffff").pack(
            anchor="w", padx=16, pady=4
        )

    def _render_view2(self):
        root = tk.Frame(self.view_area, bg="#ffffff")
        root.pack(fill="both", expand=True)

        tk.Label(root, text="View 2", font=("Courier New", 16), bg="#ffffff").pack(
            anchor="w", padx=12, pady=8
        )

        # ---- PLACEHOLDER: per-view-2 logic ----
        tk.Label(root, text="[placeholder: view 2 content]", bg="#ffffff").pack(
            anchor="w", padx=16, pady=4
        )

    def _render_view3(self):
        root = tk.Frame(self.view_area, bg="#ffffff")
        root.pack(fill="both", expand=True)

        tk.Label(root, text="View 3", font=("Courier New", 16), bg="#ffffff").pack(
            anchor="w", padx=12, pady=8
        )

        # ---- PLACEHOLDER: per-view-3 logic ----
        tk.Label(root, text="[placeholder: view 3 content]", bg="#ffffff").pack(
            anchor="w", padx=16, pady=4
        )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
