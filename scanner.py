import streamlit as st

st.write("Good Bye World")

picture = st.camera_input("Scanner")

if picture:
  st.image(picture)
  st.write("Very Well")
