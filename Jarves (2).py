import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import keyboard
import wikipedia as googlescrap
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from keyboard  import press_and_release
from keyboard  import press
import datetime
from time import sleep
import pyjokes
import webbrowser as web
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',130)
engine.setProperty('volume',0.8)


def speak(audio): 
    print(" ")
    engine.say(audio)
    print(f": {audio}")
    print(" ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning,sir!")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir ")
        

    else:
        speak("Good Evening,sir!")

    speak("i am online ,sir")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}") 
    
    except Exception as e:
        print("say that again please....")
        return "None"
    return query

def SpeedTest():
    import speedtest
    speak("checking ,speed......")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctdown = int(downloading/8000000)
    uploading = speed.upload()
    correctUpload = int(uploading/8000000)

    if'check uploading speed' in query:
        speed(f"the Uploading Speed Is {correctupload}mbp s")

    elif'check downloading speed' in query:
        speak(f"the Downloading speed Is {correctdown}mbp s")

    else:
        speak(f"the Downloading is {correctdown} and the uploading speed is{correctUpload} mbp s")

def Temp():
    search = "temprature in patna"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The Temperature outside  is{temperature} celcius")


if __name__ == "__main__":
    
    wishMe()

    while True:
      query = takecommand().lower()

 # logic for excuting task based on query

      if 'wikipedia' in query:
         speak("Searching wikipedia")
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=3)
         speak("According to wikipedia")
         print(results)
         speak(results)
        
      elif'hello jarvis'in query:
          speak("hello,sir")

      elif 'open whatsapp' in query:
           webbrowser.open("https://web.whatsapp.com/")
           speak("wait a second")

      elif 'open google' in query:
               webbrowser.open("google.com")
               speak("opening,google,wait a second")

      elif ' time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:")
           speak(f"sir, the time is: {strTime}")

      elif 'open wordpad' in query:
         os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\wordpad.exe")
         speak("ok,sir wait a second")

      elif 'take a break' in query:
             speak("ok,sir")
             speak("have a nice day,sir")
             os.startfile("D:\Wake up")
             break 

      elif 'who are you' in query:
          speak("i am your persional assistant,jarvis sir")
          
      elif 'how are you jarves' in query:
          speak("i am fine sir")
          speak ("How are you  sir")
          
      elif 'how are you ' in query:
          speak("i am fine sir")
          speak ("How are you  sir")
          
      elif 'I am good' in query:
          speak("Happy to know,sir ")
          

      elif 'tell me about yourself' in query:
          speak("My name is jarves and i am your persional assistant,sir")
           
      elif 'how old are you' in query:
          speak("I was launched in 2020,but i am wise beyond my years")
             
             
      elif 'good morning'in query:
          speak("Good morning ,sir")

      elif 'good job ,Alex'in query:
          speak("Thank you ,sir")

      elif 'good job' in query:
          speak("Thank you,sir")

      elif'what is your name' in query:
          speak("my name is  jarvis ")

      elif'college song'in query:
          os.startfile("E:\\my fav song\\collagesong.mp4")
          speak("ok,sir")
          sleep(180)

      elif'mahiya song'in query:
              os.startfile("E:\\my fav song\\mahiya.mp4")
              speak("ok,sir")
              sleep(300)

      elif'jagdish song'in query:
              os.startfile("E:\\my fav song\\jagdish.mp4")
              speak("ok,sir")
              sleep(280)

      elif'ek bari song'in query:
              os.startfile("E:\\my fav song\\ek baari.mp4")
              speak("ok,sir")
              sleep(300)

      elif'friend song'in query:
              os.startfile("E:\\my fav song\\friends.mp4")
              speak("ok,sir")
              sleep(240)

      
      elif 'play my song' in query:
             os.startfile("E:\\my fav song\\mererang.mp4")
             speak("ok,sir wait a second") 
             sleep(240) 
      
      elif 'downloading speed' in query:
          SpeedTest()

      elif 'uploading speed' in query:
           SpeedTest()

      elif 'internet speed' in query:
          SpeedTest()

      
      elif'search' in query:
         import pywhatkit
         query = query.replace("jarves","")
         query = query.replace("google search","")
         query = query.replace("google","")
         speak("this is what i found on the web!")
         pywhatkit.search(query)

         try:
              result = googlescrap.summary(query,2)
              speak(result)

         except:
              speak("no found data")

      elif'temperature' in query:
          Temp()

      elif'how to' in query:
          speak("wait a second")
          op = query.replace("jarves","")
          max_result = 1
          how_to_func = search_wikihow(op,max_result)
          assert len(how_to_func)==1
          how_to_func[0].print()
          speak(how_to_func[0].summary)

      elif'open facebook'in query:
          webbrowser.open('https://www.facebook.com/')
          speak("ok,sir,wait a second")

      
      elif'open youtube'in query:
          webbrowser.open('https://www.youtube.com/')
          speak("ok ,sir")
    
      elif'i am also fine' in query:
          speak(" Happy to know  ,sir")
           
      elif'open vs' in query:
           os.startfile("C:\\Users\\Hario Om\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
           speak("wait a second")

      elif'open telegram'in query:
          os.startfile("C:\\Users\\Hario Om\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
          speak("as u wish")

      elif'open my pc'in query:
          os.startfile("C:\\Users\\Hario Om\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools")
          speak("ok ,sir")

      elif'open lms'in query:
          os.startfile("https://lms.galgotiasuniversity.edu.in//my//")
          speak("ok ,sir")

      elif'open icloud'in query:
              os.startfile("https://gu.icloudems.com//corecampus//student//student_index.php")
              speak("ok ,sir")
              
      
      elif'open movie list'in query:
              os.startfile("E:\Movie")
              speak("ok ,sir")
      
      
      elif'open your file'in query:
              os.startfile("D:\Jarvis")
              speak("ok ,sir")
      

      elif'open chrome' in query:
          os.startfile("C:\\Users\\Hario Om\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
          speak("as u wish,sir")

      
      elif'open prime' in query:
              os.startfile("https://www.primevideo.com//ref=av_auth_return_redir")
              speak("ok,sir")

      elif'close vs code'in query:
          os.system("TasKill /F /in Code.exe")
          speak("ok,sir")

      elif'close chrome'in query:
          os.system("TasKill /F /in chrome.exe")
          speak("As u wish")

      elif'open brave'in query:
          os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
          speak("As your command,sir")
         
     

      elif'exit'in query:
          speak("ok,sir")
          speak("Have a nice day,sir")
          break 

      elif'stop'in query:
          keyboard.press('space bar')
          speak("done,sir")

      elif'skip' in query:
          keyboard.press('l')

      elif'mute'in query:
          keyboard.press('m')
          speak("ok,sir")

      elif'full screen'in query:
          keyboard.press('f')
          speak("done,sir")
        
      elif'new tab'in query:
            press_and_release('ctrl +  t')

      elif'close tab'in query:
            press_and_release('ctrl + w')
        
      elif'new window'in query:
            press_and_release('ctrl + n ')

      elif'select all' in query:
          press_and_release("ctrl + A ")

      elif'delete'in query:
          press_and_release("shift+delete")
      
      elif'shutdown' in query:
          press_and_release("alt+f4")
          press("enter")
          speak("As you wish ,sir")

      elif'close' in query:
          press_and_release("alt+f4")
      
      elif'joke' in query:
          get = pyjokes.get_joke()
          speak(get)
      
      elif'play' in query:
         import pywhatkit
         query = query.replace("jarves","")
         query = query.replace("youtube video","")
         query = query.replace("youtube","")
         speak("this is what i found on the youtube!")
         pywhatkit.playonyt(query)
         sleep(240)

      elif'what is your age ' in query:
          speak("i was launched in 2020 but i am wise beyond my years")
         
      elif'open translation'in query:
          webbrowser.open("https://translate.google.co.in/?hl=en&tab=rT&sl=hi&tl=en&op=translate")
          speak("sure ,sir")
     
      elif'who,s your creator' in query:
          speak("my creator is priyanshu kumar.")

      elif'what is the current location' in query:
          speak("greater noida,knowladge park 3")
        
      elif'where i am' in query:
          speak("you are  in your Pg")

      elif'who is your creator' in query:
          speak("Its confidential")
         
      elif'your creator name' in query:
          speak("Its confidential")

      elif'what is my IP address' in query:
          speak("sir, your IP address is 192.168. 0.1")
          
      elif'jarvis' in query:
          speak("yes,sir")
               

