import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Simur.inc", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")

with st.container():
    st.subheader("Hi i am Simur Samuel :wave:")
    st.write("A seventh grader from Crews Middle school")
    st.write("i am passionate about learning new aspects of python programming it is a very easy and efficent way to code")
    st.write("[Learn More>](https://www.python.org/downloads/)")

def load_lottieurl2(url1):
    r = requests.get(url1)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottieurl2("https://assets1.lottiefiles.com/packages/lf20_yy8zQVN03K.json")

def load_lottieurl3(url2):
    r = requests.get(url2)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding2 = load_lottieurl3("https://assets6.lottiefiles.com/packages/lf20_fN91t3YtTf.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("what I do is I like to build electronic objects then code them I usually use the arduino as my main board but I also code in python")
        st.write("[Learn More>](https://www.bing.com/search?pglt=41&q=arduino&cvid=fb5ca6b44f8d46b99846f6520be41805&aqs=edge.1.69i57j46j0l2j46j0l4.2516j0j1&FORM=ANNTA1&PC=HCTS)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    text_column, image_column= st.columns(2)
    with text_column:
        st.header("My Projects")
        st.write("##")
        st.write("My latest projects are a bionic arm that is alomst finished i just need to find a cable to attach the motherboard to my computer to transfer the code and the other one is a arduino controlled alpha-bot that i do not know how to use but im done building it.")

with image_column:
    st_lottie(lottie_coding1, height=150, key="coding1")

with image_column:
    st_lottie(lottie_coding2, height=150, key="coding2")

with st.container():
    st.write("---")
    text1_column, game_column= st.columns(2)
    with text_column:
        st.header("Games")
        st.write("##")
        st.write("[Subway Surfers>](https://poki.com/en/g/subway-surfers)")
        st.write("[Fireboy and lavagirl>](https://www.coolmathgames.com/0-fireboy-and-water-girl-in-the-forest-temple)")
        st.write("[Motorx3m>](https://poki.com/en/g/moto-x3m)")
        st.write("[Stickman hook>](https://poki.com/en/g/stickman-hook)")
        st.write("[Temple run 2>](https://poki.com/en/g/temple-run-2)")
