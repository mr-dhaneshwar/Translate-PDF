import streamlit as st
from OCR import *

# Streamlit App
with st.sidebar:
    st.title("PDF Document Uploader")
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf", accept_multiple_files=False)

    if uploaded_file:
        process = st.button("Process..")
        if process:
            st.write("Processing the uploaded PDF. Please wait...")
            st.spinner()
            output_file = perform_ocr(uploaded_file)
            
            if output_file:
                st.download_button(
                    label="Download OCR'd PDF",
                    data=output_file,
                    file_name=f"OCR_{uploaded_file.name}",
                    mime="application/pdf"
                )
