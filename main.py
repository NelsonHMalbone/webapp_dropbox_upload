import os, dropbox, dotenv
import streamlit as st


# centering the title
st.title("Dropbox File Uploader")

with st.form('drop file', enter_to_submit=False):
    form_one = st.write("Choose a file to upload")
    file_uploader = st.file_uploader('Drag and drop file here')
    # putting the button on the upload button to the right
    with st.columns(3)[0]:
        file_name = st.write(f'FileName: ')
        file_cap = st.write(f'File Size: ')
        submitBTN = st.form_submit_button('Upload')