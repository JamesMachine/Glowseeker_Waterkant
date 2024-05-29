import streamlit as st
import numpy as np
import soundfile as sf
import base64

st.title("Microphone Input in Streamlit")

# Embed JavaScript to capture audio
st.markdown("""
<script>
const sleep = time => new Promise(resolve => setTimeout(resolve, time))

let mediaRecorder;
let audioChunks = [];

async function recordAudio() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };
    mediaRecorder.start();
}

async function stopRecording() {
    mediaRecorder.stop();
    await sleep(1000); // wait for the recording to finalize

    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    audioChunks = [];
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    const reader = new FileReader();
    reader.readAsDataURL(audioBlob);

    reader.onloadend = function() {
        const base64data = reader.result.split(',')[1];
        const blob = new Blob([Uint8Array.from(atob(base64data), c => c.charCodeAt(0))], { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('file', blob, 'recording.wav');

        fetch('/upload', {
            method: 'POST',
            body: formData,
        }).then(response => {
            console.log('Success:', response);
        }).catch(error => {
            console.error('Error:', error);
        });
    };
}

window.recordAudio = recordAudio;
window.stopRecording = stopRecording;
</script>
""", unsafe_allow_html=True)

if st.button('Start Recording'):
    st.markdown("<script>recordAudio()</script>", unsafe_allow_html=True)

if st.button('Stop Recording'):
    st.markdown("<script>stopRecording()</script>", unsafe_allow_html=True)
