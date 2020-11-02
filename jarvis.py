# project on desktop assistant jarvis
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import googlesearch
import webbrowser
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis . Please tell how may i help you ?")
def take():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Reconizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('your email',to,content)
    server.close()
if __name__ == '__main__':
    wishme()
    while True:
        query=take().lower()
        if "wikipedia" in query:
            print("Searching on Wikipedia...")
            speak("Searching on Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print("According to Wikipedia...")
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "yahoo" in query:
            print("Opening Yahoo...")
            speak("Opening Yahoo")
            webbrowser.open("yahoo.com")
        elif 'amazon' in query:
            speak("opening amazon")
            webbrowser.open("amazon.com")

        elif 'flipkart' in query:
            speak("opening flipkart")
            webbrowser.open("flipkart.com")

        elif 'myntra' in query:
            speak("opening myntra")
            webbrowser.open("myntra.com")


        elif 'snapdeal' in query:
            speak("opening snapdeal")
            webbrowser.open("snapdeal.com")


        elif 'shopclues' in query:
            speak("opening shopclues")
            webbrowser.open("shopclues.com")


        elif 'jabong' in query:
            speak("opening jabong")
            webbrowser.open("jabong.com")


        elif 'ajio' in query or 'ajiyo' in query:
            speak("opening ajio")
            webbrowser.open("ajio.com")


            # Code for opening social media sites
        elif 'facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")


        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")


        elif 'linked' in query:
            speak("opening linkedin")
            webbrowser.open("linkedin.com")


        elif 'whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")


        elif 'twitter' in query:
            speak("opening twitter")
            webbrowser.open("twitter.com")

        elif "open youtube" in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif "open stackoverflow" in query:
            speak("opening Stackoverfolw")
            webbrowser.open("stackqverflow.com")

        elif "open google" in query:
            speak("opening Google")
            webbrowser.open("google.com")
        elif "google about" in query:
                try:
                    from googlesearch import search
                    print("Please tell me what should I google about?")
                    speak("Please tell me what should I google about?")
                    to_search=take()
                    speak(f"User said:{to_search}\n")
                    speak("According to Google,these are the websites where you can find the results of yoyr query.")
                    all=search(to_search,num_results=5)
                    for j in all:
                        print(j)
                        speak(j)
                    print("Enter the number of website you want to open.")
                    speak("Enter the number of website you want to open.")
                    w=int(input())
                    w-=1
                    webbrowser.open(all[w])

                except Exception as e:
                    print("I am sorry. I cannot find this at the moment.")
                    speak("I am sorry. I cannot find this at the moment.")
        elif  "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir , the time is {strTime}")
        elif "play music" in query:
            music_dir="E:\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "open atom" in query:
            path="C:\\Users\\NAMAN SINGLA\\AppData\\Local\\atom\\atom.exe"
            os.startfile(path)
        elif "open harry potter" in query:
            path="E:\\Holloywood Movies\\Harry Potter\\Harry Potter 1 and the Philosopher's Stone.avi"
            os.startfile(path)
        elif "email to naman" in query:
            try:
                speak("What should i say!")
                content=take()
                to="sender's email"
                sendemail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                print("Sorry Sir I am not able to send the email")
                speak("Sorry Sir I am not able to send the email")
        elif "quit" in query:
            print("Thank You very much for your time . Good Bye .")
            speak("Thank You very much for your time . Good Bye .")
            exit()
# project completed by Naman Singla
# project requirements
# 1.python-3.8.3
# 2.pip install wikipedia for wikipedia
# 3.pip install SpeechRecognition for  SpeechRecognition
# 4.pip install pipwin and pipwin install pyaudio for support in SpeechRecognition module
# 5.pip install pyttsx3 for voices
# 6.pip install pywin32 for error of sapi5
# 7.pip install googlesearch-python for search purpose
