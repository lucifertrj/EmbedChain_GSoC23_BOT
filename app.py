import streamlit as st
from embedchain import App
import os
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
import api

#os.environ['OPENAI_API_KEY'] = api.get_key()
API_KEY = st.secrets['OPENAI_API_KEY']

st.title("My GSoC23 Bot")

articles = st.selectbox("Choose article",[
    'https://medium.com/@jaintarun7/getting-started-with-camicroscope-4e343429825d',
    'https://medium.com/@jaintarun7/multichannel-image-support-week2-92c17a918cd6',
    'https://medium.com/@jaintarun7/multi-channel-support-week3-2d220b27b22a',
    'https://medium.com/@jaintarun7/multi-channel-image-support-week4-d16dc63429be',
    'https://medium.com/@jaintarun7/google-summer-of-code-week-5-6-midterm-evaluation-818c2da0d56d',
    'https://medium.com/@jaintarun7/multi-channel-support-week-7-to-9-3b68ef640e41',
])

# two states
#- generated
#- past
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi, I am a GSoC23 Bot"]
if 'past' not in st.session_state:
    st.session_state['past'] = ['How can you help me?']
        
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()
input_container = st.container()

def generate_response(prompt,data):
    chatbot = App()
    chatbot.add(data)
    response = chatbot.query(prompt)
    return response

with response_container:
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
    
    with input_container:
        input_text = st.text_input("You: ", "", key="input")
    
    if input_text:
        with st.spinner("Generating results..."):
            response = generate_response(input_text,articles)
            st.session_state.past.append(input_text)
            st.session_state.generated.append(response)