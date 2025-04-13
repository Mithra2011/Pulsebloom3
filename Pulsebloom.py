import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="PulseBloom - Emotional Garden", page_icon="🌱")
st.title("PulseBloom: Your Emotional Garden")
st.write("Type how you’re feeling, and your emotional garden will grow!")

plant_map = {
    "happy": "https://cdn.pixabay.com/photo/2016/11/23/15/36/sunflower-1853323_960_720.jpg",
    "sad": "https://cdn.pixabay.com/photo/2017/06/20/21/36/flower-2420074_960_720.jpg",
    "angry": "https://cdn.pixabay.com/photo/2018/06/26/19/31/cactus-3502487_960_720.jpg",
    "neutral": "https://cdn.pixabay.com/photo/2020/08/25/11/24/plant-5515931_960_720.jpg"
}

# Text input
user_input = st.text_input("How are you feeling today?", "")

if st.button("Grow My Plant!") and user_input:
    text = user_input.lower()
    if "happy" in text:
        emotion = "happy"
    elif "sad" in text:
        emotion = "sad"
    elif "angry" in text:
        emotion = "angry"
    else:
        emotion = "neutral"

    st.image(plant_map[emotion], caption=f"Your plant is feeling {emotion} today.")

    # Generate audio
    response = f"You sound {emotion}. Your garden is growing beautifully."
    tts = gTTS(response)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
