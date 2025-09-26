# Mycite Framework

## Overview
The Mycite Framework is a control system and data handling skeleton built to support extensible software and data environments through semantic coordination. It reflects a design principle where automation and smart systems remain interpretable and controllable by their users—not through oversimplification, but through a unified and disambiguated language of intention.

Modern automation introduces a tension between control and action: as systems become smarter, the abstraction between a user's directive and the resulting behavior becomes less clear. The Mycite Framework ensures that every computational action, whether triggered by human input or another process, remains legible and modifiable. Control is preserved not through containment, but through dynamic, interoperable system design.

---

## Project Layout

- /ProjectFolder
- ├── main.py           # Entry point script: Holds App state and Hosts Control gate & Peripheral Socket participation.
- ├── MSS_convention.py # Logic module: Load Data file in as memory, change and update memory, configure new MSS design, etc.
- ├── terminal_ui.py    # Tkinter I/O socket handlers 
- ├── README.md         # This file
- ├── docs/             # Specialized directory
  - ├── [White Paper](Mycite-white_paper.md)
  - └── [Schema Standardization]
- └── assets/           # Optional specialized module directory with init.py to group modules in packages
  - ├── bloom/          # Ambiguous Design division logic to visualize Control Gate view field
  - ├── hyphae/         # Input command line abstraction module
  - └── KatBots/        # Application tool module

---

## Core Components

### `MSS_convention.py`
Implements the **Mycelium Schema Standardization (MSS)**:
- Defines binary parsing and index structures (`index_a`, `index_b`, `index_c`, etc.)
- Provides `UI_layer` and `UI_ssid` classes for semantic scoping
- Loads data from `world.bin` into a structured semantic graph
- Supports layered addressable contexts (`SSID`) and dynamic data growth

### `main.py`
Manages live system execution via `AppState`:
- Holds active MSS system state (`mss_systm`)
- Buffers asynchronous input from HID, network, and peripherals
- Provides enqueue/dequeue mechanisms with flags
- Runs the `main_loop`, which isolates HID input when present, otherwise checks network and peripheral buffers
- Serves as the orchestration layer between MSS state and user/system interaction

### `terminal_ui.py`
Implements the **Tkinter UI layer**:
- Renders a responsive window (“MSS Control Gate”)
- Provides a bottom command bar for text input
- Handles `/ENTER COMMAND` and quit (`q`) commands
- Dynamically resizes and redraws interface tiles
- Acts as the user’s visual and command interface to the MSS system

---

## How It Works
1. `MSS_convention.py` loads and structures binary data from `world.bin` into MSS indices and SSID layers.  
2. `main.py` initializes `AppState`, creates buffers, and manages the main execution loop.  
3. As inputs arrive (HID, NET, PERI), they are queued into buffers and dispatched to directives or daemons.  
4. `terminal_ui.py` provides a graphical entry point for user input, rendering state and allowing text commands.  

---

## Background Concepts (for reference)
- **MSS (Mycelium Schema Standardization):** Base model for storing and interpreting data in extensible, domain-agnostic form.  
- **SSID Layering:** Semantic frames that define scope boundaries in which references are meaningful, enabling modular reuse and logical extensibility.  
- **Rieman-Zeckendorf Notation (RZN):** A method for encoding values in a canonical, retroindeterministic format that supports layered, lossless integer addressing.  

These theoretical models inform the current prototype but are now directly embedded in `MSS_convention.py` instead of separate modules.

---

## Development Roadmap
- Flesh out peripheral processes (HID, network, peripheral handlers)  
- Expand intention handling logic inside `AppState`  
- Connect UI input to state directives  
- Add logging and diagnostics  
- Implement modular plugin architecture for future extensions  

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows modification, redistribution, and commercial use with attribution.

---

## Acknowledgments

Built and authored by Dylan Montgomery
VERSION:	9.03.04
Status: Active prototyping and architectural refinement
