//Author: Dylan Montgomery
//Title: Genesis Java Script File
//Purpose: Event-Driven Interactions (Adopt the running state and the variables' assigned value to provide interface upon action)

// Global variable to store mouse position
let mouseCords = [0, 0];

// Event listener to track mouse position and update the variables
window.addEventListener('mousemove', (event) => {
    mouseCords[0] = event.clientX;  // Viewport relative X-coordinate
    mouseCords[1] = event.clientY;  // Viewport relative Y-coordinate
});

// Function triggered by mouse clicks
function actionRequest(clickType, mouseCords) {
    if (clickType === 'left-click') {
        console.log(`Left-click detected at: X = ${mouseCords[0]}, Y = ${mouseCords[1]}`);
    } else if (clickType === 'right-click') {
        console.log(`Right-click detected at: X = ${mouseCords[0]}, Y = ${mouseCords[1]}`);
    } else {
        console.warn('Unknown click event');
    }
}

//Function to handle both left and right click events
function setupMouseClickListeners() {
    window.addEventListener('mousedown', (event) => {
        const clickType = event.button === 2 ? 'right-click' : 'left-click';
        actionRequest(clickType, [event.clientX, event.clientY]);
    });
}

// Call the function to start listening for click events
setupMouseClickListeners();

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function createViewportMatrix() {
    // Calculate viewport dimensions
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    // Create a 2D matrix where rows = height, columns = width
    const matrix = new Array(viewportHeight)
        .fill(null)  // Initialize rows
        .map(() => new Array(viewportWidth).fill(0)); // Initialize columns with default value 0

    console.log(`2D Array created with ${viewportHeight} rows and ${viewportWidth} columns`);
    return matrix;
}

// Create the matrix based on current viewport size
const viewportMatrix = createViewportMatrix();
console.log('Viewport Matrix:', viewportMatrix);

