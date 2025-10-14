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
# MODIFIED:	2025-10-14
# VERSION:	10.03.07
# PURPOSE:  HERE

import threading
import time
from MSS_convention import MSS
from directive_engine import DirectiveEngine
from sockets.portal_ui import Portal

class AppState:
    def __init__(self):      
        self.running = True
        
        self.mss_systm = MSS() if 'MSS' in globals() and MSS else None
        if self.mss_systm:
            try:
                self.mss_systm.boot()
                self.mss_systm.boot_load()
                self.objects = getattr(self.mss_systm, 'flmnt_ssid', None)
                self.obj_tree = getattr(self.mss_systm, 'self.ssid_g', None)
            except Exception:
                self.objects = None
        else:
            self.objects = None

        self.hid_flag, self.net_flag, self.pri_flag = False

        self.hid_buffer, self.net_buffer, self.pri_buffer: list[bytes] = []
        
        if getattr(self.app, "view_dirty", False) or cdzm_changed:
            self._raise_from_state()
            self.app.view_dirty = False
        
        self.cdzm[1] = [0]; 
        self.cdfcs[1] = [0]; 
        self.cdslct[1] = [0]; 
        self.tm = None
        
        self.director = DirectiveEngine(self)

    def enqueue_hid(self, datum: bytes) -> None:
        """Append to the HID buffer and raise the HID flag if it was empty."""
        was_empty = not self.hid_buffer
        self.hid_buffer.append(datum)
        if was_empty:
            self.hid_flag = True

    def enqueue_net(self, datum: bytes) -> None:
        """Append to the NET buffer and raise the NET flag if it was empty."""
        was_empty = not self.net_buffer
        self.net_buffer.append(datum)
        if was_empty:
            self.net_flag = True

    def enqueue_pri(self, datum: bytes) -> None:
        """Append to the PRI buffer and raise the PRI flag if it was empty."""
        was_empty = not self.pri_buffer
        self.pri_buffer.append(datum)
        if was_empty:
            self.pri_flag = True
    
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
