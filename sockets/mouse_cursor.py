# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/sockets/mouse_cursor.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-18
# VERSION:	10.03.09
# PURPOSE:  Minimal mouse/cursor input module (no UI widgets created here). Binds left/right clicks on a provided widget and forwards (x, y) to callbacks.
# NOTE:     Does not create any widgets.
#           Binds left-click and right-click to the given parent widget.
#           Calls the provided callbacks with (x, y) in widget coordinates.
#           Provides enable()/disable()/destroy() to control bindings.
#           Right-click can be Button-3 on most platforms; Button-2 is also commonly used on some systems. We bind both to be safe.

from __future__ import annotations
from typing import Callable, Optional

try:
    import tkinter as tk
except Exception:
    # Allow import in non-GUI contexts without failing immediately
    tk = None  # type: ignore


class MsCrsr:
    def __init__(
        self,
        parent_widget,
        on_left: Optional[Callable[[int, int], None]] = None,
        on_right: Optional[Callable[[int, int], None]] = None,
    ):
        self.parent = parent_widget
        self.on_left = on_left
        self.on_right = on_right

        # Keep track of current bindings so we can unbind if needed.
        self._enabled = False
        self._bind_ids = []  # list of (sequence, funcid) for cleanup

        self.enable()

    # ----------------------
    # Public control methods
    # ----------------------
    def enable(self) -> None:
        if self._enabled or self.parent is None:
            return
        self._enabled = True

        # Left click
        funcid = self.parent.bind("<Button-1>", self._handle_left, add="+")
        self._bind_ids.append(("<Button-1>", funcid))

        # Right click (common mapping)
        funcid = self.parent.bind("<Button-3>", self._handle_right, add="+")
        self._bind_ids.append(("<Button-3>", funcid))

        # Alternate “right” on some systems
        funcid = self.parent.bind("<Button-2>", self._handle_right, add="+")
        self._bind_ids.append(("<Button-2>", funcid))

    def disable(self) -> None:
        if not self._enabled or self.parent is None:
            return
        # Unbind all sequences we attached
        for sequence, funcid in self._bind_ids:
            try:
                self.parent.unbind(sequence, funcid)
            except Exception:
                pass
        self._bind_ids.clear()
        self._enabled = False

    def destroy(self) -> None:
        """Disable and drop references."""
        self.disable()
        self.on_left = None
        self.on_right = None
        self.parent = None

    # ----------------------
    # Internal event handlers
    # ----------------------
    def _handle_left(self, event) -> str | None:
        if self.on_left is not None:
            try:
                x, y = int(event.x), int(event.y)
            except Exception:
                return None
            self.on_left(x, y)
            # We return None to allow other handlers to run if any.
        return None

    def _handle_right(self, event) -> str | None:
        if self.on_right is not None:
            try:
                x, y = int(event.x), int(event.y)
            except Exception:
                return None
            self.on_right(x, y)
        return None

