# Copyright [2025] [Dylan Montgomery]
# Licensed under the Apache License, Version 2.0 (the "License");

# mycite_project/MSS_convention.py
# AUTHOR:   Dylan Montgomery
# MODIFIED:	2025-09-26
# VERSION:	9.03.04
# PURPOSE:  HERE
# NOTES:
    # Add to datum objects so that group value is understood, selection of COMB, and magnitude value are denoted.
    # Making sure the COBM can 0 select with a Bit Mask, as well as by ordered value in COMB_arr
    # Develop to enable
        # the adding of datums
        # semi-global reference
        # allow for dynamic user interface use and for dynamic work shopping (outright and by action call)

class dnmc_datum:
    def __init__(self, value=None, parent_layer=None):
        self.value = value
        self.parent_layer = parent_layer


class UI_layer:
    def __init__(self, name, COBM=None):
        self.name = name
        self.COBM = COBM
        self.grpVls = []

    def ensure_group(self, m_index):
        while len(self.grpVls) <= m_index:
            self.grpVls.append([])

    def add_datum(self, m_index, datum_value):
        self.ensure_group(m_index)
        d = dnmc_datum(value=datum_value, parent_layer=self)
        self.grpVls[m_index].append(d)
        return d


class UI_ssid:
    def __init__(self):
        self.layers = []
        self.COMB_filament = []

    @property
    def COBM_arr(self):
        return [layer.COBM for layer in self.layers]

    def reload_build(self, reset=True):
        if not self.layers:
            return 0
        if reset:
            self.COMB_filament = []
        last_layer = self.layers[-1]
        count = 0
        for group in last_layer.grpVls:
            for d in group:
                self.COMB_filament.append(d)
                count += 1
        return count

    def load_from_ssid_s(self, ssid_s, reset=True, cobm_map=None):
        if reset:
            self.layers = []

        def ord_index(key, prefix):
            try:
                return int(key.split(f"{prefix}_", 1)[1])
            except Exception:
                return 10**9

        layer_keys = sorted(
            (k for k in ssid_s.keys() if k.startswith("layer_")),
            key=lambda k: ord_index(k, "layer")
        )

        for li, lkey in enumerate(layer_keys, start=1):
            if callable(cobm_map):
                cobm = cobm_map(lkey, li)
            elif isinstance(cobm_map, dict):
                cobm = cobm_map.get(lkey)
            else:
                cobm = None

            layer = UI_layer(name=lkey, COBM=cobm)
            self.layers.append(layer)

            groups = ssid_s[lkey]
            group_keys = sorted(
                (gk for gk in groups.keys() if gk.startswith("group_")),
                key=lambda gk: ord_index(gk, "group")
            )

            for gi, gkey in enumerate(group_keys, start=1):
                iter_dict = groups[gkey]
                iter_keys = sorted(
                    (ik for ik in iter_dict.keys() if ik.startswith("iteration_")),
                    key=lambda ik: ord_index(ik, "iteration")
                )

                m_index = gi - 1
                for ikey in iter_keys:
                    pair = iter_dict[ikey]
                    layer.add_datum(m_index, datum_value=pair)

        return len(self.layers)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bitInt(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (b & 1)
    return v

def bits_from_str(bitstr: str) -> list[int]:
    return [int(b) for b in bitstr]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MSS():
    def __init__(self):
        self.capture: list[int] = []
        
        self.index_a = []
        self.index_b = []
        self.index_c = []
        
        self.index_d = []
        self.index_g = []
        
        self.index_e = []
        self.index_s = []
        
        self.ssid_g = {}
        
        self.system_ssid = UI_ssid()

    def boot(self):
        with open('world.bin', 'rb') as f:
            raw = f.read()
        for byte in raw:
            for bitpos in range(7, -1, -1):
                self.capture.append((byte >> bitpos) & 1)
        
        n = len(self.capture)
        a_stp = 0

        while a_stp < n and self.capture[a_stp] == 1:
            a_stp += 1
        
        adrs_sz = (len(self.index_a)) - 1
        self.index_a = self.capture[:a_stp]
        self.index_b = self.capture[(a_stp+1):((2*a_stp)+1)]
        self.index_c = self.capture[((2*a_stp)+1):((3*a_stp)+1)]
        self.index_d = self.capture[((3*a_stp)+1):bitInt(self.index_c[:a_stp])]
        self.index_g = self.capture[bitInt(self.index_c[:a_stp]):bitInt(self.index_c[a_stp:(2*a_stp)])]
        self.index_e = self.capture[bitInt(self.index_c[(2*a_stp):(3*a_stp)]):bitInt(self.index_c[(2*a_stp):(3*a_stp)])]
        self.index_s = self.capture[bitInt(self.index_c[(2*a_stp):(3*a_stp)]):]
        
    def compute_index_d_adrss(index_d, adrs_sz):
        index_d_adrss = []
        start = 0
        while start + adrs_sz <= len(index_d):
            stop = start + adrs_sz
            index_d_adrss.append(bitInt(index_d[start:stop]))
            start = stop
        return index_d_adrss

    def compute_index_g_vls(index_g, index_d_adrss):
        index_g_vls = []
        prev = 0
        n = len(index_g)
        for stop in index_d_adrss:
            index_g_vls.append(bitInt(index_g[prev:stop]))
            prev = stop
        index_g_vls.append(bitInt(index_g[prev:n]))  # final slice to end
        return index_g_vls

    def boot_load(self):
        adrs_sz = len(self.index_a) - 1
        index_g_vls   = compute_index_g_vls(self.index_g, index_d_adrss)

        pos = 0
        L = index_g_vls[1]          # Number of layers
        Li = 1  # Current layer
        Gi = 1  # Current group
        L_grps = index_g_vls[Li:L]   # Array of the number of groups for layer 1
        
        for Li <= L_grps:
            for Gi <= index_g_vls[Gi+Li]:
                for 
                Gi += 1
        # iteration counts per group, laid out layer-by-layer
        iter_counts = []
        idx = 0
        for gi in group_counts:
            iter_counts.append(index_g_vls[pos + idx : pos + idx + gi])
            idx += gi
        pos += sum(group_counts)
        
        # fill nested dict: layer_i -> group_m -> iteration_k -> [a,b]
        self.ssid_g = {}
        for layer_idx in range(L):
            layer_key = f"layer_{layer_idx + 1}"
            self.ssid_g[layer_key] = {}
            groups_in_layer = group_counts[layer_idx]
            for group_idx in range(groups_in_layer):
                group_key = f"group_{group_idx + 1}"
                self.ssid_g[layer_key][group_key] = {}
                num_iters = iter_counts[layer_idx][group_idx]
                for iter_idx in range(num_iters):
                    a = index_g_vls[pos]
                    b = index_g_vls[pos + 1]
                    pos += 2
                    iter_key = f"iteration_{iter_idx + 1}"
                    self.ssid_g[layer_key][group_key][iter_key] = [a, b]
    
    layer_keys = [k for k in self.ssid_g.keys() if k.startswith("layer_")]
    if layer_keys:
        last_key = max(layer_keys, key=lambda k: int(k.split("_", 1)[1]))
        last_layer_only = {last_key: self.ssid_g[last_key]}
        self.system_ssid.load_from_ssid_s(last_layer_only, reset=True)
        self.system_ssid.reload_build(reset=True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def boot_strap(self):
        # TODO: Use index_s to handle operations for building and saving new dynamic objects at the UI layer level
        # TODO: Logic to handle COBM
        return ()

