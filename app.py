# from flask import Flask, render_template, request

# # Import your personal assistant code
# from personalassistant import wishMe, username, takeCommand

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/command', methods=['POST'])
# def execute_command():
#     command = request.json['command']
#     # Call your personal assistant function here and get the output
#     output = process_command(command)
#     return {'output': output}

# if __name__ == '__main__':
#     app.run(debug=True)


# import streamlit as st
# import wave
# import webrtcvad
# import pyaudio
# import time
# import subprocess
# import os

# def record_audio(file_path, duration=5):
#     chunk = 1024
#     sample_format = pyaudio.paInt16
#     channels = 1
#     rate = 16000
#     frames = []

#     p = pyaudio.PyAudio()

#     stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=rate,
#                     frames_per_buffer=chunk,
#                     input=True)

#     st.info("Recording started. Speak into the microphone.")

#     for _ in range(int(rate / chunk * duration)):
#         data = stream.read(chunk)
#         frames.append(data)

#     st.info("Recording completed.")

#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     wf = wave.open(file_path, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(sample_format))
#     wf.setframerate(rate)
#     wf.writeframes(b''.join(frames))
#     wf.close()

# st.title("Personal Assistant")
# robot_image = "robot.png"  # Replace with the path to your robot image
# st.image(robot_image, width=200)

# if st.button("Start Assistant"):
#     # Define file path for recording audio
#     file_path = "audio.wav"

#     # Record audio
#     record_audio(file_path)

#     # Run personal assistant code
#     process = subprocess.Popen(["python", "personalassistant.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()

#     # Display assistant output
#     if stdout:
#         st.success(stdout.decode("utf-8"))
#     if stderr:
#         st.error(stderr.decode("utf-8"))

#     # Remove audio file
#     os.remove(file_path)



import os
import streamlit as st
from streamlit.components.v1 import html


current_directory= os.getcwd()

script_path = os.path.abspath(__file__)
# st.write("Script Path:", script_path)


# Read the contents of the index.html file
with open('sticky.html', 'r') as file:
    index_html = file.read()

# Define the CSS and JS files
css_file = "sticky.css"
js_file = "https://code.jquery.com/jquery-3.6.0.min.js"

# Display the index.html file in the left half
col1, col2 = st.columns([30, 5])
with col1:
    # Load the CSS file
    # st.markdown(f'<link rel="stylesheet" href="{css_file}">', unsafe_allow_html=True)
    # Load the index.html content
    html(f'<style>{open(css_file).read()}</style>{index_html}', height=1000, scrolling=False)
    
with col2:
    st.title("Personal Assistant")
    robot_image = "robot.png"  # Replace with the path to your robot image
    st.image(robot_image, width=200)

    
    
    
    
    if st.button("Start Assistant"):
        import speech_recognition as sr
        import pyttsx3
        import datetime
        import wikipedia
        import webbrowser
        import os
        import time
        import subprocess
        from ecapture import ecapture as ec
        import wolframalpha
#     import json
        import cv2
        from PIL import Image
        import requests
        import shutil
#     from urllib.request import urlopen
        
        engine=pyttsx3.init('sapi5')   #windows/ ms api to get voice
        voices= engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        
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
                speak(" I AM YOUR PERSONAL ASSISTANT")
        
        def username():
                speak("What should i call you?")
                uname = takeCommand()
                speak("Welcome")
                speak(uname)
                columns = shutil.get_terminal_size().columns
                        
                print(f"Welcome {uname}") # uname.center(columns))
                        
                speak("How can i Help you?")
        def takeCommand():
                ''' to take input from user
                        '''
                r=sr.Recognizer() #class to recognize audio
                with sr.Microphone() as source:
                        print("Listening...")
                        r.pause_threshold= 0.5
                        audio=r.listen(source)
                try:
                        print("Recognizing...")
                        query= r.recognize_google(audio, language='en-in')
                        print(f"Did you say :{query}\n")
                except Exception as e:
                        print("Say that again please...")
                        return "None"
                return query
        if __name__=="__main__":
                wishMe()
                username()
                while True:
                        query=takeCommand().lower()
                                #logic to execute tasks
                        if "goodbye" in query or "okay bye" in query or "stop" in query or 'shut up' in query or 'bye' in query :
                                speak('your personal assistant  is shutting down,Good bye')
                                print('your personal assistant  is shutting down,Good bye')
                                assistant_running = False
                                break
                        if 'wikipedia' in query:
                                speak('Searching wikipedia')
                                query=query.replace("wikipedia","")
                                results =wikipedia.summary(query, sentences=2)
                                speak("Acccording to wikipedia")
                                print(results)
                                speak(results)

                        elif 'open youtube' in query:
                                webbrowser.open_new_tab("https://www.youtube.com")
                                speak("youtube is open now")
                                time.sleep(5)
                        elif 'open google' in query:
                                webbrowser.open_new_tab("https://www.google.com")
                                speak("Google chrome is open now")
                                time.sleep(5)
                        elif 'open gmail' in query:
                                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                                speak("Google Mail open now")
                                time.sleep(5)
                        elif 'time' in query:
                                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                                speak(f"Its {strTime}")
                
                        elif 'who are you' in query or 'what can you do' in query or " you programmed for" in query:
                                speak('I am NOTEHUB your persoanl assistant. I am programmed to minor tasks like'
                                        'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                                'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

                        elif "who made you" in query or "who created you" in query or "who discovered you" in query or 'who built you' in query:
                                speak("I was built by Pooja")


                        elif "open stack over flow" in query or "open stackover flow" in query or "open stack overflow" in query or "open stackoverflow" in query:
                                webbrowser.open_new_tab("https://stackoverflow.com/")
                                speak("Here is stackoverflow")

                        elif "camera" in query or "take a photo" in query or "take a picture" in query:
                                cap = cv2.VideoCapture(0)
                                ret, frame = cap.read()
                                cap.release()
                                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                                st.image(image, caption="Captured Image", use_column_width=True)
                        elif "spotify" in query:
                                webbrowser.open_new_tab("https://open.spotify.com/")
                                speak("Here is spotify")

                        elif "weather" in query or 'temperature' in query:
                                api_key="8ef61edcf1c576d65d836254e11ea420"
                                base_url="https://api.openweathermap.org/data/2.5/weather?"
                                speak("whats the city name")
                                city_name=takeCommand()
                                complete_url=base_url+"appid="+api_key+"&q="+city_name
                                response = requests.get(complete_url)
                                x=response.json()
                                if x["cod"]!="404":
                                        y=x["main"]
                                        current_temperature = y["temp"]
                                        current_humidiy = y["humidity"]
                                        z = x["weather"]
                                        weather_description = z[0]["description"]
                                        speak(" Temperature in kelvin unit is " +
                                                str(current_temperature) +
                                                "\n humidity in percentage is " +
                                                str(current_humidiy) +
                                                "\n description  " +
                                                str(weather_description))
                                        print(" Temperature in kelvin unit = " +
                                                str(current_temperature) +
                                                "\n humidity (in percentage) = " +
                                                str(current_humidiy) +
                                                "\n description = " +
                                                str(weather_description))

                                else:
                                        speak(" City Not Found ")
                        elif 'news' in query:
                                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                                speak('Here are some headlines from the Times of India,Happy reading')
                                time.sleep(6)

                        elif "log off" in query or "sign out" in query:
                                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                                subprocess.call(["shutdown", "/l"])
                        elif 'how are you' in query:
                                speak("I am fine, Thank you")
                                speak("How are you?")

                        elif 'fine' in query or "good" in query:
                                speak("It's good to know that your fine")

                        elif 'ask' in query or 'calculate' in query:
                                speak('I can answer to computational and geographical questions and what question do you want to ask now')
                                question=takeCommand()
                                app_id="R2K75H-7ELALHR35X"
                                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                                res = client.query(question)
                                answer = next(res.results).text
                                speak(f" The result of your query is {answer}")
                                print(answer)
                        elif "write a note" in query or "convert to text" in query or"make a note" in query or "write note" in query or "take notes" in query:
                                speak("What is the name of file? Note this will be a text file")
                                name=takeCommand()
                                speak("What should i write?")
                                note = takeCommand()

                                directory_path = r"D:/projects/MINI"
                                file_path = os.path.join(directory_path, f"{name}.txt")
                                st.write(file_path)

                                with open(file_path, 'w') as file:
                                        file.write(note)
                        
                                # file = open(f"{name}.txt", 'w')
                                # file.write(note)
                                speak("I have saved your note. To view say say show note")

                        elif "show note" in query or "view note" in query or 'open a file' in query:
                                speak("what is the name of the note or file you want to open?")
                                name_show=takeCommand()
                                directory_path = r"D:/projects/MINI"
                                speak("Showing Notes")
                                file_path = os.path.join(directory_path, f"{name_show}.txt")
                                if os.path.exists(file_path):
                                        with open(file_path, "r") as file:
                                                note_contents = file.read()
                                                st.write("Note preview:")
                                                st.write(note_contents[:200])
                                

                        
                
                        elif "will you be my gf" in query or "will you marry me?" in query:  
                                speak("I'm not sure about it, may be you should give me some time")

                        elif "how are you" in query:
                                speak("I'm fine, glad you asked me that")

                        elif "i love you" in query:
                                speak("Sorry,It's hard to understand. Love is Complicated")

                        elif "you think" in query :
                                speak("Sorry I am not programmed to think on my own\n")

                        elif "none" in query:
                                speak("Please repeat clearly\n")

                        else:
                                webbrowser.open_new_tab(f"https://www.google.com/search?q={query}&rlz=1C1GCEA_enIN989IN989&oq={query}&aqs=chrome..69i57j0i433i512l2j0i512j0i433i512j69i61l3.3188j0j7&sourceid=chrome&ie=UTF-8")
                                time.sleep(3)

                st.markdown("<span style='color:red;'>Say 'stop' to shutdown the assistant</span>", unsafe_allow_html=True)

                time.sleep(3)







