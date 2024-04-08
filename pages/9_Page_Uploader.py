import streamlit as st
import pathlib
import os

uploaded_page = st.file_uploader("Choose a streamlit page", type="py")

def upload():
    if uploaded_page:
        parent_path = pathlib.Path(__file__).parent.parent.resolve()
        save_path = os.path.join(parent_path, "pages", uploaded_page.name)
        
        with open(save_path, "wb") as out:
            out.write(uploaded_page.getvalue())
            print (f"Save file {save_path} completed.")


st.button("Upload", on_click=upload)