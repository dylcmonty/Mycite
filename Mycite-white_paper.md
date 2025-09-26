# INFORMATION TECHNOLOGY SOCIAL SYSTEMS 
## THE MYCITE PROJECT MISSION & A DISAMBIGUOUS UNIVERSAL LANGUAGE OF INFORMATION

**AUTHORED BY: DYLAN MONTGOMERY**

---

### ABSTRACT
Information has inherent properties. These laws of reality resist information ownership and containment. This condition of information, in tandem with ever growing technological advancement, wages a continued instability on current tools that underpin our daily lives. Simultaneously there are limitless positive implications in a paradigm of software and hardware that operate on a universal language of information (ULI).

---

## §1. THE MSS CONVENTION

Digital computers, in combination with laws of information, provide a stringent guide that one must stay within to create a ULI. The MSS is a method of implementing a self organizing universal language of information.

Note the parameters:
- Self-terminating
- Retrodeterministic
    The meaning of any part of a sentence can’t be understood as intended until the sentence signals that it is finished; either by pause or by contextual conclusion.
    This is the result of not using a “word size convention, so that the convention is not limited by any size parameter.
- Polymorphic Combinitoric Continuity
    In tandem with no size constraints or use of ‘word size’, we are able to employ a system of recombination.
    This means that every ‘layer’ of any of the possible instances of an abstraction's notation can be used to define a new instance in a later abstraction. (Only possible for application with a ‘clean up’ carry over bit mask.)
    Progressively zoomable: higher layers refine information without rewriting earlier ones.

With these as a base, one can describe a ULI that takes the form of a sequential stream of 1’s and 0’s, one that can then notate any instance of information. However, there are many notable conventions used for the particular ULI that is discussed later. This is to avoid the explosive size of notating ever more complex abstractions of rearrangement.

### §1.1 SEQUENTIAL BIT STREAM INTERPRETING

Let's consider the method in the context upon binary file acquisition. Firstly, beginning by reading the contents of a binary file and expressing the data as a flat sequence of bits. This transforms raw byte-oriented storage into a bit-level stream suitable for structural interpretation. With these assumptions in place we can apply a methodology to interface with the Mycelium Schema Standardization.

#### §1.1.1 Initial Segmentation
- Detection of Index A:
    From the beginning of the bitstream, identify the run of consecutive 1s until the first 0 is encountered.
    This initial run constitutes Index A.
    The length of this run (the count of 1s) is significant: it defines a constant referred to as the address size.
    Going forward, all structural addresses in the stream will be expressed in blocks of this length.
- Extraction of Index B:
    Immediately following Index A and its terminating 0, the next block of bits—of length equal to the address size—is isolated.
    Interpreted as a binary integer, this block yields Index B.
    The semantic role of Index B is to denote the file size or overall length of the bitstream.
- Construction of Index C:
    After Index B, the next two consecutive blocks, each of length equal to the address size, are extracted.
    Together, these four binary integers form Index C.
    Each element of Index C specifies a non-inclusive stopping position for one of the subsequent major sections of the stream.
- Application of Index C:
    The four values in Index C are then interpreted sequentially as delimiters for the following indexes:
        The first value specifies the endpoint of Index D.
        The second value specifies the endpoint of Index G.
    Both of these indexes is defined as the segment of the stream between successive stopping positions, with boundaries determined by the corresponding values in Index C.
- Key Observations:
    Run-Length Encoding of Address Size: The number of leading 1s is not just a marker but a rule-setting mechanism. It dictates the granularity of subsequent address-based parsing.
    Self Organizing Structure:
        The stream encodes both its own size and the boundaries of its subsections within its first few blocks.
        This allows any compliant interpreter to reconstruct the structure without external metadata.
    Hierarchical Partitioning:
        Detect Index A (to establish address size).
        Read Index B (file length).
        Read Index C (subsection boundaries).
        Use Index C to partition the remaining stream into distinct indexes (D, G, E, S).

#### §1.1.2 Further Interpreting
Begin by interpreting an initial portion of the sequential bitstream as a control value. This control value specifies how many high-level structures (e.g., “layers”) will exist in the nested representation.

- Layer Definition:
    For each declared layer, the next portion of the bitstream encodes how many substructures (e.g., “groups”) that layer contains.
    Each group count is drawn sequentially from the stream, so the stream itself dictates the topology.
- Group Definition:
    For each group, another segment of the stream specifies how many iterations (repeated sub-units) it will hold.
    Again, the count of iterations is not arbitrary; it is derived directly from successive values in the stream.
- Iteration Population:
    Once the structure of layers and groups is defined, subsequent segments of the bitstream are consumed in fixed-size units (in this example, pairs of values).
    Each unit corresponds to the contents of an iteration.
    Thus, the raw stream is gradually partitioned: first to set the hierarchy, then to fill it with data.
- Hierarchical Assembly:
    The nested representation is constructed by associating each extracted value with its ordinal position (e.g., “layer 1,” “group 2,” “iteration 5”).
    This ordinal indexing provides unique keys for every element in the hierarchy, regardless of the actual bit values.
    The result is a tree-like structure in which the bitstream is both the blueprint (defining counts) and the content (providing payload values).
- Key Principle:
    The process alternates between two modes:
        Counting mode (determine how many children or iterations to expect at the next level).
        Filling mode (consume the specified number of payloads).
    Because the stream is sequential, each mode consumes exactly as much data as is needed before moving forward.

A good rule of restraint is in trying to apply a system that allows for the extrapolation of building blocks. This allows for the mapping of values without recombination. Then use the post genesis name space to recombine for data storage and use.
Since, written language is attributed

Initial value notations within the schema must extend themselves to maximize their notation, with respect to space, by aligning with digital limiters. The value notations must maintain retroindeterministic behavior.  To do this we use unitary prefacing.
Urinary prefacing must expand the magnitude in which a following denotation can represent at ever increasing rates of continued prefacing. This can only be done by representing an increasingly increasing constant rate of notation that sets the frame for the following notation. (This is NOT an increasingly increasing constant rate of value, but rather the manner in which each respective sequential 1, or ‘TRUE’ bit, can further instill in what is to be expected. All of which is up until a 0, or a ‘FALSE’ bit, is encountered.)
Therefore, the balance in this growth must consider
What are the informational limits of representing a continuous natural number field array?

To isolate this limiter, we can consider each cell of notation as an incremental addition to the informational capacity of a notation.
{ See Markov Chains and or Stochastic Processes}
Now if we use a convention that employs a capacity to add or subtract by 1, then we can create paths to values within an instilled field that more efficiently arrives upon a greater number of values.

### §1.2 DATA SEMANTIC NETWORKS

Instead of each piece of hardware or software defining its own format and requiring custom translation layers, we use a shared data standard, so every system can speak the same language natively. However, even with data standardization, each standard still limits what can be expressed and translation between standards isn’t always possible if they capture different assumptions or dimensions of the data. Hardware and software each follow their own internal logic and data handling standards, using external standards only at the point of transmission. So, the meaning of data is local to the system’s operational context, not to the standard it's packaged in. 

Currently, hardware and software systems cannot achieve indiscriminate interoperability by default and they must be explicitly engineered to interact in specific ways. This is because there exists no universal data standard capable of expressing the infinite variety of possible data structures, contextual relationships, operational states, and localized identifiers that define how systems behave.

Internally, every system handles data in a way that is deeply tied to its own logic and operational flow. External data standards, when used, merely serve as fixed formats for transmission, not for internal interpretation or function. As a result, systems cannot natively interpret or manipulate arbitrary data or behavior without prior integration work."

This has real-world consequences. For instance, software interfaces (especially graphical user interfaces or GUI's) are built with hard-coded assumptions about purpose, data types, and interaction models. Because the GUI is not modularized by function or semantic context, it cannot automatically reconfigure itself to support different modes of interaction, such as non-visual navigation. This is a key reason digital systems remain inaccessible to many visually impaired users.

In short, unless explicitly designed to expose their structure, behavior, and data semantics in a modular and machine-readable way, software systems cannot adapt their interface or behavior to new contexts. The limitation is not just technical, it’s foundational to how we currently design systems: for specific uses, in specific forms.

#### §1.1.2 The Technical Core:
The vision of the semantic web has long been to create a more intelligent and intuitive internet by structuring data in a way that machines can understand context and relationships. The concept is meant to create an internet that revolves around creating a web where data is structured and tagged with metadata; in a way that encodes relationships for the meaning, and context between different pieces of information. However, it has faced many challenges in terms of implementation. The foremost hurdle being the complexity of structuring all web data in a universally understood format, and the sheer scale of the web makes it challenging to adopt such a system universally. This leads many to believe it’s not a viable approach on a large scale. Instead, more focused applications, like structured data for search engines, have become the practical route forward.
In contrast, the Mycite Framework demonstrates that a semantic data structure is indeed possible and practical.

By integrating data and metadata into a single, unified system, the framework uses a highly reduced alphabet of elements to embody the components that are arranged to create any instance of information. This is accomplished by using the SSID Layering to create hierarchical abstractions. 
This approach uses partial-convention, rather than being solely self defining. This allows for the unrestrictive nature of what can be defined, while also preventing notations from having to notate with impossible specificity that differentiates an instance from infinity.

#### § 1.2.2 MSS Interface Development:
The significance of being able to reduce all information down into a universal language is that it is made up of a finite set of components that when reneged, can make up any instance of information. In this way, all encodings of information can be represented as locations that are navigated to and all creations are discovered. This allows for encoding of information in memory as mapped out location within this space. In doing so it can be made immediately parents how adjacent locations are contextualized with each. 

This is also the same reasoning with which the MSS software is made to handle and operate on data without being explicitly engineered to. This makes the task of software development far faster for any given purpose and context. Rather than having to consider how to visualize data, navigate it, and mediate on it for each case; the Dev process foremost includes considerations for how a user may want to more complexly interface with data, rather than what form it expects information to exist in.

In this way; weather software is made to operate as a computer directed process or if it involves a human interface; the software framework can stay the same for almost any case. This is what is called the MSS Control Gate  Framework (GCF). The GCF functions as an input abstraction layer; where no matter if it's mouse, keyboard, or an API, it comes through as a unified "intention" type, like navigation, investigation, mediation or manipulation. In this way, the GCF can have software developed over top of it to handle that intention in context, without prior context. This is all possible as the MSS is accessible as if it were a single instance of data, where interfacing allows for the GCF to handle all data and its structures as an ordered instance is abstracted from the observable components its made from. This means the application state, like the current location of investigation,( i.e. the directory) or aspects of child objects that may be selected, they all shape how the system responds to output to a display or terminal.

Additionally this can also be used to deepen the understanding an AI’s Neural network has about a singular topic and its relation to other ideas.

    "Some people can read War and Peace and come away thinking it's a simple adventure story... Others can read the ingredients on a chewing gum wrapper and unlock the secrets of the universe."
- Lex Luthor in the 1978 movie Superman

---

## §2. IMPLEMENTATION

Information has inherent properties. Natural forces, similar to that of gravity or energy, make information’s true nature one that is perpetually resistant to its containment. This physical reality makes ownership a fiction and gets reflected in how well information aligns with a belief that all new ideas are discovery and not creation. 

These simple articulations have heavy implications as they become more difficult to defy. Artificial intelligence, quantum computing and global connectivity amplify the mismatch between laws of information and ownership. Of note are the cracks in online encrypted connection as a result of quantum computing; the challenges made to artists, engineers, and lawyers alike to compete with AI’s mechanistic mastery; and helplessness in preventing copyright piracy. 

However, a third option exists outside this default response of tighter centralisation and rejection of modernity. It demands the treatment of information not as a commodity ( one to be contained), but as a non-excludable and non-depletable resource. One that is built on the basis of a universal language of information. When information is recognized as non-excludable and non-depletable, an economy would inevitably align to reward individuals for the exploration and furthering of ideas, not for their "creation". The Mycite Project is a response to this moment of choice. It asserts that this technological infrastructure can be built as a precursor solution before it becomes a primary solution.

This pursuit demands public discourse. Just as energy cannot be owned, only harnessed, information must be allowed to flow,
recombine, and self-discover. The Mycite project and this report outlines why this shift can be made a flawless transition by starting in agriculture to save billions of dollars in waste that leaks out of local communities. The question is not whether this transformation will come, but whether we will meet it with foresight or be overtaken by crisis.

What is proposed here is simple in premise and revolutionary in implication: a world in which every datum can be understood in context to what it is, to whom it was cited to, and under what terms it should be seen.Yet, solutions such as these are not fully adopted until catastrophe strikes. Thus, in the meantime, the Mycite Project is on a mission-driven effort to support public awareness of systemic information problems and to develop the Mycite Framework as an infrastructure solution, by utilizing the power of this new technology to achieve what is thought to be impossible: universal information literacy without a central authority. The Mycite project, firstly, aims to assist small agriculture networks to operate at the same economies of scale and efficiency as a single large industrial farm. In this way, the Mycite project aims to provide an alternative so much better that the world can’t help but adopt it to compete in a new terrain of commerce.

Let it be clear: the semantic internet will not ask permission. The Mycite Framework does not wait for the reluctant custodians of scarcity to approve. Like literacy before it, this shift begins wherever someone decides to build, and spreads wherever someone refuses to be locked out of meaning.

The door is open.

Step through, or be stepped over.

### §2.1 GLOBALIZATION

The modern information economy is dominated by centralized platforms designed to contain rather than coordinate. From agriculture to healthcare, these systems impose artificial drag: duplicated efforts, incompatible standards, and opaque supply chains. In such architectures, waste is not a side effect, it is structural.

Take agriculture as an example; despite a demand for less pesticides, more heirlooms, sustainably grown produce; and a clear and common value for local economies, small farms still operate 10% more efficiently per acre than industrial farms with respect to perishable crops. That figure only applies to a farm's ability to output. Thus, either as a result of waste, or by not being able to plan to grow greater amounts of produce; small farms are merely limited by an inability to locate demand for supply. Local supply fails to meet regional demand due to fractured communication networks and rigid software ecosystems designed for monopolistic operations. Small actors cannot coordinate at scale, and large actors cannot adapt without imposing full control. 

The productivity gap is more so an observation that can be attributed to small-agriculture's obstruction to being collectively accessible. This discourages the Agricultural industry from making use of their output, causing perishable crops to go to waste (without a known buyer). This also prevents SSL agriculture from fully utilizing their land, as they can not expect a buyer output match to what they may be able to yield.

Where coordination is most needed, rigidity compounds failure. The Semantic Internet offers a structural alternative: rather than requiring all participants to conform to a dominant system, it makes meaning itself legible across systems. Semantics becomes the bridge between diverse actors, eliminating the need for uniform infrastructure.

Just as automotive centralization once produced affordability through scale, it later stagnated innovation. Similarly, individuals today can produce studio-grade media with tools that once required entire teams. Yet the administrative infrastructure that once enabled broad access is being re-centralized under monopolistic control. The pattern repeats: centralization brings initial efficiency, but eventually becomes a bottleneck to innovation.

Meanwhile, globalized supply chains remain locked into economies of scale. Multinational corporations outcompete local businesses not because of product superiority, but because they control top-down visibility into supply and demand. Local businesses could rival them. If economies had complete and instant transparency to demand and supply, a more competitive and pure meritocracy can give way. Today, such coordination is only possible within a single corporate silo.

A semantic architecture changes this. Shared grammar enables cooperation without centralized control. Local businesses retain autonomy while achieving the same economies of scale as multinationals. Waste declines, coordination increases, and global reach is no longer exclusive to monopolies.
Shared grammar enables cooperation without monolithic platforms.
Centralized architectures create drag and spoilage by design.

#### §2.1.1 Barcelona Proof-Point:
Barcelona’s decision to pursue a zero-import, zero-export economy is among the first civic-scale attempts to operationalize a locally productive, globally connected model. The program was launched through the Fab City initiative and developed by the Institute for Advanced Architecture of Catalonia (IAAC) and rooted in the global Fab Lab network. This strategy embodies what Neil Gershenfeld describes as a future where data travels globally but materials stay local.¹

Rather than rely on centralized production and logistics, Barcelona invests in distributed infrastructure: public maker spaces, open-source toolchains, local fabrication labs, and educational programs. Design files can be shared across continents, but physical goods are produced in the neighborhood. The city effectively flips the supply chain from importing finished goods to importing instructions. This proves more than a policy innovation. It shows that complex, urban-scale economies can decentralize without losing interoperability, precisely the kind of architecture the Semantic Internet enables for information systems. When meaning is standardized and interaction is legible, coordination no longer requires hierarchy.

    Neil Gershenfeld, Alan Gershenfeld, and Joel Cutcher-Gershenfeld, Designing Reality: How to Survive and Thrive in the Third Digital Revolution (Basic Books, 2017).

#### §2.1.2 The Mycelium Network:
While blockchain protocols replicate trust through rigid consensus and ledger duplication, the Mycite Network achieves distributed cooperation through semantic alignment. It is not a chain of blocks. It is a lattice of meaning. Nodes operate independently, resolving interoperability through "semantic diff" rather than absolute uniformity. Each node maintains its own schema and interpretive context. Synchronization occurs not by enforcing a single truth, but by resolving differences through shared grammar. The outcome:
Autonomy: Nodes retain their own workflows, logic, and priorities.
Interoperability: Nodes interpret each other’s data without sharing infrastructure.
Auditability: Logs reflect not just what happened, but how meaning was resolved.

This avoids the rigidity of frozen ledgers and the inefficiency of universal consensus. Trust becomes an outcome of interpretability, not brute replication.

Practically, this allows two regional food cooperatives to share data on forecasts, inventories, or logistics. Even if their systems are entirely distinct. They don’t need to run the same software. They need only share a semantic data fabric. Governance and privacy are preserved; coordination becomes effortless.

The Mycite Network is the infrastructure backbone that makes the Semantic Internet viable. Not as theory, but as a living, federated system of meaning.

### §4.2 FRUITFUL NETWORK DEVELOPMENT

Fruitful Network Development provides interactive, integrated data management software designed specifically to empower local, small-scale agriculture networks. Our unified, user-friendly platform enables farmers and agricultural businesses to achieve economies of scale typically reserved for large conglomerates, without sacrificing independence or profits.
Built on an innovative, semantic web-based framework, our applications seamlessly combine Geo-spatial mapping, land-use planning, inventory control, operational management, and ERP solutions into a single intuitive interface. By eliminating fragmented data silos and redundant hosting, Fruitful Network Development offers significant cost savings, efficiency gains, and simplified logistical management.
Key Benefits:
    Cost Efficiency: Reduce the need for separate hardware, software, and website solutions, minimizing unnecessary operational expenses.
    Salable Collaboration: Enable coordinated, network-driven growth by facilitating shared access to data such as supply, demand, inventory, and pricing information.
    Improved Sustainability: Empower producers to minimize waste, optimize resources, and scale sustainably without reliance on harmful chemicals or destructive practices.

With Fruitful Network Development, consumers can directly support responsible agricultural practices by easily navigating local markets and transparently choosing providers that align with their values. This technology promotes grassroots organization and financial resilience, fostering stronger local economies, healthier communities, and higher standards of food production.

---

## License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows modification, redistribution, and commercial use with attribution.

---

## Acknowledgments

Built and authored by Dylan Montgomery
VERSION:	9.03.04
Status: Active prototyping and architectural refinement

