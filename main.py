# Copyright 2025 Dylan Montgomery
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
# MODIFIED:	2025-10-07
# VERSION:	10.02.05
# PURPOSE:  HERE

import threading
import queue
import time
from MSS_convention import MSS
from sockets.portal_ui import Portal
from directive_engine import Director

class AppState:
    def __init__(self):
        self.mss_systm = MSS()
        
        self.running = True
        self.hid_flag, self.net_flag, self.pri_flag = False

        self.hid_buffer, self.net_buffer, self.pri_buffer: list[tuple[bytes, datetime]] = []
        
        self.mss_systm.boot()
        self.mss_systm.boot_load()
        self.objects = self.mss_systm.flmnt_ssid
        
        self.cdzm = [0]; self.cdfcs = [0]; self.cdslct = [0]; self.tm = None
        self.obj_tree = self.ssid_g
        
        self.director = DirectiveEngine(self)

    def enqueue(self, kind: str, datum: bytes, ts: datetime | None = None):
        buf, flag_name = self._select(kind)
        was_empty = (len(buf) == 0)
        buf.append((datum, ts or datetime.utcnow()))
        if was_empty:
            setattr(self, flag_name, True)   # first item flips flag on
    
    def main_loop(self, sleep_s: float = 0.01):
        while self.running:
            # HID isolation
            if self.hid_flag:
                while self.hid_flag and self.running:
                    self.director.directive(self.hid_buffer.pop(0), self.cdzm, )
                time.sleep(sleep_s)
                continue  # restart outer loop after HID isolation
            # One-shot checks for NET/PRI
            if self.net_flag:
                self.director.daemon((self.net_buffer.pop(0)), ())
            if self.pri_flag:
                self.director.daemon(((self.pri_buffer.pop(0)), ())
            time.sleep(sleep_s)

def main():
    app = AppState();
    
    # Run the scheduler loop on a worker thread
    t = threading.Thread(target=app.main_loop, daemon=True)
    t.start()
    
    # Start the user interface window on the mainthread
    ui = Portal(app_state=app, title="Control Gate")
    ui.start()

if __name__ == '__main__':
    main()
