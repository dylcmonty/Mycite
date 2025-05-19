# mycite_project/boot.py
# AUTHOR:   Dylan Montgomery
# MODIFIED: 2025-05-18
# VERSION:  6.02
# PURPOSE:  Read the world.bin file to initialize the main program and socket information etc. 
# NOTE:     HERE
    # NIMM args are folllowed by: NULL - IDK
        # Fetch     Navigate                (cd)
        # Decode    Investigate (Inspect)   (ls)
        # Execute   Mediate                 (RUN)
        # Store     Manipulate              (update from IRIS output)
##############
####
##
#

def bootLoad(RunTimeHMS): # capture, conventGrps, contextLgr, conventMS
    # 1) Load and unpack bits
    with open('world.bin', 'rb') as f:
            raw = f.read()
    for byte in raw:
        for bitpos in range(7, -1, -1):
            RunTimeHMS.capture.append((byte >> bitpos) & 1)
    
    # 2) Prepare the groups and state
    conventMS   = {grp: []   for grp in conventGrps} # Maybe create global task for schema
    contextLgr  = {grp: False for grp in conventGrps} # Possibly start here for first IRIS
    
    # 3) Parse the capture into groups
    for grp in conventGrps:
        if not contextLgr[grp]:
            for i # Condition to meet to denote how many iteration until indexA has finished
                #Logic to figure out later here and assign 'length' a value
            #length = determine_length_for(grp)
            conventMS[grp]  = RunTimeHMS.capture[:length]
            contextLgr[grp] = True

#
##
####
################
####
##
#

import threading
from queue import Queue

def bootStrap():
    class InputSocket:
        def __init__(self, name):
            self.name = name
            self.buffer = Queue()
            self.thread = threading.Thread(target=self.listen, daemon=True)
            self.thread.start()
        
        def listen(self):
            while True:
                data = read_input_data_somehow()
                self.buffer.put(data)
    
    class OutputSocket:
        def __init__(self, name):
            self.name = name
            
        def send(self, data)
            draw_to_display(data)   #Make both classes ambiguous beyond input and output

#
##
####
################
####
##
#

RudiGrp = ["phnmR", "Alice", "Bob", "Carol", "Dave"]

# enumerate(names, 1) yields (1,"Alice"), (2,"Bob"), …
numbered = { i: rudi for i, rdui in enumerate(RudiGrp, 1) }

#Convention creates some number of instances of a given rudi to create a system
phnmSyst    = [LIPpos, JAWpos, TONGUEpos, TONGUEman, TONGUEshp, MOUTHloc, NASAL, THROAT] # 8 instances

#
##
####
################
####
##
#

def harmoicDev  #Zeckendorf notation of value
    #Logic here
    return

def jumpset     #Pingala notation of value
    #Logic here
    return

plSyst      = [POS, NEG]
eqSyst      = [True, False]

natureSyst  = [polarity, cardinal, natural, ratio,]

crdnlSyst   = [up, down, back front, weird, strange]
rltnSyst    = [subject, origin, nature, truth, frequency, magnitude, ]

wavesyst    = [frequency, magnitude]

#
##
####
################
