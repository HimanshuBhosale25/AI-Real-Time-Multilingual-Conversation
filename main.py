import os
import io
from google.cloud import speech, translate_v2 as translate, texttospeech
from pydub import AudioSegment

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\Audio Translator\voice-translation-444720-b5fd5eb9bf77.json'

# Function to transcribe audio using Google Cloud Speech-to-Text
def transcribe_audio(audio_file_path: str, language_code: str = "en-US") -> str:
    client = speech.SpeechClient()

    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)

    if response.results:
        return response.results[0].alternatives[0].transcript
    else:
        return ""

# Function to translate text using Google Cloud Translation
def translate_text(text: str, target_language: str = "mr") -> str:
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result["translatedText"]

# Function to convert text to speech using Google Cloud Text-to-Speech
def text_to_speech(text: str, output_audio_file: str, language_code: str = "mr-IN"):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_audio_file, "wb") as out:
        out.write(response.audio_content)

# Function to process the uploaded audio and return the result
def process_audio(file_path: str, source_language: str, target_language: str):
    input_audio_path = "uploaded_audio.wav"
    converted_audio_path = "converted_audio_16bit.wav"

    # Convert to WAV format with 16kHz and mono using pydub
    try:
        audio = AudioSegment.from_file(file_path)
        audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
        audio.export(converted_audio_path, format="wav")
    except Exception as e:
        return {"error": f"Failed to process audio file: {str(e)}"}

    # Transcribe audio
    transcribed_text = transcribe_audio(converted_audio_path, language_code=source_language)

    if not transcribed_text:
        return {"error": "Audio transcription failed. Please try again."}

    # Translate text
    translated_text = translate_text(transcribed_text, target_language=target_language.split("-")[0])

    # Convert translated text to speech
    output_audio_path = "static/translated_audio.mp3"
    text_to_speech(translated_text, output_audio_path, language_code=target_language)

    return {
        "audio_url": f"/static/translated_audio.mp3",
        "translated_text": translated_text
    }
