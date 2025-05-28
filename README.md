# ControlGate Framework

## Overview

This project is a modular Python-based environment designed to model and manage dynamic attention systems using socket-driven input/output, visual control fields, and evolving system state. It is designed to function as a simulation and control environment capable of integrating multiple input modalities (HID, network, sensor), visual representation systems (Pygame), and eventual expansions into protocol-based communication (e.g. HTTP, DNS, BitTorrent).

The architecture is based on a central runtime object (`AppState`) and a perception-action framework controlled by a `ControlGate` object with a visual `view` matrix and intention buffer. The code is designed for extensibility and experiment-based control simulations.

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
Holds the active runtime state of the application. Includes:
- Captured binary stream
- Socket registry
- Entity tracking
- ControlGate instance

### ControlGate
Manages the perception field:
- `attention` (field, focus)
- `view` matrix: a 2D space into which `Entity.id`s can be bloomed
- `intention`, `chronological`, and `archetype` states
- Future methods like `AITA()` to synthesize and interpret data

### Entity
Each object or agent that can be "bloomed" into the visual field. Identified by a unique `id`.

### Socket
Threaded I/O object capable of safely managing asynchronous data exchange using Python’s `queue.Queue`. Supports general-purpose input and output logic, decoupled from specific protocols.

### GameState
Initializes Pygame window and manages frame updates. Reads from a `display` socket buffer to drive visualization.

---

## How It Works

1. `bootLoad()` loads binary input from a `.bin` file and unpacks it into a bitstream.
2. `bootStrap()` initializes logical groups and sets up any required socket configurations or handlers.
3. `main.py` launches the game window, loads system memory, and starts the main application loop.
4. A function like `bloom()` writes `Entity.id` values into matrix positions in the `ControlGate.view`.
5. Data from input sockets are routed through asynchronous listeners into queues and processed via `process()` (to be defined).
6. Display sockets feed the screen with content for real-time visualization of internal state.

---

## Extensibility Plan

The system is structured to support:

- **HTTP or WebSocket communication**  
- **Modular plugin handlers for protocols** (BitTorrent, DNS, etc.)  
- **Graphical or auditory output devices**
- **Multimodal input** (mouse, keyboard, custom sensors)
- **Custom entity processing pipelines**

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows modification, redistribution, and commercial use with attribution.

---

## Acknowledgments

Built and authored by Dylan Montgomery  
Version: 6.04.05  
Status: Active prototyping


