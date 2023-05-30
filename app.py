import streamlit as st
import speech_recognition as sr
def transcribe_audio():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust the microphone sensitivity if needed
        recognizer.adjust_for_ambient_noise(source)

        st.info("Listening...")

        # Record audio from the microphone
        audio = recognizer.listen(source)

    st.info("Processing...")

    try:
        # Perform speech recognition
        text = recognizer.recognize_google(audio)

        # Display the transcribed text
        st.success(f"Transcription: {text}")

    except sr.UnknownValueError:
        st.error("Unable to recognize speech.")
    
    except sr.RequestError as e:
        st.error(f"Speech recognition request error: {str(e)}")
st.title("Speech Recognition App")

if st.button("Start Recording"):
    transcribe_audio()
