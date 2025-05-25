# Copyright [2025] [Dylan Montgomery]
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/boot.py
# AUTHOR:   Dylan Montgomery
# MODIFIED: 2025-05-25
# VERSION:  6.04.01
# PURPOSE:  Load & initialize the main program and socket information etc. 
# NOTE:
        # Fetch     Navigate                (cd)
        # Decode    Investigate (Inspect)   (ls)
        # Execute   Mediate                 (RUN)
        # Store     Manipulate              (update from IRIS output)
    # Assuming the bytes are called in MSB-First (MSB in position 0)
    # We want to store each byte sequentially by first reversing its order; then we will have an order array
################################################################################################################################################################################################################################################################
################
####
##
#
def bootLoad(app_state):
    # 1) Load and unpack bits
    with open('world.bin', 'rb') as f:
            raw = f.read()
    for byte in raw:
        for bitpos in range(7, -1, -1):
            app_state.capture.append((byte >> bitpos) & 1)
    
    # 2) Prepare the groups and state
    conventMS   = {grp: []   for grp in conventGrps} # Maybe create global task for schema
    
    
    # 3) Parse the capture into groups
    for grp in conventGrps:
        while #Iterative loop logic until finished
            for i #Iterative loop to access and count i
                # Condition to meet to denote how many iteration until each index has finished
        conventMS[grp]  = app_state.capture[i:length]

def bootStrap():
    

#
##
####
################
################################################################################################################################################################################################################################################################

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
