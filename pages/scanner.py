import streamlit as st

picture = st.camera_input("Scanner")

if picture:
  st.image(picture)
 st.write("Very Well")












