import speech_recognition as sr
import webbrowser
import time
import playsound
import os,sys
import random
import pyautogui
import requests
from PIL import Image
from time import sleep
from gtts import gTTS
from time import ctime

#Function for linking voice_data
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            ruby_speaks(ask)
        audio=r.listen(source)
        voice_data = ""
        try:
                voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
                ruby_speaks("sorry, can't get you")
        except sr.RequestError:
                ruby_speaks("Sorry, My speech service is down")
        return voice_data
                                    

def ruby_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)




def respond(voice_data):
    #1 what is your name?
    if there_exists(["what is your name","tell me you name"]):
        ruby_speaks("My name is ruby")

    #2 what is the time?
    if "what is the time" in voice_data:
        ruby_speaks(ctime())

    #3 how are you?
    if there_exists(["how are you", "how you doing?"]):
        ruby_speaks("I'm very well, thanks for asking ")

    #4 google search
    if "search for" in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        ruby_speaks("Here is what I found for" + search_term + " on google")

    #5 location
    if "location for" in voice_data:
        location = voice_data.split("for")[-1]
        #url = 'https://www.google.com/maps/search/?api=1&query=' + location + '/&amp;'
        webbrowser.get().open('https://www.google.com/maps/search/?api=1&query=' + location )
        ruby_speaks("here is the location" + location)

    #6 open image
    if "actress" in voice_data:
        ruby_speaks("deepika padukone")
        im = Image.open(r"C:\Users\asus\Downloads\Deepika.jpg")
        im.show()

    #7 weather
    if there_exists(["weather"]):
        weather = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        ruby_speaks("This is the weather at your location")


    #8 take a screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\asus\Pictures\Screenshots\screen.png')
        ruby_speaks("Done")

    #9 tells a joke
    if 'tell me a joke' in voice_data:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            ruby_speaks('Here is an awesome joke for you ')
            ruby_speaks(str(res.json()['joke']))
        else:
            ruby_speaks('oops!I ran out of jokes')


    #10 youtube video
    if "video for" in voice_data:
        search_term = voice_data.split("for")[-1]

        url = 'https://www.youtube.com/results?search_query=' + search_term

        webbrowser.get().open(url)

        ruby_speaks("Here is what I found for" + search_term + " on youtube")



    #11  exit
    if "exit" in voice_data:
        ruby_speaks("bye")
        exit()

time.sleep(1)
ruby_speaks("How can I help you?")

while 1:
    voice_data = record_audio("Recording.....")
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)





