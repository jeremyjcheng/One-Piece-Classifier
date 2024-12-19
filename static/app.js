// Drag-and-Drop Handlers
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    console.log("Dragover event triggered");
    dropArea.style.backgroundColor = '#f9f9f9';
});

dropArea.addEventListener('dragleave', () => {
    console.log("Dragleave event triggered");
    dropArea.style.backgroundColor = '';
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    console.log("Drop event triggered");
    const file = e.dataTransfer.files[0];
    console.log("File dropped:", file); // Log the file details
    handleFile(file);
});

// File Handling
function handleFile(file) {
    if (!file || !file.type.startsWith("image/")) {
        console.log("Invalid file detected:", file);
        result.innerText = "Please upload a valid image file.";
        return;
    }

    console.log("Valid image file:", file.name); // Log the file name
    const reader = new FileReader();
    reader.onload = () => {
        console.log("File successfully read as Base64");
        console.log(reader.result); // Log Base64 string (truncated if long)

        preview.src = reader.result;
        preview.style.display = 'block';

        // Send to backend
        console.log("Sending Base64 image data to backend...");
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: reader.result })
        })
        .then(res => {
            console.log("Received response from backend:", res);
            return res.json();
        })
        .then(data => {
            console.log("Parsed response data:", data);
            if (data.error) {
                console.error("Backend error:", data.error);
                result.innerText = `Error: ${data.error}`;
            } else {
                result.innerText = `Character: ${data.character}`;
            }
        })
        .catch(err => {
            console.error("Fetch error:", err);
            result.innerText = 'Error identifying the character.';
        });
    };

    reader.onerror = () => {
        console.error("Error reading the file");
        result.innerText = "Error reading the file.";
    };

    reader.readAsDataURL(file);
}
