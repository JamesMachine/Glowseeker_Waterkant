import streamlit as st
from st_audiorec import st_audiorec
from openai import OpenAI
import prompt_db
import time

api_key=st.secrets.api_key
client = OpenAI(api_key=api_key)


st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})







wav_audio_data = st_audiorec()
# user_input = None
user_input = """
        Anna Müller, a 22-year-old from Berlin, Germany, has combination skin and is dealing with several common skin concerns. 
        Her primary issues include acne, particularly in the form of inflammatory pimples concentrated around her chin and jawline, 
        indicative of hormonal acne. She also struggles with blackheads, whiteheads, and enlarged pores, especially in her T-zone. 
        Additionally, Anna experiences post-inflammatory hyperpigmentation, uneven skin tone, and occasional dullness, 
        all of which contribute to her desire to prevent early signs of aging. 
        Her skincare routine includes using a gentle foaming cleanser with salicylic acid to control 
        acne, a lightweight, non-comedogenic gel moisturizer with hyaluronic acid and niacinamide to maintain hydration, and spot treatments with benzoyl peroxide.
        She incorporates a BHA exfoliant several times a week to address blackheads and clogged pores and applies a clay mask weekly for deep cleansing. 
        To improve skin texture and brighten her complexion, she has recently started using a vitamin C serum in the morning and a mild retinol cream at night. 
        Anna also consistently uses a broad-spectrum SPF 30 sunscreen daily to protect her skin from UV damage and prevent further pigmentation. 
        She avoids harsh physical exfoliants, over-washing her face, picking or squeezing pimples, heavy comedogenic products, 
        and alcohol-based products to prevent further irritation and maintain her skin's health.
    """


if wav_audio_data is not None:
    # st.audio(wav_audio_data, format='audio/wav')
    with open("recorded_audio.wav", "wb") as f:
            f.write(wav_audio_data)

    audio_file = open("recorded_audio.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    
    user_input = transcription.text

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = [
        {"role": "system", "content": prompt_db.system_content}
    ]





# 
# if user_input:
#     st.session_state.conversation_history.append({"role": "user", "content": user_input})
#     st.session_state.conversation_history, assistant_message = prompt.chat_response(st.session_state.conversation_history)
# 
#     def stream_data():
#         for word in assistant_message.split(" "):
#             yield word + " "
#             time.sleep(0.02)
#     
#     st.write_stream(stream_data)

