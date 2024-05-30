import streamlit as st

#picture = st.camera_input("Scanner")
#
#if picture:
#  st.image(picture)
# st.write("Very Well")

from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="example")











