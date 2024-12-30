

import streamlit as st
import speech_recognition as sr

def speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Speak now...")

        audio = recognizer.listen(source)

        st.info("Transforming to text...")
        try:
            text = recognizer.recognize_google_cloud(audio)

            return text

        except:
            return "Sorry, I couldn't hear what you said"

def main():
    st.title("Speech Recognition")

    st.write("Click to start recording")

    if st.button("Record"):
        speech_recognition()

if __name__ == "__main__":
    main()
