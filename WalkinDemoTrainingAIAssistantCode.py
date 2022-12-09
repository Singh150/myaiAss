import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import speech_recognition as sr #pip install speechRecognition
import pyttsx3
import smtplib
import re
from doubts import *
from answer import *
import numpy as np
#import pandas
engine = pyttsx3.init('sapi5')   #sapi is engine: espeak,nsss
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am counselling taking Robot. Please wait!!!")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio=r.record(source, duration = 4)
        print(audio)
        #audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: {0}\n".format(query))

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


wishMe()
sss=input('Press any key to start Counselling taking robot')
while True:
    # if 1:
    a=0
    count=[]
    query = takeCommand().lower()
    querylist=re.findall(r'\w+',query)
    querylist=np.unique(querylist)
    for q in range(len(ques)):
        a=0
        for i in range(len(querylist)):
            dtt=re.findall(r'\w+',ques[q])
            dtt=np.unique(dtt)
            dtt=' '.join(dtt)
            r=re.findall(r'{0}'.format(querylist[i]),dtt.lower())
            a=a+len(r)
            a
            #print(r,q,a)
        count.append(a)
    quesnumber=count.index(max(count))
    print(ans[quesnumber])
    speak(ans[quesnumber])
    resp=input("press q to exit and c to continue")
    if(resp=='q'):
        break
