from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Load the trained model
model = tf.keras.models.load_model("mnist_model.h5")

# Create FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "MNIST API is running"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read and preprocess image
    image = Image.open(io.BytesIO(await file.read())).convert("L")  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to match MNIST input shape
    image_array = np.array(image) / 255.0  # Normalize
    image_array = image_array.reshape(1, 28, 28, 1)  # Reshape for model

    # Make prediction
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)
    
    print("digit: ", int(predicted_digit))

    return {"digit": int(predicted_digit)}
