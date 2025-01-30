async function predictDigit() {
    const fileInput = document.getElementById("imageInput");
    const resultText = document.getElementById("result");
    const preview = document.getElementById("preview");

    if (fileInput.files.length === 0) {
        alert("Please select an image.");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    // Show preview
    const reader = new FileReader();
    reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };
    reader.readAsDataURL(file);

    // Send to FastAPI backend
    try {
        const response = await fetch("http://127.0.0.1:8000/predict/", {
            method: "POST",
            body: formData,
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        resultText.innerHTML = `Predicted Digit: <strong>${data.digit}</strong>`;
    } catch (error) {
        console.error("Error:", error);
        resultText.innerHTML = `Error predicting digit: ${error.message}`;
    }
}
