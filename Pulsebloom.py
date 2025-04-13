import streamlit as st
import pyttsx3
import speech_recognition as sr
from deepface import DeepFace
import tempfile
import os

# Setup text-to-speech engine
engine = pyttsx3.init()

# Plant image map based on emotion
plant_map = {
    "happy": "https://cdn.pixabay.com/photo/2016/11/23/15/36/sunflower-1853323_960_720.jpg",
    "sad": "https://cdn.pixabay.com/photo/2017/06/20/21/36/flower-2420074_960_720.jpg",
    "angry": "https://cdn.pixabay.com/photo/2018/06/26/19/31/cactus-3502487_960_720.jpg",
    "surprise": "https://cdn.pixabay.com/photo/2020/01/22/19/49/flower-4785616_960_720.jpg",
    "fear": "https://cdn.pixabay.com/photo/2016/07/19/22/02/dark-1528308_960_720.jpg",
    "neutral": "https://cdn.pixabay.com/photo/2020/08/25/11/24/plant-5515931_960_720.jpg"
}

st.title("PulseBloom: The Emotional Garden")
st.write("This app uses your **voice** to detect emotion and grows a plant reflecting how you feel.")

# Voice input + emotion processing
if st.button("Tap to Speak"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
        # Fake emotion detection for demo
        if any(word in text.lower() for word in ["happy", "great", "fun"]):
            emotion = "happy"
        elif any(word in text.lower() for word in ["sad", "tired", "down"]):
            emotion = "sad"
        elif any(word in text.lower() for word in ["angry", "mad", "frustrated"]):
            emotion = "angry"
        elif any(word in text.lower() for word in ["surprised", "wow", "what"]):
            emotion = "surprise"
        elif any(word in text.lower() for word in ["scared", "afraid", "fear"]):
            emotion = "fear"
        else:
            emotion = "neutral"

        st.image(plant_map[emotion], caption=f"Your emotion: {emotion.capitalize()}")
        engine.say(f"You sound {emotion}. Let your plant bloom.")
        engine.runAndWait()

    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand you.")
    except sr.RequestError:
        st.error("Speech Recognition service error.")
