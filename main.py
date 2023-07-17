import speech_recognition as sr
import os
import win32com.client as w
import webbrowser
import openai
from openapi import*
from datetime import datetime




speaker=w.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def inputvoice():
    r= sr.Recognizer()
    with sr.Microphone() as source :
        
        audio=r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language="en-in")
            print(query)
            return query
        except Exception as prob:
            return "the program has occured a error"
        



if __name__ == '__main__':
    say("how may i help you today sir?")
    while True:
        print("Listening......")
        query= inputvoice()
        sites=[["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["anime site","https://www.aniwatch.to/"],["wikipedia","https://www.wikipedia.com/"]]
        for i in sites:
            z=f"open {i[0]}".lower()
            if z in query.lower():
                say(f"right away sir {i[0]} has been opened anything else sir?")
                webbrowser.open(i[1])
        if "the time"in query.lower():
            now = datetime.now()
            time = now.strftime("%H:%M")
            say(f"sir the time is {time}")
        
        
        elif "open ai" in query.lower():
            ai(input=query)
            



        
        


        
        if "thank you" or "close"  in query.lower():
            say("it was an honor to help you sir ")
            say("have a pleasant day")
            say("sir")
            quit()
            
            
            

        