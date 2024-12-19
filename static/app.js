document.addEventListener('DOMContentLoaded', () => {
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const preview = document.getElementById('preview');
    const result = document.getElementById('result');

    // Drag-and-Drop Handlers
    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.style.backgroundColor = '#f9f9f9';
    });

    dropArea.addEventListener('dragleave', () => {
        dropArea.style.backgroundColor = '';
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.style.backgroundColor = '';
        const file = e.dataTransfer.files[0];
        handleFile(file);
    });

    dropArea.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', () => handleFile(fileInput.files[0]));

    function handleFile(file) {
        if (!file || !file.type.startsWith("image/")) {
            result.innerText = "Please upload a valid image file.";
            return;
        }

        const reader = new FileReader();
        reader.onload = () => {
            preview.src = reader.result;
            preview.style.display = 'block';

            fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image: reader.result })
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    result.innerText = `Error: ${data.error}`;
                } else {
                    result.innerText = `Character: ${data.character}`;
                }
            })
            .catch(err => {
                result.innerText = 'Error identifying the character.';
                console.error(err);
            });
        };

        reader.onerror = () => {
            result.innerText = "Error reading the file.";
        };

        reader.readAsDataURL(file);
    }
});
