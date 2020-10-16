'''
Should tell me the current time
Should tell me the date
Should be able to Greet me when I run the program
Should be able to redirect me to other pages
Everything should be voice controlled
Current window operations like max and min the window
play songs on youtube
search query on google
'''

from speech_recognition import Microphone,Recognizer
import webbrowser as wb
from gtts import gTTS
import pyautogui
import datetime
import os
import time
import subprocess

now = str(datetime.datetime.now())
print(now)
now = now.split()
print(now)
t = now[1].split(':') #for time
hour = int(t[0])
min = int(t[1])
#print(hour)

#greeting the user

if hour < 12:
    greetings = 'Good Morning!'
    lang = 'en'
    obj = gTTS(text=greetings,lang=lang,slow=True)
    obj.save('greetings.mp3')
    os.system('greetings.mp3')
    time.sleep(2)
    pyautogui.moveTo(1910,10)
    pyautogui.click()

elif hour > 12 and hour <16:
    greetings = 'Good Afternoon!'
    lang = 'en'
    obj = gTTS(text=greetings, lang=lang)
    obj.save('greetings.mp3')
    os.system('greetings.mp3')
    time.sleep(1.6)
    pyautogui.moveTo(1910, 10)
    pyautogui.click()

elif hour > 16 and hour<21:
    greetings = 'Good Evening!'
    lang = 'en'
    obj = gTTS(text=greetings, lang=lang)
    obj.save('greetings.mp3')
    os.system('greetings.mp3')
    time.sleep(1.6)
    pyautogui.moveTo(1910, 10)
    pyautogui.click()

#speech recog
print('-----------------------------------')
print()
print('1. SHOW OPERATIONS')
print('2. START OPERATIONS')
print('3. THANKS JARVIS') #to end the process

time.sleep(2)
r = Recognizer()
mic = Microphone()
while True:
    try:
        print()
        print('-----------------------------------')
        print('Speak now')
        print('-----------------------------------')
        print()
        with mic as source:
            audio = r.listen(source)
            voice_text = r.recognize_google(audio)
            try:
                if voice_text == 'start operations':
                    print(voice_text)
                    r1 = Recognizer()
                    mic1 = Microphone()
                    while True:
                        print()
                        print('-----------------------------------')
                        print('What operation?')
                        print()
                        print('1.What is the Time?')
                        print('2.Play Songs on Youtube')
                        print('3.Maximize the current window')
                        print('4.Minimize the current window')
                        print('5.Search dogs on Google')
                        print('-----------------------------------')
                        print()
                        time.sleep(2)
                        with mic1 as source_again:
                            audio1 = r.listen(source_again)
                            command = r1.recognize_google(audio1)
                            if command == 'maximize the window':
                                pyautogui.getActiveWindow().maximize()
                            elif command == 'minimise the window':
                                pyautogui.getActiveWindow().minimize()
                            elif command == 'play songs on YouTube':
                                url = 'https://www.youtube.com/results?search_query=play+songs'
                                wb.get().open_new(url)
                                time.sleep(1)
                                pyautogui.click(220,220)
                                break
                            elif command == 'search dogs on Google':
                                command = command.split(' ')
                                query = command[1]
                                url = f'https: //{query}'
                                wb.get().open_new(url)

                            elif command == 'Open File explorer':
                                subprocess.Popen('C:/Users/91884/Desktop')

                            elif command == 'what is the time':
                                telling_the_time = f'{hour} hours and {min} minutes'
                                lang = 'en'
                                obj = gTTS(text=telling_the_time, lang=lang, slow=True)
                                obj.save('time.mp3')
                                os.system('time.mp3')
                                time.sleep(4)
                                pyautogui.moveTo(1910, 10)
                                pyautogui.click()
                            else:
                                print(command)
                                break

                elif voice_text == 'show operations':

                    print('1.What is the Time?')
                    print('2.Open Social Media Handles')
                    print('3.Play Songs on Youtube')
                    print('4.Maximize the current window')
                    print('5.Minimize the current window')
                    print('6.Search query on Google')

                elif voice_text == 'thanks Jarvis':
                    print('Have a great day!')
                    break
                else:
                    print(voice_text)
            except Exception:
                break
    except Exception:
        break
print('Hope you liked the fun project!')
print('Follow Bhavishya on Linkedin!')