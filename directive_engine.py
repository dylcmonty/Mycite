# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/directive_engine.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-18
# VERSION:	10.03.09
# PURPOSE:  The single consumer of the buffers and the sole operator that mutates User-Interface-observable state
# NOTE:     For the user interface attribute:
    # Its Important to have these separate forms of the DnmcDtm instances here, because they are the only instances the have assigned value for their mbrObjs attributes
    # This allows for the Directive Engine logic (and future logic) to handle the data under the assumption that the data resides in a standardized convention that has these ambiguous objects in the same place, at the end of the file. Despite being made up of different contents.
    # This also allows for the Directive Engine to contain methods that more easily access these user-interface tailored objects for consistent user interfacing, with only minimally knowing how the objects will exist/ there contents

class DirectiveEngine:
    def __init__(self, app_state):
        self.app = app_state
        
        self.Syst = self.app.objects[-1]
        self.Syst.ui_handle([-2, -3,-4, -5, -6, -7, -8, -9, -10])
        
        self.HID = self.Syst.mbrObjs[0]
        self.HOD = self.Syst.mbrObjs[1]
        self.TRSV = self.Syst.mbrObjs[2]
        self.Workflow = self.Syst.mbrObjs[3]
        self.Profile = self.Syst.mbrObjs[4]
        self.Archive = self.Syst.mbrObjs[5]
        self.Analysis = self.Syst.mbrObjs[6]
        self.Calendar = self.Syst.mbrObjs[7]
        self.Meta = self.Syst.mbrObjs[8]
        
        self.HID.ui_handle([-11, -12, -13, -14])
        self.HOD.ui_handle([-15, -16])
        self.TRSV.ui_handle([-17, -18, -19, -20])
        self.Workflow.ui_handle(['Address', 'Parcels', 'Plots', 'Contracts', 'Animals', 'Inventory', 'Catalog', 'Schedule', 'USDA_grw'])
        self.Profile.ui_handle(['HERE'])
        self.Archive.ui_handle(['HERE'])
        self.Analysis.ui_handle(['HERE'])
        self.Calendar.ui_handle(['HERE'])
        self.Meta.ui_handle(['HERE'])
        
        self.ui_tree = [self.Syst, self.HID, self.HOD, self.TRSV, self.Workflow, self.Profile, self.Archive, self.Analysis, self.Calendar, self.Meta] # Add more meta data access
        
        # This only helps for the updating logic, and dose not get used for perusal, as investigation is handled by an obj member objects attribute
        self.stafullUi_focus = self.ui_tree[getattr(self.app, "hanus_attention", 0)];
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def arngmntPull(self, text[5:])):
        pos = 6
        while text[pos]) != ","
            pos +=
        
        selectedX = int(text[5:pos])
        selectedY = int(text[(pos + 2):])
        
        DatumRecall = self.stafullUi_focus.mbrObjs[selectedX][selectedY]
        
        # Search for that particular Datum Recall reference in the the first row of self.stafullUi_focus.mbrObjs
        # i.e. for the member objects of the current focus, return the ordinal value with which the referenced member object is found in the first row
        # Assign the ordinal value to a variable called 'memberOrdinalVal'
        
        return memberOrdinalVal
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Some logic is left intentionally ambiguous for later development
    def directive(self, datum: bytes):
        text = datum.decode("utf-8", errors="ignore").strip().lower()

        if self.app.running:
            # Quit commands
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
                # Enter pressed on startup to advance from splash screen
                if (text == ""):
                    self.app.hanus_attention = 1
                    self.app.update_flag = True
                    return
            
            elif (0 < getattr(self.app, "hanus_attention", 0)):
                
                # NAVIGATION COMMANDS
                if (text[:4] == "nav"):
                    if (text[5:9] == "bck") and 2 <= getattr(self.app, 'hanus_attention', 0): # Cant move back if at 1
                        # Add logic later
                        self.app.update_flag = True
                        return
                    elif (text[5:9] == "twd") and getattr(self.app, 'perused_focus', None) is not None: # Cant move in if no item is selected
                        if (0 < getattr(self.app, "hanus_attention", 0) < 5):
                            self.app.hanus_attention = getattr(self.app, "perused_focus", None)
                            self.app.perused_focus = None
                        elif (4 < getattr(self.app, "hanus_attention", 0)):
                            self.app.hanus_attention = 9
                            # Determine the respective value to set perused_focus equal to for Meta data investigation
                        self.app.update_flag = True
                        return
                    return
                # INVESTIGATION COMMANDS
                if (text[:4] == "inv"):
                    if 0 in text[5:9] == "esc"):
                        self.app.perused_focus = None
                        return
                    elif len(int(text[5:])) < len(self.self.stafullUi_focus.mbrObjs)
                        self.perused_focus = int(text[5:]) 
                    else:
                        self.perused_focus = (self.arngmntPull(text[5:]))
                    return
                # MEDIATION COMMANDS
                if (text[:4] == "med"):
                    # Add logic later
                    return
                # MANIPULATION COMMANDS
                if (text[:4] == "man"):
                    # Add logic later
                    return
        
        return

    # Background / daemon events — intentionally no-op
    def daemon(self, datum: bytes):
        # Reserved for NET / PRI handling
        return
