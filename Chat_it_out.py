import streamlit as st
from st_audiorec import st_audiorec
from openai import OpenAI

client = OpenAI(api_key=st.secrets.api_key)

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # st.audio(wav_audio_data, format='audio/wav')
    audio_file= open(st.audio(wav_audio_data, format='audio/wav'), "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription.text)


