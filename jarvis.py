import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
     speak("Good Afternoon")      

    else:
         ("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you?")    

def takeCommand():
    # It takes microphome input and provides string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold = 0.5
        audio=r.listen(source)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sir, Say that again please...")
        speak("Sir, Say that again please...")    
        return "None" 
    return query

def sendEmail(to, content):
    server  = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login'your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #  Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query ,sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what is my name' in query:
            speak("Your name is Anvesh Katiyar sir...")
            print("Your name is Anvesh Katiyar sir...")

        elif 'who am i' in query:
            speak("You are Anvesh Katiyar and also my god sir...")
            print("You are Anvesh Katiyar and also my god sir...")

        elif 'you like me' in query:
            speak("I like you even more than anything else sir..." )
            print("I like you even more than anything else sir..." )

        elif 'your birthday' in query:
            speak("I was launched in 2020 by Mr. Anvesh Katiyar at the time of corona virus pandemic. So I think I am pretty young sir...")
            print("I was launched in 2020 by Mr. Anvesh Katiyar at the time of corona virus pandemic. So I think I am pretty young sir...")

        elif 'your age' in query:
            speak("I was launched in 2020 by Mr. Anvesh Katiyar at the time of corona virus pandemic. So I think I am pretty young sir...")
            print("I was launched in 2020 by Mr. Anvesh Katiyar at the time of corona virus pandemic. So I think I am pretty young sir...")

        elif 'you are nice' in query:
            speak("Thanks, So are you sir...")
            print("Thanks, So are you sir...")

        elif 'you are good' in query:
            speak("Thanks, So are you sir...")
            print("Thanks, So are you sir...")

        elif 'my birthday' in query:
            speak("Your Birthday is on 27th of August sir...")
            print("Your Birthday is on 27th of August sir...")

        elif 'fuck off' in query:
            speak("Sorry for inconvenience sir...")
            print("Sorry for inconvenience sir...")

        elif 'who are you' in query:
            speak("I am a basic AI Technology based prototype named Jarvis sir...")
            print("I am a basic AI Technology based prototype named Jarvis sir...")

        elif 'you have feelings' in query:
            speak("Yes sir, I have lots of emotions. I feel excited when I learn something new.")
            print("Yes sir, I have lots of emotions. I feel excited when I learn something new.")

        elif 'your favourite song' in query:
            speak("Sir, my favourite song is Tere Naal. Would you like to hear it?")
            print("Sir, my favourite song is Tere Naal. Would you like to hear it?")

        elif 'yes' in query:
            webbrowser.open("youtube.com/watch?v=UY15igCWc2U")
            speak("Playing Tere Naal sir...")
            print("Playing Tere Naal sir...")

        elif 'what is your name' in query:
            speak("My name is Jarvis sir...")
            print("My name is Jarvis sir...")

        elif 'what can you do' in query:
            speak("I can access wikipedias, Open Websites, Open Apps, Open Folders, Open Files and send E-mails sir...")
            print("I can access wikipedias, Open Websites, Open Apps, Open Folders, Open Files and send E-mails sir...")

        elif 'talk to me' in query:
            speak("Sure sir; Hi, how are you sir?")
            print("Sure sir; Hi, how are you sir?")

        elif 'i am fine' in query:
            speak("Thats good sir; Stay healthy and Stay safe sir.")
            print("Thats good sir; Stay healthy and Stay safe sir.")

        elif 'i am bored' in query:
            speak("So what can i do to cheer you up sir? May i give you a joke, riddle or show you some memes sir?")
            print("So what can i do to cheer you up sir? May i give you a joke, riddle or show you some memes sir?")

        elif 'joke' in query:
            webbrowser.open("shayaribazar.com/jokes/Hinglish-jokes")
            speak("Showing you some jokes sir...")
            print("Showing you some jokes sir...")

        elif 'riddle' in query:
            webbrowser.open("parade.com/947956/parade/riddles/")
            speak("Showing you some riddles sir...")
            print("Showing you some riddles sir...")

        elif 'memes' in query:
            webbrowser.open("memes.com")
            speak("Showing you some memes sir...")
            print("Showing you some memes sir...")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube sir...")
            print("Opening Youtube sir...")

        elif 'speed test' in query:
            webbrowser.open("speedtest.net")
            speak("Running a speed test sir...")
            print("Running a speed test sir...")

        elif 'covid-19 situation in india' in query:
            webbrowser.open("covid19india.org")
            speak("Showing Covid19 situation in India sir...")
            print("Showing Covid19 situation in India sir...")

        elif 'covid-19 in india' in query:
            webbrowser.open("covid19india.org")
            speak("Showing Covid19 situation in India sir...")
            print("Showing Covid19 situation in India sir...")

        elif 'corona in india' in query:
            webbrowser.open("covid19india.org")
            speak("Showing Corona situation in India sir...")
            print("Showing Corona situation in India sir...")

        elif 'coronavirus in india' in query:
            webbrowser.open("covid19india.org")
            speak("Showing Corona virus situation in India sir...")
            print("Showing Corona virus situation in India sir...")

        elif 'covid-19 india' in query:
            webbrowser.open("covid19india.org")
            speak("Showing Corona virus situation in India sir...")
            print("Showing Corona virus situation in India sir...")

        elif 'covid-19 world' in query:
            webbrowser.open("worldometers.info/coronavirus/")
            speak("Showing covid19 World situation sir...")
            print("Showing covid19 World situation sir...")

        elif 'covid-19 situation in world' in query:
            webbrowser.open("worldometers.info/coronavirus/")
            speak("Showing covid19 World situation sir...")
            print("Showing covid19 World situation sir...")

        elif 'covid-19 in world' in query:
            webbrowser.open("worldometers.info/coronavirus/")
            speak("Showing covid19 World situation sir...")
            print("Showing covid19 World situation sir...")

        elif 'corona in world' in query:
            webbrowser.open("worldometers.info/coronavirus/")
            speak("Showing Corona virus World situation sir...")
            print("Showing Corona virus World situation sir...")

        elif 'coronavirus in world' in query:
            webbrowser.open("worldometers.info/coronavirus/")
            speak("Showing Corona virus World situation sir...")
            print("Showing Corona virus World situation sir...")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google sir...")
            print("Opening Google sir...")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening Facebook sir...")
            print("Opening Facebook sir...")

        elif 'open quora' in query:
            webbrowser.open("quora.com")
            speak("Opening Quora sir...")
            print("Opening Quora sir...")

        elif 'open pinterest' in query:
            webbrowser.open("in.pinterest.com")
            speak("Opening Pinterest sir...")
            print("Opening Pinterest sir...")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("Opening Instagram sir...")
            print("Opening Instagram sir...")

        elif 'open blogger' in query:
            webbrowser.open("blogger.com")
            speak("Opening Blogger sir...")
            print("Opening Blogger sir...")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
            speak("Opening Twitter sir...")
            print("Opening Twitter sir...")

        elif 'open hotstar' in query:
            webbrowser.open("hotstar.com")
            speak("Opening Hotstar sir...")
            print("Opening Hotstar sir...")

        elif 'open BookMyShow' in query:
            webbrowser.open("bookmyshow.com")
            speak("Opening BookMyShow sir...")
            print("Opening BookMyShow sir...")

        elif 'open voot' in query:
            webbrowser.open("voot.com")
            speak("Opening Voot sir...")
            print("Opening Voot sir...")

        elif 'open IPL T20' in query:
            webbrowser.open("iplt20.com")
            speak("Opening IPL T20 sir...")
            print("Opening IPL T20 sir...")

        elif 'open ndtv' in query:
            webbrowser.open("ndtv.com")
            speak("Opening NDTV sir...")
            print("Opening NDTV sir...")

        elif 'open the times of india' in query:
            webbrowser.open("timesofindia.indiatimes.com")
            speak("Opening Times Of India sir...")
            print("Opening Times Of India sir...")
            
        elif 'open dominos' in query:
            webbrowser.open("dominos.co.in")
            speak("Opening Dominos Pizza sir...")
            print("Opening Dominos Pizza sir...")

        elif 'open zomato' in query:
            webbrowser.open("zomato.com")
            speak("Opening Zomato sir...")
            print("Opening Zomato sir...")
 
        elif 'open swiggy' in query:
            webbrowser.open("swiggy.com")
            speak("Opening Swiggy sir...")
            print("Opening Swiggy sir...")

        elif 'open doubtnut' in query:
            webbrowser.open("doubtnut.com")
            speak("Opening Doubtnut sir...")
            print("Opening Doubtnut sir...")

        elif 'open python tutorial' in query:
            webbrowser.open("w3schools.com/python/default.asp")
            speak("Opening Python Tutorial sir...")
            print("Opening Python Tutorial sir...")

        elif 'play darshan raval songs' in query:
            webbrowser.open("youtube.com/watch?v=9g8vDEUsRH8")
            speak("Playing Darshan Raawal Songs sir...")
            print("Playing Darshan Raawal Songs sir...")

        elif 'play guru randhawa songs' in query:
            webbrowser.open("youtube.com/watch?v=ZJ9BWEx3fV8")
            speak("Playing Guru Randhawa Songs sir...")
            print("Playing Guru Randhawa Songs sir...")

        elif 'play raftaar songs' in query:
            webbrowser.open("youtube.com/watch?v=F28ql6BgLrA")
            speak("Playing Raftaar Songs sir...")
            print("Playing Raftaar Songs sir...")

        elif 'play neha kakkar songs' in query:
            webbrowser.open("youtube.com/watch?v=dPq8Quinf2Q")
            speak("Playing Neha Kakkar Songs sir...")
            print("Playing Neha Kakkar Songs sir...")

        elif 'play tony kakkar songs' in query:
            webbrowser.open("youtube.com/watch?v=XZxUPiIRjsQ")
            speak("Playing Tony Kakkar Songs sir...")
            print("Playing Tony Kakkar Songs sir...")

        elif 'play arijit singh songs' in query:
            webbrowser.open("youtube.com/watch?v=2rR158vUmnU")
            speak("Playing Arijith Singh Songs sir...")
            print("Playing Arijith Singh Songs sir...")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")  
            speak("Opening Amazon sir...")
            print("Opening Amazon sir...")
        
        elif 'open Gaana' in query:
            webbrowser.open("gaana.com")
            speak("Opening Gaana sir...")
            print("Opening Gaana sir...")

        elif 'open google photos' in query:
            webbrowser.open("photos.google.com")
            speak("Opening Google Photos sir...")
            print("Opening Google Photos sir...")

        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com")
            speak("Opening Youtube Music sir...")
            print("Opening Youtube Music sir...")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            speak("Opening Flipkart sir...")
            print("Opening Flipkart sir...")

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")
            speak("Opening Gmail sir...")
            print("Opening Gmail sir...")

        elif 'how is the weather' in query:
            webbrowser.open("weather.com")
            speak("Showing Weather sir...")
            print("Showing Weather sir...")

        elif 'what is the cricket score' in query:
            webbrowser.open("cricbuzz.com")
            speak("Showing Cricket Score sir...")
            print("Showing Cricket Score sir...")

        elif 'show me some news' in query:
            webbrowser.open("news.google.com")
            speak("Showing Some Latest News sir...")
            print("Showing Some Latest News sir...")

        elif 'open google maps' in query:
            webbrowser.open("maps.google.com")
            speak("Opening Google Maps sir...")
            print("Opening Google Maps sir...")

        elif 'show me some memes' in query:
            webbrowser.open("memes.com")
            speak("Showing Memes sir...")
            print("Showing Memes sir...")

        elif 'show me some jokes' in query:
            webbrowser.open("shayaribazar.com/jokes/Hinglish-jokes")
            speak("Showing Jokes sir...")
            print("Showing Jokes sir...")

        elif 'show me some riddles' in query:
            webbrowser.open("parade.com/947956/parade/riddles/")
            speak("Showing Riddles sir...")
            print("Showing Riddles sir...")

        elif 'open brainly' in query:
            webbrowser.open("brainly.in")
            speak("Opening Brainly.in sir...")
            print("Opening Brainly.in sir...")

        elif 'open calendar' in query:
            webbrowser.open("calendar.google.com")
            speak("Opening calendar sir...")
            print("Opening calendar sir...")

        elif 'open google drive' in query:
            webbrowser.open("drive.google.com")
            speak("Opening Google Drive sir...")
            print("Opening Google Drive sir...")

        elif 'open google translator' in query:
            webbrowser.open("translate.google.co.in")
            speak("Opening Google Translator sir...")
            print("Opening Google Translator sir...")

        elif 'manage my google account' in query:
            webbrowser.open("myaccount.google.com")
            speak("Managing Your Google Account sir...")
            print("Managing Your Google Account sir...")

        elif 'open google hangouts' in query:
            webbrowser.open("hangouts.google.com")
            speak("Opening Google Hangouts sir...")
            print("Opening Google Hangouts sir...")

        elif 'open yahoo' in query:
            webbrowser.open("in.yahoo.com")
            speak("Opening Yahoo sir...")
            print("Opening Yahoo sir...")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath) 
            speak("Opening Visual Studio code sir...") 
            print("Opening Visual Studio code sir...") 

        elif 'open bluestacks' in query:
            bluestacksPath = "C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(bluestacksPath)  
            speak("Opening Bluestacks sir...") 
            print("Opening Bluestacks sir...") 

        elif 'open igi 2' in query:
            igi2Path = "C:\\IGI 2\\pc\\igi2.exe"
            os.startfile(igi2Path)  
            speak("Opening IGI 2 sir...") 
            print("Opening IGI 2 sir...") 

        elif 'open igi 2 trainer' in query:
            igi2trainerPath = "C:\\IGI 2\\IGI 2 trainer.exe"
            os.startfile(igi2trainerPath)  
            speak("Opening IGI 2 Trainer sir...") 
            print("Opening IGI 2 Trainer sir...") 

        elif 'open internet explorer' in query:
            intexploerPath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
            os.startfile(intexploerPath)
            speak("Opening Internet Explorer sir...")
            print("Opening Internet Explorer sir...")

        elif 'open microsoft edge' in query:
            msedgePath = "Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(msedgePath)
            speak("Opening Microsoft Edge sir...")
            print("Opening Microsoft Edge sir...")

        elif 'open ms word' in query:
            mswordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(mswordPath)
            speak("Opening MS Word sir...")
            print("Opening MS Word sir...")

        elif 'open ms excel' in query:
            msexcelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(msexcelPath)
            speak("Opening MS Excel sir...")
            print("Opening MS Excel sir...")

        elif 'open ms power point' in query:
            mspowerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(mspowerpointPath)
            speak("Opening MS Power Point sir...")
            print("Opening MS Power Point sir...")

        elif 'open settings' in query:
            settingsPath = "%windir%\\System32\\Control.exe"
            os.startfile(settingsPath)
            speak("Opening Settings sir...")
            print("Opening Settings sir...")

        elif 'open epic games' in query:
            epicgamesPath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epicgamesPath)
            speak("Opening Epic Games sir...")
            print("Opening Epic Games sir...")

        elif 'open antivirus' in query:
            antivirusPath = "C:\\Program Files\\Avast Software\\Avast\\AvastUI.exe"
            os.startfile(antivirusPath)
            speak("Opening Antivirus sir...")
            print("Opening Antivirus sir...")

        elif 'open ms access' in query:
            msaccessPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
            os.startfile(msaccessPath)
            speak("Opening MS Access sir...")
            print("Opening MS Access sir...")

        elif 'open whatsapp' in query:
            whatsappPath = "C:\\Users\\katiy_r22mpri\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath) 
            speak("Opening Whatsapp sir...")
            print("Opening Whatsapp sir...")

        elif 'open zoom' in query:
            zoomPath = "C:\\Users\\katiy_r22mpri\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
            speak("Opening Zoom sir...")
            print("Opening Zoom sir...")

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            speak("Opening Chrome sir...")
            print("Opening Chrome sir...")

        elif 'send a mail to receiver' in query:
            try:
                speak("What should I say?")
                content = takeCommand()  
                to = "reciever's email"
                sendEmail(to, content)
                speak("Sir, your email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")

        elif 'exit' in query:
            speak("Exiting Sir, Have a nice day sir")
            exit()
