# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/directive_engine.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-14
# VERSION:	10.03.07
# PURPOSE:  The single consumer of the buffers and the sole operator that mutates User-Interface-observable state

class DirectiveEngine:
    def __init__(self, app_state):
        self.app = app_state
        # ensure baseline fields exist; do not add behavior
        if not hasattr(self.app, "hanus_attention"):
            self.app.hanus_attention = 0
        if not hasattr(self.app, "view_dirty"):
            self.app.view_dirty = True
        if not hasattr(self.app, "running"):
            self.app.running = True
        
        self.Syst = flmnt_ssid[-1]
        self.HID = self.Syst.mbrObjs[0]
        self.HOD = self.Syst.mbrObjs[1]
        self.TRSV = self.Syst.mbrObjs[2]
        self.Workflow = self.Syst.mbrObjs[3]
        self.Profile = self.Syst.mbrObjs[4]
        self.Archive = self.Syst.mbrObjs[5]
        self.Analysis = self.Syst.mbrObjs[6]
        self.Calendar = self.Syst.mbrObjs[7]
        self.Meta = self.Syst.mbrObjs[8]
        
        self.Syst.ui_handle([-2, -3,-4, -5, -6, -7, -8, -9, -10])
        self.HID.ui_handle([-11, -12, -13, -14])
        self.HOD.ui_handle([-15, -16])
        self.TRSV.ui_handle([-17, -18, -19, -20])
        self.Workflow.ui_handle(['Address', 'Parcels', 'Plots', 'Contracts', 'Animals', 'Inventory', 'Catalog', 'Schedule', 'USDA_grw'])
        self.Profile.ui_handle(['HERE'])
        self.Archive.ui_handle(['HERE'])
        self.Analysis.ui_handle(['HERE'])
        self.Calendar.ui_handle(['HERE'])
        self.Meta.ui_handle(['HERE'])
        
        self.ui_tree = [self.Syst, self.HID, self.HOD, self.TRSV, self.Workflow, self.Profile, self.Archive, self.Analysis, self.Calendar, self.Meta]
        # Its Important to have these separate forms of the DnmcDtm instances here, because they are the only instances the have assigned value for their mbrObjs attributes
        # This allows for the Directive Engine logic (and future logic) to handle the data under the assumption that the data resides in a standardized convention that has these ambiguous objects in the same place, at the end of the file. Despite being made up of different contents.
        # This also allows for the Directive Engine to contain methods that more easily access these user-interface tailored objects for consistent user interfacing, with only minimally knowing how the objects will exist/ there contents
        
        self.StafulUi_focus = self.ui_tree[getattr(self.app, "hanus_attention", 0);     # The current DnmcDtm instance that the user is on# Add logic later
    
    # ------------------------------------------------------------
    # Primary input handler — called for each HID submission
    # ------------------------------------------------------------
    def directive(self, datum: bytes):
        text = datum.decode("utf-8", errors="ignore").strip().lower()

        # --- Some logic is left intentionally ambiguous for later development ---
        if self.app.running 
            # --- Quit commands ---
            if (text == "q") or (text == "quit"):
                self.app.running = False
                root = getattr(self.app, "root", None)
                if root is not None:
                    try:
                        root.quit()
                    except Exception:
                        pass
                return
            elif getattr(self.app, "hanus_attention", 0) == 0:
                # --- Enter pressed on startup (hanus_attention == 0) ---
                if (text == ""):
                    self.app.hanus_attention = 1
                    self.app.view_dirty = True
                    return
            elif (0 < getattr(self.app, "hanus_attention", 0)):
                if (text[:4] == "nav"):
                    if (text[5:9] == "bck") and 2 <= getattr(self.app, 'hanus_attention', 0): # Cant move back if at 1
                        # Add logic later
                        self.app.hanus_attention_flag = True
                        return
                    elif (text[5:9] == "twd") and getattr(self.app, 'perused_focus', None) is not None: # Cant move in if no item is selected
                        # Add logic later
                        self.app.perused_focus = None
                        self.app.peruse_flag = False
                        self.app.hanus_attention_flag = True
                        return
                    return
                if (text[:4] == "inv"):
                    if (int(text[5:9]) <= len(self.StafulUi_children)):
                        self.perused_focus = int(text[5:9])
                        self.app.peruse_flag = True
                        return
                    if 0 in text[5:9] == "esc"):
                        self.app.perused_focus = None
                        self.app.peruse_flag = False
                        return
                    return
                if (text[:4] == "med"):
                    # Add logic later
                    return
                if (text[:4] == "man"):
                    # Add logic later
                    return
        
        return

    # ------------------------------------------------------------
    # Background / daemon events — intentionally no-op
    # ------------------------------------------------------------
    def daemon(self, datum: bytes):
        # Reserved for NET / PRI handling
        return
