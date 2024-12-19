function handleFile(file) {
    if (!file || !file.type.startsWith("image/")) {
        result.innerText = "Please upload a valid image file.";
        return;
    }

    const reader = new FileReader();
    reader.onload = () => {
        console.log("Image successfully read as Base64:");
        console.log(reader.result); // Log the Base64 string

        preview.src = reader.result; // Display the image
        preview.style.display = 'block';

        console.log("Sending image data to the backend...");

        // Send to backend
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: reader.result })
        })
        .then(res => {
            console.log("Received response from server:", res);
            return res.json();
        })
        .then(data => {
            console.log("Response data:", data);
            if (data.error) {
                result.innerText = `Error: ${data.error}`;
                console.error("Backend error:", data.error);
            } else {
                result.innerText = `Character: ${data.character}`;
            }
        })
        .catch(err => {
            result.innerText = 'Error identifying the character.';
            console.error("Fetch error:", err);
        });
    };

    reader.onerror = () => {
        console.error("Error reading file.");
        result.innerText = "Error reading the file.";
    };

    reader.readAsDataURL(file); // Convert file to Base64
}
