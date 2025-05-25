# Copyright [2025] [Dylan Montgomery]
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# mycite_project/main.py
# AUTHOR:   Dylan Montgomery
# MODIFIED: 2025-05-25
# VERSION:  6.04.01
# PURPOSE:  HERE
# Notes:    HERE
import threading
import time
import pygame
from collections    import defaultdict
from boot           import bootLoad
from boot           import bootStrap
################################################################################################################################################################################################################################################################
################
####
##
#
class AppState:
    def __init__(self):
        self.capture = []
        self.conventGrps = {"indexA": [], "indexB": [], "indexC": [], "indexR": [], "indexE": [], "indexS": [], "indexT": []}
        self.sockets = []           # List of Socket instances
        self.running = True         # Main loop control flag
        self.AITA = []              # Holds the current context, including visual state
    def log_socket(self, socket):
        self.sockets.append(socket)
    def stop(self):
        self.running = False
    def main_loop(self):
        # Add Logic to define what is an input socket
        while self.running:
            for socket in self.sockets: # Loops over inputs
                subject = socket.read()
                # Add logic to use input and execute output in context with:
                    # AITA
                    # NIMM

class Socket:
    def __init__(self, name):
        self.name = name
        self.id = socket_id
        self.buffer = []
        self.queue = []
        self.running = True
        self.thread = threading.Thread(target=self.asynch_loop, daemon=True)
        self.thread.start()
    def read(self):
        if self.buffer:
            return self.buffer.pop(0)
        return None
    def write(self, data):
        self.queue.append(data)
        pass
    def asynch_loop(self):
        while self.running:
            if self.queue:
                self.buffer.append(process(self.queue.pop(0)))
            return None

#
##
####
################
################################################################################################################################################################################################################################################################
def main():
    app_state = AppState() 
    bootLoad(app_state)
    # Assigns values to Run Time App State and create sockets
    bootStrap(app_state)
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    # Necessary: creates the window or screen surface
    clock = pygame.time.Clock()
    running = True
    
    while running:
        data = display.read_data()
        if data:
            # Do something with the processed display data
            update_screen_with(data)

        # Update Pygame display
        draw_screen(screen)
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()

