import streamlit as st
from streamlit_chat import message


def on_input_change():
    user_input = st.session_state.user_input
    print('*')
    print(st.session_state.user_message)
    print('*')
    print(st.session_state.agent_message)
    print('*')


    st.session_state.user_message.append(user_input)
    st.session_state.agent_message.append('agent message')

    print('*')
    print(st.session_state.user_message)
    print('*')
    print(st.session_state.agent_message)
    print('*')


def on_btn_click():
    del st.session_state.user_message[:]
    del st.session_state.agent_message[:]

st.session_state.setdefault(
    'user_message', 
    ['hello i am user']
)
st.session_state.setdefault(
    'agent_message', 
    ['hello i am agent']
)

st.title("Autogen UI")

chat_placeholder = st.empty()

with chat_placeholder.container():
    for i, message_ in enumerate(st.session_state.agent_message):
        message(message_, key=f"{i}_agent")

    for i, message_ in enumerate(st.session_state.user_message):
        message(message_, is_user=True, key=f"{i}_user")

    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
