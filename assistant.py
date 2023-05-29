import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import smtplib
import requests
from bs4 import BeautifulSoup
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from plyer import notification
import speedtest
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from googletrans import Translator
import requests
import pywhatkit as kit
import socket
sg = sendgrid.SendGridAPIClient(api_key='YOUR_SENDGRID_API_KEY')

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Sir") 
        print("Good Morning,Sir")    
    elif hour>=12 and hour<18:
          speak("Good Afternoon,Sir")
          print("Good Afternoon,Sir")
    else:
        speak("Good Evening,Sir")
        print("Good Evening,Sir")
    speak("I Am Your Virtual Assistant Royal, Please Tell Me How May I Help You")  
    print("I Am Your Virtual Assistant Royal, Please Tell Me How May I Help You")

def takecommand():
    #it take microphone input from user and returns as string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e) 
        speak('Say that again please')   
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__=="__main__" :
    wishme()
    while True:
        query=takecommand().lower()
    #logic for executing task based on query
        if "how are you" in query:
            speak("I am Great Sir, How are you?")
        elif "i am fine" in query:
            speak("Great to hear that sir")
        elif 'close' in query:#to close the program
            speak("Ok sir i am sleeping, you can call me anytime")
            print("Ok sir i am sleeping, you can call me anytime")
            exit()
            break
        
        elif 'date and time' in query:#to ask time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            today = date.today() 
            print("Sir,  the date is",today)
            speak(f"Sir, the date is {today}")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'email' in query:#to send email
            try:
                speak("Sending Email Sir")
                print("Sending Email Sir")
                # Define the sender and recipient email addresses
                sender_email = "mithungr67@gmail.com"
                recipient_email = input("Enter Recipient Email address:-")

                # Define the email message
                message = input("Enter Message to be sent:- ")

                # Connect to the SMTP server
                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.starttls()
                    smtp.login(sender_email, "mxagowyzobjipaho")

                # Send the email message
                    smtp.sendmail(sender_email, recipient_email, message)
                    speak("Email Sent Successfully Sir")
                    print("Email Sent Successfully Sir")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif "weather" in query:#to check the weather
            search = "temperature in bangalore"
            search1="humidity in Bangalore"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
            print({search},"\n",{temp})
        
        elif "internet speed" in query:# to print internet speed
            speak("Gathering Data sir")
            print("Gathering Data....   ")
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net,"mbps")
            print("Wifi download speed is ",download_net,"mbps")
            speak(f"Wifi Upload speed is {upload_net}mbps")
            speak(f"Wifi download speed is {download_net}mbps")
        
        elif "open folder" in query:
            folder_path = r"E:\AI&ML"
            os.startfile(folder_path)
        
        elif "create folder" in query:
            folder_path = r"F:\internals"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print("New folder created!")
            else:
                print("Folder already exists.")
                
        elif "news" in query:
            url = 'https://newsapi.org/v2/top-headlines'
            params = {
                'country': 'in',
                'apiKey': 'ea683342df7b4b24937003f123365e8b'
             } # Replace with your News API key
            
# Make the API request and get the response data
            response = requests.get(url, params=params)
            news_data = response.json()

# Print the top headlines
            for article in news_data['articles']:
                print(article['title'])
                print(article['description'])
                print()
                speak(article['title'])

#to search in google
        elif "search" in query:
            speak("Type to search Sir")
            print("Type to search Sir")
            kit.search(input("Search:- "))
            speak("Ok sir i am sleeping, you can call me anytime")
            print("Ok sir i am sleeping, you can call me anytime")
            break

#to play a video on youtube
        elif "youtube" in query:
            speak("Type to Search Sir")
            print("Type to search Sir")
            kit.playonyt(input("Search for your video:-"))
            speak("Ok sir i am sleeping, you can call me anytime")
            print("Ok sir i am sleeping, you can call me anytime")
            break

        elif "ip address" in query:
            # Get the IP address of the local computer
            local_ip = socket.gethostbyname(socket.gethostname())
            print("Local IP address:", local_ip)
            speak(f"Local IP address is:{local_ip}" )

            # Get the IP address of a remote host
            remote_host = "www.google.com"
            remote_ip = socket.gethostbyname(remote_host)
            print("Remote IP address of", remote_host, ":", remote_ip)
            speak(f"Remote IP address of{remote_host} is {remote_ip}")
            







    
            
