// JavaScript code to handle the API request and display the results
function getShayari() {
    const keyword = document.getElementById('keywordInput').value;
    const baseURL = "http://localhost:5000/";
    const generateButton = document.getElementById('generateButton');
    const loader = document.getElementById('loader');
    // Show the loader
    loader.style.display = 'inline-block';
    // Disable the generate button while the fetch request is in progress
    generateButton.disabled = true;

    // Make an API request to the backend to get the shayari
    // You can use Fetch or Axios to make the HTTP request

    // Example using Fetch:
    fetch(`${baseURL}/shayari?keyword=${keyword}`)
        .then(response => response.json())
        .then(data => {
            // Display the shayari results on the page
            const shayariContainer = document.getElementById('shayariResult');
            shayariContainer.innerHTML = '';
            const shayariElement = document.createElement('div');
            shayariElement.className = 'shayari';
            shayariElement.innerText = data.shayari;
            shayariContainer.appendChild(shayariElement);

            // Hide the loader
            loader.style.display = 'none';

            // Enable the generate button
            generateButton.disabled = false;
        })
        .catch(error => console.error(error));
}

// Function to handle the Enter key press event
function handleKeyUp(event) {
    if (event.keyCode === 13) { // Check if Enter key is pressed
        event.preventDefault(); // Prevent the default Enter key behavior

        // Programmatically click the "Generate Shayari" button
        document.getElementById('generateButton').click();
    }
}
// Function to copy the shayari text
function copyShayari() {
    const shayariText = document.getElementById('shayariResult').innerText;
    const textarea = document.createElement('textarea');
    textarea.value = shayariText;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Shayari copied!');
}