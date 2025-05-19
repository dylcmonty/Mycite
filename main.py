# mycite_project/main.py
# AUTHOR:   Dylan Montgomery
# MODIFIED: 2025-05-18
# VERSION:  6.02
# PURPOSE:  HERE
# Notes:    HERE
    # Assuming the bytes are called in MSB-First (MSB in position 0)
    # We want to store each byte sequentially by first reversing its order; then we will have an order array
################
####
##
#

from collections    import defaultdict
from boot           import bootLoad
from boot           import bootStrap
import time

class HanusModelState:
    def __init__(self):
        self.capture = []
        self.conventGrps = {
            "indexA": [],
            "indexB": [],
            "indexC": [],
            "indexR": [],
            "indexE": [],
            "indexS": [],
            "indexT": [],
        }
        self.sockets = []

def main():
    RunTimeHMS = HanusModelState()
    
    bootLoad(RunTimeHMS)

    # Assigns values to Run Time object including sockets that run Asynchronously upon creation.
        # Asynchronous sockets are considered separate from main loop
    bootStrap(RunTimeHMS)        

    # Create Synchronous main program logic clock cycle
    while True:
        for socket in input_Sockets
            if socket.has_data():
            data = socket.get_data()
            process(data)

#
##
####
################
####
##
#

if __name__ == '__main__':
    main()

#
##
####
################
