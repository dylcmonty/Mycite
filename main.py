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
# MODIFIED:	2025-09-26
# VERSION:	9.03.04
# PURPOSE:  HERE

import threading
import queue
import time
import MSS_convention
from datetime import datetime

class AppState:
    def __init__(self):
        self.mss_systm = MSS()
        
        self.running = True
        self.hid_flag = False
        self.net_flag = False
        self.peri_flag = False

        self.hid_buffer: list[tuple[bytes, datetime]] = []
        self.net_buffer: list[tuple[bytes, datetime]] = []
        self.peri_buffer: list[tuple[bytes, datetime]] = []
        
        self.mss_systm.boot()
        self.mss_systm.boot_load()
        self.objects = self.mss_systm.COMB_filament
        
        self.cdzm = [0]
        self.cdfcs = [0]
        self.cdslct = [0]
        self.tm = None  # 
    
    def directive(self, item):
        pass
    def daemon(self, item):
        pass
        
    def _select(self, kind: str):
        # kind ∈ {'hid','net','peri'}
        if kind == 'hid':  return self.hid_buffer, 'hid_flag'
        if kind == 'net':  return self.net_buffer, 'net_flag'
        if kind == 'peri': return self.peri_buffer, 'peri_flag'
        raise ValueError(f"unknown buffer kind: {kind}")
    def enqueue(self, kind: str, datum: bytes, ts: datetime | None = None):
        buf, flag_name = self._select(kind)
        was_empty = (len(buf) == 0)
        buf.append((datum, ts or datetime.utcnow()))
        if was_empty:
            setattr(self, flag_name, True)   # first item flips flag on
    def try_dequeue(self, kind: str):
        buf, flag_name = self._select(kind)
        if not buf:
            return None
        item = buf.pop(0)
        if not buf:
            setattr(self, flag_name, False)  # drained → flag off
        return item
    # TODO: Setup sockets, peripheral processes, and intention handlers here
    
    def main_loop(self, sleep_s: float = 0.01):
        while self.running:
            # HID isolation
            if self.hid_flag:
                while self.hid_flag and self.running:
                    item = self.try_dequeue('hid')
                    if item is not None:
                        self.directive(item)
                    else:
                        time.sleep(sleep_s)
                continue  # restart outer loop after HID isolation
            # One-shot checks for NET/PERI
            if self.net_flag:
                item = self.try_dequeue('net')
                if item is not None:
                    self.daemon(item)
            if self.peri_flag:
                item = self.try_dequeue('peri')
                if item is not None:
                    self.daemon(item)
            time.sleep(sleep_s)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PortMaster(AppState):
    def __init__(self):
        super().__init__()
    def main_loop(self):
    # TODO: Asynchronously listen to hardware sockets and put datums into the corresponding buffer queue
    # When a datum is added to the queue, the respective flag should be made true
        # Pseudocode placeholders – keep them commented to avoid syntax errors
        # if <HID condition>:
        #     self.enqueue('hid', datum)
        # if <NET condition>:
        #     self.enqueue('net', datum)
        # if <PERI condition>:
        #     self.enqueue('peri', datum)
        pass

    def get_queue(buffer: list, flag):
        if buffer:
            item = buffer.pop(0)
            return item, (len(buffer) == 0)
        # TODO: If popping from buffer, leaves the buffer empty, then set the respective flag to false
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    runtime_app = AppState();
    runtime_app.boot();
    runtime_app.boot_load();

    runtime_app.main_loop();

if __name__ == '__main__':
    main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
