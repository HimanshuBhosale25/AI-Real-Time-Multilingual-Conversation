# Real-Time Multilingual Conversation 🎤🌍

## Project Overview 🌟
This project implements a real-time text-to-speech translation system that enables users to input text in one language and generate speech in another language. The system uses Google Cloud Speech-to-Text API, Google Cloud's Text-to-Speech (TTS) API and Translation API to provide translation and speech output in over 70 languages.

## Technologies Used 🛠️
- **Python 3.10** 🐍
- **Uvicorn** for running the FastAPI server 🚀
- **Google Cloud Speech-to-Text API** for converting speech into text 🔊➡️📝
- **Google Cloud Translation API** for translating text between languages 🌐
- **Google Cloud Text-to-Speech API** for converting text into speech 🎧
- **FastAPI** for the backend framework ⚙️
- **HTML/CSS** for the frontend design 🎨
- **JavaScript** for handling user interactions 💻

## Features ✨
- **Real-Time Translation**: Users can input Audio input in one language, and it is instantly translated into the target language 🌍🔄
- **Text-to-Speech**: Translated text is converted into speech using Google Cloud's TTS API 🗣️
- **Multiple Language Support**: Supports a variety of languages for translation and speech output 🌏
- **Web Interface**: Provides an interactive interface where users can input Audio and hear the translated speech 💬

## Setup Instructions 📋

### Prerequisites 🧑‍💻
1. **Create a Google Cloud Account**: You need to enable the **Google Cloud Speech-to-Text API**, **Google Cloud Translation API** and **Google Cloud Text-to-Speech API** in your Google Cloud Console.
2. **Install Required Python Packages**: Install the necessary Python packages using `conda` or `pip`.

    ```bash
    conda create --name translation-env python=3.10
    conda activate translation-env
    pip install fastapi uvicorn google-cloud-translate google-cloud-texttospeech fastapi[all] uvicorn websockets python-multipa pydub

    ```

### Google Cloud Credentials 🌥️
Set up the environment variable for Google Cloud authentication:

    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_google_cloud_credentials.json"
    ```

### Running the Project 🚀
Start the FastAPI server with Uvicorn:

    ```bash
    uvicorn app:app --reload
    ```

### Open the Web Interface 🌐
Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to access the translation system.

## API Endpoints 📡
- **GET /**: Serves the frontend HTML page, including all the necessary files (JavaScript, CSS, etc.)
**POST /process-audio**: Accepts an uploaded audio file and processes it for speech-to-text conversion, translation, and speech synthesis.

## Project Screenshots 📸

- **Web Interface:**  

  ![Web Interface](images/Screenshot%202024-12-16%20041339.png)

- **Language Selection Menu:**  

  ![Language Selection Menu](images/Screenshot%202024-12-16%20041357.png)

- **Person talks in English and is translated to Japanese text with Audio in background:**  

  ![English to Japanese](images/Screenshot%202024-12-16%20042932.png)

- **Person talks in Japanese and is translated to English text with Audio in background:**  

  ![Japanese to English](images/Screenshot%2024-12-16%043201.png)


## Future Improvements 🔮
- **Offline Mode**: Implement functionality to work offline by caching translations and speech 📴
- **Transcription Logging**: Save transcriptions of conversations for review and analysis later 🗃️
- **Enhanced UI/UX**: Improve the user interface and user experience for better usability and accessibility 🌟