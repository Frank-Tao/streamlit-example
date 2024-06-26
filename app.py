from huggingface_hub import InferenceClient
from streamlit_chat import message
import streamlit as st

def get_prompt(question: str):
    prompt = f"""<s>[INST] {question} [/INST]</s>
    """
    # prompt = """<s>[INST] What is AI?  [/INST]</s>
    # """
    return prompt

def get_completion(question):    
    client = InferenceClient(
        "mistralai/Mistral-7B-Instruct-v0.1"
    )
    prompt = get_prompt(question)

    res = client.text_generation(prompt, max_new_tokens=300)
    #print (res)
    return res

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Mistral 7B Chatbot")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
user_input = st.chat_input("What would you like to know?")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get bot response (Assuming your get_completion function returns the response text)
    bot_response = get_completion(user_input)
    
    # Display bot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
