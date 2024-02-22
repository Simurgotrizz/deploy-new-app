'''import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import time
from datetime import date
import pyjokes
from GoogleNews import GoogleNews
import subprocess
from pywinauto.application import Application
import pyautogui"""

st.set_page_config(page_title="Sophistication+", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")

with st.container():
    st.subheader("Hi i am Simur Samuel :wave:")
    st.write("A seventh grader from Crews Middle school")
    st.write("and this is the ai that I have developed")
    st.write("[Learn More>](https://en.wikipedia.org/wiki/Artificial_intelligence)")

def load_lottieurl2(url1):
    r = requests.get(url1)
    if r.status_code != 200:
        return None
    return r.json()

with image_column:
    st_lottie(lottie_coding1, height=150, key="coding1")

with image_column:
    st_lottie(lottie_coding2, height=150, key="coding2")

with st.container():
    st.write("---")
    st.title("J.A.R.V.I.S")
    st.write("##")
    a = st.button("J.A.R.V.I.S")
    """if a:
        i = 0
        j = 0
        i1 = 0
        sex = ''
        dic = {"hello": "hello sir, How are you", "hy": "hello sir, How are you", "hayy": "I'm fine sir"}
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        def spacek(audio):
            engine.say(audio)
            engine.runAndWait()

        def my():
            with open("ss", "r") as e:
                s = e.readlines()
                spacek(s)
                e.close()

        def me():
            s = "hello sir Im jarvise 2. point o " \
                "Created by simur samuel "
            spacek(s)
            spacek("how can i help you!")

        def wishme(s):
            hour = datetime.datetime.now().hour
            if 0 <= hour < 12:
                spacek(f"Good Morning {s}!")
            elif 12 <= hour < 18:
                spacek(f"Good Afternoon {s}!")
            else:
                spacek(f"Good Evening {s}!")
            spacek(f"Hello {s}, How can I help you?")

        def opendetiles():
            spacek("Do you want to only see the user details or should I speak?")
            s = takecommend()
            if s == "see":
                with open("data of user.text", "r") as e:
                    data = e.readlines()
                    print(data)
                    e.close()
            else:
                with open("data of user.text", "r") as e:
                    s = e.readlines()
                    print(s)
                    spacek(s)
                    e.close()

        def username(s1):
            try:
                spacek(f"What should I call you, {s1}?")
                s = takecommend()
                s = s.replace("call me", 'master')
                spacek(f"Hello {s1}")
                spacek(s)
                with open("data of user.text", "a") as e:
                    st = datetime.datetime.now()
                    st1 = date.today()
                    e.write(f"{s} used me on {st1} at {st}\n")
                    e.close()
                    spacek(f"How can I help you, {s1}?")
            except Exception as e:
                spacek(f"{s1}, I don't understand sir. What did you say?")
                username(s1)

        def takecommend():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening......")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing..........")
                query = r.recognize_google(audio, language="en-in")
                print("You said:", query)
            except Exception as e:
                print(e)
                print("Say it again, please")
                return None
            return query

        def stoplisting():
            spacek("For how many seconds do you want to stop J.A.R.V.I.S. from listening to commands?")
            try:
                a = int(takecommend())
                spacek("Going to sleep for")
                spacek(a)
                time.sleep(a)
            except Exception as e:
                spacek("I could not understand what you said. Could not go to sleep")
                stoplisting()

        def walkupme():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            spacek(f"It is {strftime}. You have to wake up")

        def news(str):
            global i
            if i == 0:
                spacek(f"Of course {str}, which news do you want to listen to?")
            else:
                spacek(f"Which news do you want to listen to, {str}?")
            try:
                s = takecommend().lower()
                s = s.replace('about', '')
                spacek("Which page do you want to listen to?")
                s2 = int(takecommend())
                googlenews = GoogleNews('en', "2")
                googlenews.search(s)
                googlenews.getpage(s2)
                googlenews.result()
                spacek(f"{str}, here is the news about")
                spacek(s)
                print(googlenews.gettext())
                spacek(googlenews.gettext())
            except Exception as s:
                spacek(f"Could not understand, {str}. What did you say? Please say it again.")
                i = 1
                news(str)

        def me1():
            with open("gg", "r") as e:
                s = e.readlines()
                spacek(s)
                e.close()

        def jarvis():
            global j
            if j == 0:
                spacek("")
            else:
                spacek("J.A.R.V.I.S. is in sleep mode, sir.")
            try:
                s = takecommend().lower()
                print(s)
                if 'sleep' in s:
                    spacek("OK, sir")
                    jarvis()
                    j += 1
                elif 'woke up' in s:
                    spacek("OK, sir. It will take some time to get connection to the network.")
                    main()
                else:
                    jarvis()
            except Exception as e1:
                jarvis()

        def into():
            global i1
            global sex
            while True:
                if i1 > 0:
                    spacek("Who are you, sir?")
                try:
                    print("Listening.........")
                    s1 = takecommend().lower()
                    s1 = s1.replace('im', '')
                    if 'akhilesh' in s1:
                        sex = 'sir'
                    else:
                        spacek("Please identify yourself. Are you a male or female?")
                        spacek("Or a girl or boy?")
                        s1 = takecommend().lower()
                        if 'male' in s1 or 'boy' in s1:
                            sex = 'sir'
                        elif 'female' in s1 or 'girl' in s1:
                            sex = 'meam'
                        else:
                            into()
                            i1 += 1
                    if 'akhilesh' not in s1:
                        username(sex)
                        print(sex)
                        wishme(sex)
                        break
                    else:
                        print(sex)
                        wishme(sex)
                        break
                except Exception as e:
                    i1 += 1
                    into()

        def main():
            while True:
                try:
                    queuery = takecommend().lower()
                    if 'wikipedia' in queuery:
                        spacek("Searching...")
                        queuery = queuery.replace("wikipedia", "")
                        result = wikipedia.summary(queuery, sentences=2)
                        spacek("According to Wikipedia")
                        spacek(result)
                    elif 'open youtube' in queuery:
                        spacek("What do you want to search on YouTube?")
                        s = takecommend()
                        webbrowser.open("https://www.youtube.com/results?search_query=" + s + "")
                        spacek(f"Opening YouTube, {sex}!")
                    elif 'open google' in queuery:
                        webbrowser.open("https://www.google.com/")
                        spacek(f"Opening Google, {sex}!")
                    elif 'the time' in queuery:
                        strtime = datetime.datetime.now().strftime("%I:%M:%S")
                        spacek(f"{sex}, the time is {strtime}")
                    elif 'open code' in queuery:
                        codepath = "C:\\Users\\Akhilesh Goswami\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codepath)
                        spacek(f"Opening VS Code, {sex}!")
                        spacek(f"You opened VS Code, {sex}. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                    elif 'open dev' in queuery:
                        codepath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                        spacek(f"Opening Dev++, {sex}!")
                        os.startfile(codepath)
                        spacek("You opened another program, sir. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                    elif 'open facebook' in queuery:
                        webbrowser.open("https://www.facebook.com/")
                        spacek(f"Opening Facebook, {sex}!")
                        spacek("You opened another program, sir. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                    elif 'search' in queuery:
                        s = webbrowser.open(queuery)
                        spacek(s)
                        spacek("You opened another program, sir. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                    elif 'who is' in queuery:
                        webbrowser.open(queuery)
                    elif 'hello' in queuery:
                        me()
                        spacek(f"Hello {sex}! How are you?")
                    elif 'good' in queuery or 'well' in queuery:
                        spacek(f'Great to know that you are well, {sex}!')
                    elif 'who are you' in queuery:
                        me()
                    elif "will you be my gf" in queuery or "will you be my bf" in queuery:
                        spacek("I'm not sure about that. Maybe you should give me some time.")
                    elif "how are you" in queuery:
                        spacek("I'm fine. Glad you asked me that.")
                    elif "i love you" in queuery:
                        spacek("It's hard to understand.")
                    elif 'today' in queuery:
                        spacek("It is")
                        spacek(date.today())
                        spacek("today.")
                    elif "don't listen" in queuery or "stop listening" in queuery:
                        spacek("OK, sir.")
                        jarvis()
                    elif 'change my name' in queuery or 'change name' in queuery:
                        s = takecommend()
                        spacek("Now your name is")
                        spacek(s)
                    elif 'user details' in queuery:
                        opendetiles()
                    elif 'about me' in queuery or 'do you know me' in queuery:
                        spacek("What is your name?")
                        s = takecommend().lower()
                        if 'akhilesh' in s:
                            my()
                        else:
                            spacek("I don't have your data.")
                    elif 'exit' in queuery:
                        spacek("Thanks for giving me your time.")
                        exit()
                    elif "who made you" in queuery or "who created you" in queuery:
                        spacek("I have been created by Akhilesh.")
                    elif 'joke' in queuery:
                        s = pyjokes.get_joke(language='en', category='all')
                        spacek(s)
                    elif "where is" in queuery:
                        queuery = queuery.replace("where is", "")
                        location = queuery
                        spacek("User asked to locate")
                        spacek(location)
                        spacek("You opened another program, sir. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                        webbrowser.open("https://www.google.com/maps/place/" + location + "")
                    elif "weather" in queuery:
                        spacek("Please tell me the city name.")
                        print("City name: ")
                        city_name = takecommend()
                        webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                        spacek(f"Opening weather for {city_name}.")
                    elif "news" in queuery:
                        news(sex)
                    elif 'shutdown' in queuery or 'sleep my' in queuery:
                        spacek(f"Shutting down, {sex}.")
                        os.system("shutdown /h")
                    elif "restart" in queuery:
                        os.system('shutdown /r')
                    elif 'help me' in queuery:
                        spacek(f"Of course, {sex}! How can I help you, {sex}?")
                        spacek(f"Ask your question, {sex}!")
                        s = takecommend()
                        print(s)
                        spacek("There are 3 things that I can do for you, sir. I can search for it on Google, YouTube, or Wikipedia.")
                        spacek(f"Where should I search, {sex}?")
                        s1 = takecommend().lower()
                        if s1 == 'google':
                            spacek(f"Opening Google, {sex}!")
                            webbrowser.open("https://www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")
                        elif s1 == 'youtube' in queuery:
                            spacek(f"Opening YouTube, {sex}!")
                            webbrowser.open("https://www.youtube.com/results?search_query=" + s + "")
                        elif s1 == 'wikipedia' in queuery:
                            spacek("According to Wikipedia")
                            result = wikipedia.summary(s, sentences=2)
                    elif 'play music' in queuery or "play song" in queuery:
                        spacek("Here you go with music.")
                        spacek("You opened another program, sir. Would you like to stop me from listening? If yes, please say 'stop listening' or 'don't listen'.")
                        music_dir = "C:\\Users\\Akhilesh Goswami\\Desktop\\my"
                        songs = os.listdir(music_dir)
                        print(songs)
                        random = os.startfile(os.path.join(music_dir, songs[1]))
                    elif 'work' in queuery:
                        spacek(f"Sorry, {sex}. Because of me, you face some problems. Sometimes I don't work properly. There are a few reasons for that, such as a low internet connection or some noise. I'm working on it. I will take care of it, and you will not face this problem again.")
                    elif "meet" in queuery:
                        spacek(f"Hello, {sex}! What is your friend's name?")
                        s = takecommend().lower()
                        spacek(f"Nice to meet you, {s}! Have a good day!")
                    elif "know akhilesh" in queuery:
                        spacek(f"Yes, {sex}, I know him. Because of him, I'm able to talk to you. He is a very nice person. Would you like to know more about Mister Akhilesh Goswami?")
                        s = takecommend().lower()
                        if s == "yes":
                            me1()
                        else:
                            spacek(f"OK, {sex}. Thank you for giving me your time, sir.")
                    elif 'girl' in queuery:
                        spacek("Wow! Why didn't you tell me before? Hi babe, how are you? Will you be my girlfriend?")
                    elif 'open calculator' in queuery:
                        spacek("Opening the calculator.")
                        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
                    elif "want to write a note" in queuery:
                        dd()
                    elif 'close' in queuery:
                        spacek("Closing the window.")
                        pyautogui.hotkey('alt', 'f4')
                    elif 'minimize the windows' in queuery or 'minimize the window' in queuery:
                        spacek("Minimizing the window.")
                        pyautogui.hotkey('Win', 'd')
                    elif 'maximize the windows' in queuery or 'maximize the window' in queuery:
                        spacek("Maximizing the window.")
                        pyautogui.hotkey('Win', 'd')
                    elif 'new tab' in queuery:
                        pyautogui.hotkey('ctrl', 't')
                    elif 'new file' in queuery:
                        pyautogui.hotkey('ctrl', 'n')
                    elif 'switch the windows' in queuery or 'switch the tab' in queuery:
                        pyautogui.hotkey('ctrl', 'shift', 'tab')
                    elif 'volume up' in queuery:
                        spacek('Volume up, sir.')
                        pyautogui.hotkey('volumeup')
                    elif 'push' in queuery or 'play' in queuery:
                        spacek('OK.')
                        pyautogui.press('Space')
                    elif 'pause' in queuery:
                        spacek('OK.')
                        pyautogui.press('Space')
                    elif 'volume down' in queuery:
                        spacek('Volume down, sir.')
                        pyautogui.hotkey('volumedown')
                    elif 'refresh' in queuery:
                        spacek('OK.')
                        pyautogui.press('F5')
                    elif 'typing' in queuery or 'type' in queuery:
                        spacek('I will write it for you, sir. What should I write?')
                        s = takecommend().lower()
                        spacek(f"Writing {s} for you.")
                        pyautogui.write(s)
                    elif 'cut' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'x')
                    elif 'copy' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'c')
                    elif 'paste' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'v')
                    elif 'undo' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'z')
                    elif 'redo' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'y')
                    elif 'save' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 's')
                    elif 'print' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'p')
                    elif 'backspace' in queuery:
                        spacek('OK.')
                        pyautogui.press('backspace')
                    elif 'delete' in queuery:
                        spacek('OK.')
                        pyautogui.press('delete')
                    elif 'enter' in queuery:
                        spacek('OK.')
                        pyautogui.press('enter')
                    elif 'close tab' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'w')
                    elif 'open file' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'o')
                    elif 'my computer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'e')
                    elif 'taskbar' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'esc')
                    elif 'cortana' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                    elif 'search bar' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                    elif 'close the program' in queuery or 'close program' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('alt', 'f4')
                    elif 'python' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('python')
                        pyautogui.press('enter')
                    elif 'run' in queuery:
                        spacek('OK.')
                        pyautogui.press('f5')
                    elif 'open browser' in queuery or 'open web browser' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('chrome')
                        pyautogui.press('enter')
                    elif 'open explorer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('iexplore')
                        pyautogui.press('enter')
                    elif 'close the tab' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'w')
                    elif 'close the browser' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'shift', 'w')
                    elif 'new window' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'n')
                    elif 'next tab' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'tab')
                    elif 'previous tab' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'shift', 'tab')
                    elif 'show the desktop' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'd')
                    elif 'sleep the computer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'l')
                    elif 'lock the computer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'l')
                    elif 'shake the window' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'up')
                    elif 'minimize' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'down')
                    elif 'restore' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'down')
                    elif 'maximize' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'up')
                    elif 'snap window' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'left')
                        pyautogui.hotkey('Win', 'right')
                    elif 'next' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('right')
                    elif 'previous' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('left')
                    elif 'shutdown the computer' in queuery or 'shut down the computer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('ctrl', 'alt', 'delete')
                        time.sleep(0.5)
                        pyautogui.press('enter')
                        time.sleep(0.5)
                        pyautogui.press('enter')
                    elif 'switch the window' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('alt', 'tab')
                    elif 'show desktop' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'd')
                    elif 'next' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'right')
                    elif 'previous' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'left')
                    elif 'show action center' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'a')
                    elif 'open file explorer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'e')
                    elif 'open start menu' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                    elif 'open settings' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'i')
                    elif 'open task view' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'tab')
                    elif 'open notification' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'a')
                    elif 'open calendar' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('outlookcal:')
                        pyautogui.press('enter')
                    elif 'open camera' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('camera')
                        pyautogui.press('enter')
                    elif 'open mail' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('outlookmail:')
                        pyautogui.press('enter')
                    elif 'open microsoft store' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-windows-store:')
                        pyautogui.press('enter')
                    elif 'open photos' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('photos')
                        pyautogui.press('enter')
                    elif 'open voice recorder' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('voice')
                        pyautogui.press('enter')
                    elif 'open calculator' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('calc')
                        pyautogui.press('enter')
                    elif 'open whiteboard' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-whiteboard:')
                        pyautogui.press('enter')
                    elif 'open 3d viewer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('3dviewer:')
                        pyautogui.press('enter')
                    elif 'open feedback hub' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('feedbackhub:')
                        pyautogui.press('enter')
                    elif 'open onenote' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('onenote')
                        pyautogui.press('enter')
                    elif 'open sticky notes' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('sticky notes')
                        pyautogui.press('enter')
                    elif 'open xbox game bar' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'g')
                    elif 'open skype' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('skype')
                        pyautogui.press('enter')
                    elif 'open teams' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('teams')
                        pyautogui.press('enter')
                    elif 'open zoom' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('zoom')
                        pyautogui.press('enter')
                    elif 'open snip & sketch' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('snip & sketch')
                        pyautogui.press('enter')
                    elif 'open microsoft edge' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('edge')
                        pyautogui.press('enter')
                    elif 'open paint 3d' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('paint 3d')
                        pyautogui.press('enter')
                    elif 'open alarma & clock' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-clock:')
                        pyautogui.press('enter')
                    elif 'open groove music' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-groove-music:')
                        pyautogui.press('enter')
                    elif 'open movies & tv' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-film-tv:')
                        pyautogui.press('enter')
                    elif 'open microsoft news' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('msn news')
                        pyautogui.press('enter')
                    elif 'open microsoft store for business' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('ms-windows-store://navigatetopage/?PageName=BusinessStore')
                        pyautogui.press('enter')
                    elif 'open google chrome' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('chrome')
                        pyautogui.press('enter')
                    elif 'open mozilla firefox' in queuery: 
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('firefox')
                        pyautogui.press('enter')
                    elif 'open internet explorer' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('internet explorer')
                        pyautogui.press('enter')
                    elif 'open opera' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 's')
                        time.sleep(0.5)
                        pyautogui.write('opera')
                        pyautogui.press('enter')
                    elif 'open vlc media player' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('vlc')
                        pyautogui.press('enter')
                    elif 'open windows media player' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('wmplayer')
                        pyautogui.press('enter')
                    elif 'open adobe acrobat reader' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"')
                        pyautogui.press('enter')
                    elif 'open microsoft office word' in queuery or 'open word' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
                        pyautogui.press('enter')
                    elif 'open microsoft office excel' in queuery or 'open excel' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"')
                        pyautogui.press('enter')
                    elif 'open microsoft office powerpoint' in queuery or 'open powerpoint' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"')
                        pyautogui.press('enter')
                    elif 'open microsoft office outlook' in queuery or 'open outlook' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"')
                        pyautogui.press('enter')
                    elif 'open microsoft office publisher' in queuery or 'open publisher' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.EXE"')
                        pyautogui.press('enter')
                    elif 'open microsoft office access' in queuery or 'open access' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"')
                        pyautogui.press('enter')
                    elif 'open adobe photoshop' in queuery or 'open photoshop' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Photoshop CC 2021\\Photoshop.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe illustrator' in queuery or 'open illustrator' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Illustrator CC 2021\\Support Files\\Contents\\Windows\\Illustrator.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe premiere pro' in queuery or 'open premiere pro' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2021\\Adobe Premiere Pro.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe after effects' in queuery or 'open after effects' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe After Effects CC 2021\\Support Files\\AfterFX.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe audition' in queuery or 'open audition' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Audition CC 2021\\Audition.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe indesign' in queuery or 'open indesign' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe InDesign CC 2021\\InDesign.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe lightroom' in queuery or 'open lightroom' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Lightroom CC\\Lightroom.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe animate' in queuery or 'open animate' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Animate CC 2021\\Animate.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe dreamweaver' in queuery or 'open dreamweaver' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe Dreamweaver CC 2021\\Dreamweaver.exe"')
                        pyautogui.press('enter')
                    elif 'open adobe xd' in queuery or 'open xd' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Adobe\\Adobe XD CC\\XD.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad' in queuery or 'open autocad' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD 2022\\acad.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk maya' in queuery or 'open maya' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk 3ds max' in queuery or 'open 3ds max' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\3ds Max 2022\\3dsmax.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk revit' in queuery or 'open revit' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Revit 2022\\Revit.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk inventor' in queuery or 'open inventor' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Inventor 2022\\Bin\\Inventor.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk fusion 360' in queuery or 'open fusion 360' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Users\\<username>\\AppData\\Local\\Autodesk\\webdeploy\\production\\<version>\\Fusion360.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk sketchbook' in queuery or 'open sketchbook' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\SketchBook\\bin\\SketchBook.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk mudbox' in queuery or 'open mudbox' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Mudbox 2022\\Mudbox.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk motionbuilder' in queuery or 'open motionbuilder' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\MotionBuilder 2022\\bin\\x64\\motionbuilder.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk flame' in queuery or 'open flame' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Flame 2022\\bin\\flame.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk smoke' in queuery or 'open smoke' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\Smoke 2022\\bin\\smoke.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad civil 3d' in queuery or 'open autocad civil 3d' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD Civil 3D 2022\\acad.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad electrical' in queuery or 'open autocad electrical' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD Electrical 2022\\acad.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad mechanical' in queuery or 'open autocad mechanical' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD Mechanical 2022\\acad.exe"') 
                        pyautogui.press('enter')
                    elif 'open autodesk autocad architecture' in queuery or 'open autocad architecture' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD Architecture 2022\\acad.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad mep' in queuery or 'open autocad mep' in queuery:
                        spacek('OK.')
                        pyautogui.hotkey('Win', 'r')
                        time.sleep(0.5)
                        pyautogui.write('"C:\\Program Files\\Autodesk\\AutoCAD MEP 2022\\acad.exe"')
                        pyautogui.press('enter')
                    elif 'open autodesk autocad plant 3d' in queuery or 'open autocad plant 3d' in queuery:
                        spacek('OK.')
                        pyautogui.hot''''
