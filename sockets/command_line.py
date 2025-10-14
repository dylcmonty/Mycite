# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/command_line.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-14
# VERSION:	10.03.07
# PURPOSE:  A single‑line terminal. It exposes an on_submit callback, inserts a placeholder when idle, and calls on_submit on <Return>. This class is self‑contained and doesn't interact with any window‑rendering logic.

import tkinter as tk

IDLE_TEXT = "/ENTER COMMAND OR 'Q' TO QUIT"

class CommandLine(tk.Entry):
    """
    Single-line command field with idle placeholder.
    Calls on_submit(text) on <Return>. If text == 'q', quits the toplevel.
    """
    def __init__(self, master, on_submit, idle_text=IDLE_TEXT, **kw):
        super().__init__(master, **kw)
        self.on_submit = on_submit
        self.idle_text = idle_text
        self._showing_idle = False

        self._fg_idle = "#888888"
        self._fg_active = kw.get("fg", "#000000")

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<KeyRelease>", self._on_key_release)
        self.bind("<Return>", self._on_return)
        self.bind("<Escape>", self._on_escape)

        self._set_idle()

    # --- idle/placeholder helpers ---
    def _set_idle(self):
        self._showing_idle = True
        self.config(fg=self._fg_idle)
        self.delete(0, tk.END)
        self.insert(0, self.idle_text)
        self.icursor(tk.END)

    def _clear_if_idle(self):
        if self._showing_idle:
            self._showing_idle = False
            self.config(fg=self._fg_active)
            self.delete(0, tk.END)

    # --- event handlers ---
    def _on_focus_in(self, _e):
        if self._showing_idle:
            self.icursor(tk.END)

    def _on_focus_out(self, _e):
        if not self.get() or self._showing_idle:
            self._set_idle()

    def _on_key_release(self, e):
        if self._showing_idle and e.keysym not in ("Shift_L", "Shift_R"):
            if self.get() == self.idle_text:
                self._clear_if_idle()
        if not self.get():
            self._set_idle()

    def _on_escape(self, _e):
        self._set_idle()
        return "break"

    def _on_return(self, _e):
        text = self.get()
        if self._showing_idle or not text:
            return "break"
        if text.strip().lower() == "q":
            self.winfo_toplevel().quit()
            return "break"
        self.on_submit(text)
        self._set_idle()
        return "break"
