import streamlit as st
from audiorecorder import audiorecorder

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

#import streamlit as st
#from st_audiorec import st_audiorec
#from openai import OpenAI

#client = OpenAI(api_key=st.secrets.api_key)

#wav_audio_data = st_audiorec()

#if wav_audio_data is not None:
    # st.audio(wav_audio_data, format='audio/wav')
 #   audio_file= open(wav_audio_data, "rb")
  #  transcription = client.audio.transcriptions.create(
   #     model="whisper-1", 
    #    file=audio_file
    #)
    #print(transcription.text)


