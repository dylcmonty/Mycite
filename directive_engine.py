# Copyright 2025 Dylan Montgomery
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/directive_engine.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-10-07
# VERSION:	10.02.05
# PURPOSE:  HERE

class UIObject(ui_elem, ui_mbrs):
    self.object_id = ui_elem
    
    self.mbrObj = ui_mbrs

Syst = UIObject(flmnt_ssid[-1], [flmnt_ssid[-2], flmnt_ssid[-3], flmnt_ssid[-4], flmnt_ssid[-5], flmnt_ssid[-6], flmnt_ssid[-7], flmnt_ssid[-8], flmnt_ssid[-9], flmnt_ssid[-10]])

HID = UIObject(Syst.mbrObj[0], [flmnt_ssid[-11], flmnt_ssid[-12], flmnt_ssid[-13], flmnt_ssid[-14]])
HOD = UIObject(Syst.mbrObj[1], [flmnt_ssid[-15], flmnt_ssid[-16]])
TRSV = UIObject(Syst.mbrObj[2], [flmnt_ssid[-17], flmnt_ssid[-18], flmnt_ssid[-19], flmnt_ssid[-20]])

Profile = UIObject(flmnt_ssid[3], 
[flmnt_ssid['Address'], [flmnt_ssid['Parcels'], [flmnt_ssid['Plots'], [flmnt_ssid['Contracts'], [flmnt_ssid['Animals'], [flmnt_ssid['Inventory'], 
[flmnt_ssid['Catalog'], [flmnt_ssid['Schedule'], [flmnt_ssid['USDA_grw']])

Workflow = UIObject(Syst.mbrObj[4], [flmnt_ssid['#'], ...])
Archive = UIObject(Syst.mbrObj[5], [flmnt_ssid['#'], ...])
Analysis = UIObject(Syst.mbrObj[6], [flmnt_ssid['#'], ...])
Calendar = UIObject(Syst.mbrObj[7], [flmnt_ssid['#'], ...])
Meta = UIObject(Syst.mbrObj[8], [flmnt_ssid['#'], ...])

class DirectiveEngine(AppState):    
    def directive(self, item):
        pass
    def daemon(self, item):
        pass

