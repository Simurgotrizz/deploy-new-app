import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="NO SIGN UP A.I", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")

with st.container():
    st.subheader("Hi i am Simur Samuel :wave:")
    st.write("A seventh grader from Crews Middle school")
    st.write("I am passionate about learning new parts of python")
    st.write("[Learn More>](https://www.python.org/downloads/)")

def load_lottieurl2(url1):
    r = requests.get(url1)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottieurl2("https://assets9.lottiefiles.com/packages/lf20_2aeiRxOcfs.json")

def load_lottieurl3(url2):
    r = requests.get(url2)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding2 = load_lottieurl3("https://assets9.lottiefiles.com/packages/lf20_itilDAyVNt.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("I like coding and upgrading ai and creating safe agi for humanity")
        st.write("[Learn More>](https://en.wikipedia.org/wiki/Artificial_intelligence)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    text_column, image_column= st.columns(2)
    with text_column:
        st.header("My Projects")
        st.write("##")
        st.write("I am working on an A.I being that you can test out on the bottom and if follow the link bellow it will take you to my e-commerce company Axum.com")
        st.write("[blossooming>](https://buisness-rz76rmkm8gg.streamlit.app/)")

with image_column:
    st_lottie(lottie_coding1, height=150, key="coding1")

with image_column:
    st_lottie(lottie_coding2, height=150, key="coding2")

with st.container():
    st.write("---")
    st.title("J.A.R.V.I.S")
    st.write("##")
    st.button("J.A.R.V.I.S")
