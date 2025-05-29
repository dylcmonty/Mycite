# ControlGate Framework

## Overview

The ControlGate Framework is a modular, Python-based architecture designed to manage dynamic attention, intention, and state across interactive systems.
It is inspired by biological metaphors (Tree, Mycelium, Environment) and enables coordinated processing of user inputs, system states, and network events.

This framework allows:
- Modular integration of human, device, and network inputs
- Intent-driven updates to system state and visual representation
- Asynchronous-synchronous orchestration of internal flows

It can evolve into a real-time control system, database navigator, or live intelligent visualization platform.

---

## Project Layout

- /ProjectFolder
- ├── main.py          # Entry point script - only if needed
- ├── boot.py          # Logic modules: classes, functions, utilities, etc.
- ├── README.md        # This file
- ├── OperatingSystem/ # Specialized directory
- ├── Hardware/        # Specialized directory
- └── assets/          # Optional specialized module directory with init.py to group modules in packages
  - ├── bloom/         # Ambiguouse Design devision lgoic to visualize Control Gate view feild
  - ├── hyphae/        # Input command line abstaction modeule
  - └── KatBots/       # Aplication tool module

---

## Core Components

### AppState
The central brain managing:
- What’s currently focused (attention)
- What’s visible or active (view)
- What relationships or context are linked (earshot, archetypes)
- What intentions or actions are queued for processing

It synchronizes all live system state.

### Peripheral Processes
These are modular input and output modules:
- StateReadIn → Handles human/device input (keyboard, mouse, sensors)
- StateReadOut → Drives human/device outputs (visual display, feedback)
- MyciteReadIn → Captures network or external system input
- MyciteReadOut → Pushes system state or results outward

Each runs asynchronously, feeding or consuming data for the core system.

### Intention Handler
This interpretive layer:
- Classifies raw events into four intention types:
    - Navigation → Moving focus or scope
    - Investigation → Querying internal structure
    - Manipulation → Changing data or state
    - Mediation → Coordinating across boundaries
- Dispatches intentions to modify AppState
- Keeps the system’s meaning clear despite multiple asynchronous signals

### The Main Loop
The synchronous heartbeat:
- Processes queued intentions
- Recalculates the view, state, or outputs
- Drives visual or external updates (e.g., via Pygame or network)

---

## How It Works

1. `bootLoad()` Loads system memory (e.g., from .bin files) and unpacks binary data.
2. `bootStrap()` Initializes logical groups, sets up socket listeners, prepares peripheral modules.
3. `main.py` Creates AppState, launches the synchronous main loop.
4. Peripheral Processes: Asynchronously detect inputs or required outputs, adding updates to system buffers.
5. Intention Handler: Reads peripheral signals, classifies them, and updates AppState.
6. StateReadOut: Pushes updated visuals, states, or outputs to the user or external systems.

---

## Extensibility Plan
The system is structured to support:

- Adding new input devices or sensor streams
- Supporting HTTP/WebSocket/network protocols (e.g., DNS, BitTorrent)
- Building custom archetype modules for specialized behavior
- Integrating advanced visual/audio interfaces with Pygame or similar libraries
- Supporting multimodal user interaction (navigation, manipulation, mediation)

---

## Development Roadmap
- Define one working end-to-end input-to-output flow
- Integrate intention handler for interpreting and routing actions
- Expand peripheral modules (read-in, read-out, network)
- Tighten metaphor-to-data mapping (attention, intention, archetype)
- Add modular plugin architecture for easy future extensions
- Implement logging, diagnostics, and testing scaffolds

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows modification, redistribution, and commercial use with attribution.

---

## Acknowledgments

Built and authored by Dylan Montgomery  
Version: 6.04.05  
Status: Active prototyping and architectural refinement
