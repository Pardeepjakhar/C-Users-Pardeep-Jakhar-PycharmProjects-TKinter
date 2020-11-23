import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime
import time
from  time import ctime
import  requests
import wikipedia
import webbrowser
import  os
import  random
import  sys
import smtplib




r = sr.Recognizer()

def takecommand(ask=False):
    with sr.Microphone() as source:
        print("Listining.......")
        speak("listining....")
        if(ask):
            speak(ask)
        audio = r.listen(source,phrase_time_limit=4)

        text = ''
        try:
            print("Recognizing...")
            text=r.recognize_google(audio)
            print(f"User said: {text}\n")
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print("service is down")

        return text.lower()



def speak(text):
    filename = "test.mp3"
    tts = gTTS(text=text, lang='en-us')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def wishme():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good morning")
    elif hours>=12 and hours<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hello I am Jarvis , sir may i help you!")


if __name__ == '__main__':
    wishme()

    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching for Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print("results")
            speak(results)

        elif 'open youtube' in query:
            speak("Searching for youtube..")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Searching for Google..")
            webbrowser.open("https://google.com")

        elif "open stackoverflow" in query  or 'open stack overeflow' in query:
            speak("Searching for stackoveflow..")
            webbrowser.open("https://stackoverflow.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'music from pc' in query or "music" in query:
            music_folder = 'E:\\haryanvi\\'
            music = ['Star']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')

            os.system(random_music)

        elif 'play hindi music' in query or 'play hindi songs' in query or 'play hindi songs skava' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['ikvaariaa']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')

            os.system(random_music)

        elif 'video from pc' in query or 'video' in query:
            speak("ok i am playing videos")
            video_dir = 'D:\haryanvi'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif "weather" in query :
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak("Here is what I found for on google")

        elif "what is the time" in query or 'tell me time' in query:
                search_term = query.split("for")[-1]
                time = ctime().split(" ")[3].split(":")[0:2]
                if time[0] == "00":
                    hours = '12'
                else:
                    hours = time[0]
                minutes = time[1]
                time = hours + " hour and " + minutes + "minutes"


                speak(time)

        elif "search for"  in query:
            search_term = query.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for" + search_term + "on google")

        elif " youtube"  in query :
            search_term = query.split("for")[-1]
            search_term = search_term.replace("on youtube", "").replace("search", "")
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + "on youtube")

        elif "price of" in query:
            search_term = query.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + " on google")

        elif "Google meet" in query or 'google meet' in query:
            #search_term = query.split("for")[-1]
            url = "https://meet.google.com"
            webbrowser.get().open(url)
            #speak("Here is what I found for " + search_term + " on google")


        elif "where am i" in query:
            Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
            loc = Ip_info['region']
            speak(f"You must be somewhere in {loc}")

        elif "what is my current location" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps")

        elif  "my computer" in query or 'computer' in query :
            speak("which drive you want to open ")
            #der=takecommand()
            #speak(f"you want to open {der} derive")

        elif "whats up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "Tell me motivation Quotes" in query or 'motivate me' in query:
            stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
            highMsgs = ['Dont worry dude,every hard time comes to an end']
            speak(random.choice(stMsgs))
            speak('I think thins Motivated You sir ... if Not')
            speak(random.choice(highMsgs))

        elif "C" in query or 'c' in query or 'SI' in query:
           #search_term = query.split("for")[-1]
           os.startfile("C:")
           speak("i am going to open c derive ")

        elif "D" in query or 'd' in query or  'the' in query:
           #search_term = query.split("for")[-1]
           os.startfile("D:")
           speak("i am going to open d derive ")



        elif "G" in query or 'g' in query or 'ji' in query:
          # search_term = query.split("for")[-1]
           os.startfile("G:")
           speak("i am going to open G derive ")

        elif "F" in query or 'f' in query:
          # search_term = query.split("for")[-1]
           os.startfile("F:")
           speak("i am going to open F derive ")

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = takecommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = takecommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            speak("sorry sir i have not found your query please try later ")

       # time.sleep(30)