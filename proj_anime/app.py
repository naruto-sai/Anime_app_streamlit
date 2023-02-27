import streamlit as st
import os
from matplotlib import image

st.set_page_config(page_title="Anime Info", page_icon=":guardsman:")

button_style = """
    background-color: white;
    color: #4CAF50;
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    position: relative;
    top: 0px;
    right: -610px;
""" 
style = "font-size: 24px;"

title = "Watashitachi no Animepege ni Irasshaimase min'na!!   :smile: :flag-in:"
text = "Welcome to our anime page Everyone!"

st.header(title)

if st.button("Translate", key="translate_button"):
    st.markdown(f"<p style='{style}'>{text}</p>", unsafe_allow_html=True)

st.markdown( f'<style>.stButton button{{ {button_style} }}</style>', unsafe_allow_html=True )

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
#PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(FILE_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "all.jpg")
st.image(image=image.imread(IMAGE_PATH))