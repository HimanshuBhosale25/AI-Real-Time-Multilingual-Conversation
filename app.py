from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from main import process_audio  # Import the function from main.py

import os

# Set up FastAPI app
app = FastAPI()

# CORS middleware to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, JS, CSS, and audio)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the frontend HTML
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as file:
        return file.read()

# Endpoint to process audio
@app.post("/process-audio")
async def process_audio_endpoint(
    file: UploadFile = File(...),
    source_language: str = Form(...),
    target_language: str = Form(...),
):
    input_audio_path = "uploaded_audio.wav"

    # Save the uploaded file
    with open(input_audio_path, "wb") as audio_file:
        audio_file.write(await file.read())

    # Process the audio using the function from main.py
    result = process_audio(input_audio_path, source_language, target_language)

    # Return the translated text and audio file URL
    return result
