//Author: Dylan Montgomery
//Title: Genesis Java Script File
//Purpose: Initial Setup (Set up the Index and DOM appropriately upon loading)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

let binaryData = null;             	// Global variable for binary data
let SamanticAbstraction = [];      	// Dynamic global array for storing data
let MSSSBootStrap = [1,0,1,1,0,...]	// Standardized abstraction array

let bootMSSS = true;
let ooMSDL = true;
let bloomMSDL = true;
let hyphaeMSDL = true;

let MSALArchatype = []; //Array Multi use abstraction templates
let MSALPorts = null; //Array of MSAL arch instances/runaways and null [0]

let archtpArr[] = null;
let imgArr[] = null;
let adrs = 0;
let titleDynamic = 0;

const portalArr = [];
let portalArrPtr = null;    // Portal array position value held for feeding into functions for use

const archtpArr[] = null;
let archtpArrPtr = null;    // Archetype array position value held for feeding into functions for use

// Calculations based on viewport size and the 34-segment system
const vpDispGrid = window.innerWidth / 32;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

async function startFileLoad() {
    const MSSSfilePath = 'assets/world.bin'

    try {
        // Fetch the binary file from the specified path
        const response = await fetch(filePath);
        
        // Check if the response was successful
        if (!response.ok) {
            throw new Error(`Failed to fetch binary file: ${response.statusText}`);
        }

        // Convert the response data into a binary buffer and assign to global variable
        const arrayBuffer = await response.arrayBuffer();
        binaryData = arrayBuffer;  
        
        // Confirm successful data load
        console.log('Binary data successfully loaded:', binaryData);
        return binaryData;
    } catch (error) {
        // Catch any errors and log a detailed message
        console.error('Error loading binary file:', error.message);
        binaryData = null;  // Clear the global variable on failure
        return null;
    }
}

// Example of accessing the raw ArrayBuffer data directly using a DataView
const view = new DataView(binaryData);
console.log('First byte:', view.getUint8(0));  // Access first byte directly

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//bootMSSS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function parseBinaryData(binaryData) {
  let offset = 0; // Tracks the current position in the binary array

  while () {

  }

  return parsedData;
}

function MSDLInitialize() {
    const parsedData = []; // Array to store parsed data
    
    parseBinaryData(binaryData)
    
    structureParsedData(parsedData);
    
    console.log("MSDL Initialization Complete:", SamanticAbstraction);
}

async function startDataInitialization() {
    // Clear the global array
    SamanticAbstraction = [];
    
    try {
    
        if (!binaryData || binaryData.length < 256) {
            throw new Error(`Failed to process Bootstrap`);
        }
        
        // Compare the first 256 bytes
        for (let i = 0; i < 256; i++) {
            if (binaryData[i] !== MSSSBootStrap[i]) {
                bootMSSS = false;
                throw new Error(`Failed to match Bootstrap`);
            }
        }
        
        console.log("MSSS Bootstrapping matched. Running MSDLInitialize...");
        MSDLInitialize();
        return parsedData;
        
    } catch (error) {
        console.error('Error MSSS Bootstrap. Running Manual Abstraction...');
        return null;
    }    
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//ooMSDL
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Portal {
    static defaultWidth = 8 * vpDispGrid;
    static defaultHeight = 5 * vpDispGrid;
    static defaultArchetype = "Default Archetype";
    static defaultZIndex = 1;

    constructor(title = "Untitled Portal", bio = "No bio available.", img = "") {
        this.archtp = Portal.defaultArchetype;
        this.title = title;
        this.bio = bio;
        this.img = img;
        this.width = Portal.defaultWidth;
        this.height = Portal.defaultHeight;
        this.styles = { zindex: Portal.defaultZIndex };
        this.top = undefined;  // Undefined, can be assigned later
        this.left = undefined;
    }

    // Method to create and return a portal element
    createElement() {
        const element = document.createElement('div');
        element.style.position = 'absolute';
        element.style.width = `${this.width}px`;
        element.style.height = `${this.height}px`;
        element.style.backgroundColor = 'grey';
        element.style.border = '1px solid black';
        element.style.top = `${this.top}px`;
        element.style.left = `${this.left}px`;
        element.style.zIndex = this.styles.zindex;
        element.innerHTML = `<h3>${this.title}</h3><p>${this.bio}</p>`;
        return element;
    }
}

//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// Uses parsed data 2D array pointers to create classed objects
function buildPortal(parsedData) {
    
}

// Updates arrays by assigning objects to their allotted array
function updatePortalArr() {
    // Push the value into the provided array reference
    portalArr.push();
}
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

// Uses functions to iterativley build objects from parsed data and push them to objects' allotted array
function startDataPropagation(parsedData) {
    
    for (int i = 0, i < n, i++) {
        if () {
        
        updatePortalArr();
        }
        
        portalArrPtr = null;
        archtpArrPtr = null;
    }
    
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//bloomMSDL
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function propagratePortalRenderVals() {
    let m = 1; // Group counter
    for (let n = 0; n < portalArr.length; n++) {
        // Positioning the portal based on the group of three
        if (n % 3 === 0) {
            portalArr[n].top = m * 7 * vpDispGrid;
            portalArr[n].left = 3 * vpDispGrid;
        } else if (n % 3 === 1) {
            portalArr[n].top = m * 7 * vpDispGrid;
            portalArr[n].left = 13 * vpDispGrid;
        } else if (n % 3 === 2) {
            portalArr[n].top = m * 7 * vpDispGrid;
            portalArr[n].left = 23 * vpDispGrid;
            m++; // Increment group counter after a full set of three
        }
    }
}

function startRender(containerId) {
    propagratePortalRenderVals();
    
    // Get the container element where Portals will be rendered
    const container = document.getElementById(containerId);

    if (!container) {
        console.error(`Container with ID ${containerId} not found.`);
        return;
    }

    // Clear the container before rendering (to avoid duplicates)
    container.innerHTML = '';

    // Iterate over the portalArr array and render each Portal using the class method
    portalArr.forEach((portal) => {
        // Use the createElement() method directly from the Portal class
        const portalElement = portal.createElement();

        // Set the position using the portal's stored properties
        portalElement.style.top = `${portal.top}px`;
        portalElement.style.left = `${portal.left}px`;

        // Append the Portal element to the container
        container.appendChild(portalElement);
    });
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//hyphaeMSDL
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function startControlPropagation() {
	…
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

async function genesis() {
    for (int i=0, i < 5, i++) {
        if (i = 1 ) {
            startFileLoad();
    	} else if (i = 2 ) {
    	    if (bootMSSS) {
        	    startDataInitialization();
    	    } else {
    	    	manualAbstraction();
    	    }
    	} else if (i = 3 ) {
    	    if (ooMSDL) {
        	    startDataPropagation();
    	    } else {
    	    	manualAbstraction();
    	    }
    	} else if (i = 4 ) {
    	    if (bloomMSDL) {
        	    startRender('portal-container');
    	    } else {
    	    	manualAbstraction();
    	    }
    	} else if (i = 5 ) {
    	    if (hyphaeMSDL) {
        	    startControlPropagation();
    	    } else {
    	    	manualAbstraction();
    	    }
    	}
        console.log('Genesis step:', i);
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

genesis();

/*
function getDynamicTitle() {
  return 'Static Title';
}

function updatePageTitle(newTitle) {	// Function to update the webpage title
  if (newTitle && typeof newTitle === 'string') {
	document.title = newTitle; // Update the title if the new title is valid
  } else {
	console.warn('Invalid title value provided.');
  }
}

updatePageTitle(newTitle);  // Call the function to update the title
*/

//The Primary port by be checking for MSDL rudi group match
//If else then loading new MSAL variable values from initialized variables with MSDL values.
//Other ports are still left as secondary ports in case of MSDL abstraction rather than bootstrap abstraction.
//Finally the specific data signifiers are implemented with the same function
