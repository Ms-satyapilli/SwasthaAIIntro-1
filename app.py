from turtle import width
import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Swastha AI",page_icon="HEALTH.png",layout="wide")

#nav bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #5EE8CD;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a target="_self" class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a target="_self" class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("script/stype.css")
lottie_coding=load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_dd7yh7kk.json")
img_logo=Image.open("Swastha AI.png")
with st.container():
    left_column,mid_column,right_column=st.columns((1,2,1))
    with left_column:
        st.image(img_logo, width=300)
    with mid_column:
        st.markdown("<h1 style='text-align: center;'>Swastha AI</h1>", unsafe_allow_html=True)
        #st.title("Swastha AI")
        st.markdown("<h6 style='text-align: center;'>It's all in the name of finding cure</h6>", unsafe_allow_html=True)
        #st.subheader("It's all in the name of finding cure")

with st.container():
    st.write("---")
    left_column,right_column=st.columns((1,2))
    with left_column:
        st.header("About Swastha AI:")
        st.write(
           """
                Swastha Al helps doctors to identify the disease based on the symptoms of the patient and helps doctors to predict the medication needed for them. It can also help patients by helping them to save time to identify their disease.
           """       
        )
    with right_column:
        st_lottie(lottie_coding, height=300,key="healthcare")

with st.container():
    st.write("---")
    st.header("Contact Us!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/satyapilli49@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="type your comment here"></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True )
    with right_column:
        st.empty()

 
