# MNIST Digit Recognizer

A web application that uses a trained neural network to recognize handwritten digits. The application consists of a FastAPI backend and a simple HTML/JavaScript frontend.

## Features

- Upload images of handwritten digits
- Real-time digit prediction
- Simple and intuitive user interface
- RESTful API endpoint for predictions

## Prerequisites

- Python 3.7+
- TensorFlow 2.x
- FastAPI
- Pillow (PIL)
- uvicorn

## Installation

1. Clone the repository:-
2. Install the required dependencies:
3.You can create a virtual environment and install the dependencies:-

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

3. Make sure you have the trained model file `mnist_model.h5` in the project root directory.

## Project Structure

├── api.py              # FastAPI backend
├── mnist_model.h5      # Trained model
├── index.html          # Frontend HTML
├── style.css           # Frontend CSS
├── script.js           # Frontend JavaScript



## Running the Application

1. Start the FastAPI backend:
Run API: uvicorn api:app --reload


The API will be available at `http://127.0.0.1:8000`

2. Open the `static/index.html` file in your web browser

## API Endpoints

- `GET /`: Health check endpoint
- `POST /predict/`: Accepts an image file and returns the predicted digit

## Usage

1. Open the web application in your browser
2. Click the "Choose File" button to upload an image of a handwritten digit
3. Click "Predict" to get the prediction
4. The predicted digit will be displayed on the screen

## Development

- The backend is built with FastAPI and uses TensorFlow for predictions
- The frontend is built with vanilla JavaScript and uses the Fetch API for making requests
- CORS is enabled to allow cross-origin requests during development
