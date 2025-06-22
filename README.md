# Mycite Framework

## Overview
The Mycite Framework is a control system and data handling skeleton built to support extensible software and data environments through semantic coordination. It reflects a design principle where automation and smart systems remain interpretable and controllable by their users. Not through simplification, but through a unified and disambiguated language of intention.

Modern automation introduces a tension between control and action: as systems become smarter, the abstraction between a user's directive and the resulting behavior becomes less clear. The Mycite Framework directly addresses this by ensuring that every computational action, whether triggered by human input or another process, remains legible and modifiable. Control is preserved not through containment, but through dynamic, interoperable system design.

True privacy in a connected system requires that individuals and communities can build, control, and update both hardware and software that interact across platforms, without sacrificing intelligibility. Mycite enables this by offering a universally structured semantic schema (MSS) and layered addressable contexts (SSID), where meaning can evolve while remaining logically consistent and interoperable.

---

## Project Layout

- /ProjectFolder
- ├── main.py          # Entry point script: Holds App state and Hosts Control gate & Peripheral Socket participation.
- ├── boot.py          # Logic modules: Load Data file in as memory, change and update memory, configure new MSS design, etc.
- ├── README.md        # This file
- ├── hardware.py      # Less interoperable single I/O socket handlers 
- ├── OperatingSystem/ # Specialized directory
- └── assets/          # Optional specialized module directory with init.py to group modules in packages
  - ├── bloom/         # Ambiguous Design division logic to visualize Control Gate view field
  - ├── hyphae/        # Input command line abstraction module
  - └── KatBots/       # Application tool module

---

## Core Components

### main.py

#### AppState
The central brain managing:
- What’s currently focused (attention)
- What’s visible or active (view)
- What relationships or context are linked (earshot, archetypes)
- What intentions or actions are queued for processing

It synchronizes all live system state.

#### Peripheral Processes
These are modular input and output modules:
- StateReadIn → Handles human/device input (keyboard, mouse, sensors)
- StateReadOut → Drives human/device outputs (visual display, feedback)
- MyciteReadIn → Captures network or external system input
- MyciteReadOut → Pushes system state or results outward

Each runs asynchronously, feeding or consuming data for the core system.

#### Intention Handler
This interpretive layer:
- Classifies raw events into four intention types:
    - Navigation → Moving focus or scope
    - Investigation → Querying internal structure
    - Manipulation → Changing data or state
    - Mediation → Coordinating across boundaries
- Dispatches intentions to modify AppState
- Keeps the system’s meaning clear despite multiple asynchronous signals

#### The Main Loop
The synchronous Clock:
- Processes queued intentions
- Recalculates the view, state, or outputs
- Drives visual or external updates (e.g., via Pygame or network)

### boot.py

#### bootLoad
Boot logic parses and reconstructs schema sections (Index_A, B, C, S, T, and O) using modular parsing functions. The process begins by reading in a raw bitstream and interpreting it as a structured semantic address space rather than a flat record set.

Using Semantic-System ID Layering (SSID), MSS allows highly abstractable domains to coexist alongside granular detail. Each SSID Layer is a semantic scope boundary within which addressable references hold meaning. This enables meaning to be deferred through interpretive chains rather than fixed fields. It allows new schemas to evolve dynamically while preserving backward compatibility, enabling long-term extensibility and interoperability.

#### Mycelium Schema Standardization
MSS is the base model for standardizing how data is stored and interpreted. The pilot version defines:
- Index A: Size parameters for memory/space constraints
- Index B: Size parameters for remaining Schema definition ( Index A + B + C)
- Index C: Sectioning of remaining file space for structural blueprint
- Index O: Segmentation map (SSID layers)
- Index S/T: Spatial/temporal abstractions for layout, behavior, or positioning
It ensures consistency while remaining domain-agnostic.

RIEMAN-ZECKENDORF NUMBER (RZN) NOTATION:
A method for encoding values in a canonical, retroindeterministic format that allows self-termination and zoomable extensibility. Data is stored as prime-indexed values via three segments:
- Slice A: Up until what largest prime is necessary to define the space.
- Slice B: Which primes are present for use
- Slice C: To what value are each of the primes to the power of prime
This supports layered, lossless integer-based addressing, ideal for layered semantic models.

SEMANTIC-SYSTEM IDENTIFICATION (SSID) LAYERING:
- Layers are semantic frames that define scope boundaries in which references are meaningful. Each layer governs its own address space and points to archetypes defined in the previous layer. This enables modular reuse of tables and instances, where values hold meaning only in their scoped semantic context. It supports multi-resolution data referencing and logical extensibility without global redefinition.

Clarification:
- The bridge between the RZN is the point in which the space is assumed to notate the Rudi group in which the recombination in which are used to create the SSID abstraction layers.

Point of consideration for Alternative Design and/or Further Refinement:
- Using a Riemann-Pingalla-Notation (RPN), it can be shown that the use of a number notation that is less efficient in value increase can overall match a value notation. Done by using the polar nature of Tertiary-Basic (TB) in combination with RPN's use of the Fibonacci Sequence to allow for the notation of one value in multiple different ways. Increasing in means of notation by the size of description, the added semantics are in the modularization of space defined.

SUMMARY INTEGRATION:
By combining RZN and SSID Layering, a system is created that can model complex, recursive abstractions in a linear, machine-friendly way. It reflects the digital system’s sequential nature while allowing for semantic flexibility, extensibility, and depth-aware composition.

---

## How It Works

1. `bootLoad()` Loads system memory (e.g., from .bin files) and unpacks binary data.
2. `bootStrap()` Initializes parsed and structured in-memory relational data base to attach to app state system
3. `main.py` Creates AppState, launches the synchronous main loop.
4. Peripheral Processes: Asynchronously detect inputs or required outputs, adding updates to system buffers.
5. Intention Handler: As a part of the Control Gate convention of implementation; reads primary and secondary peripheral signals, classifies them, and serves them to AppState.
6. StateReadOut: Observes and pushes relevant Appstate updates to inform visuals or outputs to the user or external systems.

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
- Add modular plugin architecture for easy future extensions
- Implement logging, diagnostics, and testing scaffolds

(Future layering of federated trust systems and custom governance logic through interoperable semantic modules)

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows modification, redistribution, and commercial use with attribution.

---

## Acknowledgments

Built and authored by Dylan Montgomery
VERSION:	6.10.01
Status: Active prototyping and architectural refinement
