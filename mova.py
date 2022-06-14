from datetime import date, time
from os.path import split
from subprocess import run
import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser
import wikipedia
import weather_forecast as wf
import datetime
import random
import secrets
import re


listener = sr.Recognizer()
speak = pyttsx3.init()
def talk(text):
 speak.say(text)
 speak.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk("Yes boss how can i help you")
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'cisco ' in command:
                command=command.replace('cisco','')
                print(command)
                  

    except:
      pass
    return command
def run_mova():
   command = take_command()
   if 'name' in command:
        talk('my name is cisco iam your virtual assistant how can i be helpfull to you')
   else:
       if 'google' in command:
           talk('opening google for you sir please be patient')
           webbrowser.open('www.google.com')
       else:
           if 'youtube' in command:
               talk('opening youtube for you')
               webbrowser.open('www.youtube.com')
           else:
               if 'who is' in command:
                   pers_info=wikipedia.summary(command,1)  
                   talk(pers_info)
               else:
                  if 'date and time' in command:
                      dt=datetime.datetime.now()
                      print(dt)
                      talk(dt)
                  else:
                      
                        
                    if 'netflix' in command:   
                       li=["Breakingbad",'arrow','the walking dead','attack on titans','rick and morty','Vikings','the last kingdom','the hundred','the last dance']
                       ans=secrets.choice(li)
                       talk('while opening netflix i suggest you to watch'+ans)
                       webbrowser.open('www.netflix.com')
                    else:
                        if re.search('weather',command):
                            city=command.split('weather')[-1]
                            weather=wf.forecast(place=city,time='15:46:00',date='2021-02-24',forecast='day')
                            print(str(weather))
                            talk(str(weather))

                              
                
                    

           
    
while True:
    
  run_mova()
  