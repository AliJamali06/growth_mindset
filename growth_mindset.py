
# my code 
import streamlit as st
import pytesseract
from PIL import Image
import os

# set the path to Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# stresamlit Ui
st.title("Image to Text Converter")
st.write("Upload to Text to extract text.")

# Upload image
uploaded_file = st.file_uploader("chose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file: # file is upload before processing
    #open the image
    image = Image.open(uploaded_file)
   
   # display the image

    st.image(image, caption="uoloaded Image", use_container_width=True)
    
    # Extract text
    st.subheader("Extracted Text:")
    extracted_text = pytesseract.image_to_string(image)
  
     # display extracted text
    st.text_area("Text Output", extracted_text, height=200)

    # download extracted text as file
    st.download_button("Download Text File", extracted_text, file_name="extracted_text.txt")
   