# Description: this is my first try to create a personal AI assistant
# pyaudio installed
# speechrecognition installed
# gTTS installed
# wiki installed

# import libraries

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import calendar
import wikipedia
import warnings
import random
import math
from datetime import datetime

r=sr.Recognizer()
p = 0
with sr.Microphone() as source :
    print('heya mini here ,say the password : ')
    audio=r.listen(source)
    data =r.recognize_google(audio)
    data=data.lower()
    wake_word = 'hey mini'
    print('you said : '+data)
    while p<5:
        if data == wake_word:
            print('wellcome ruddy')
            break
        else:
            p+=1

if p<5:

    choice = int(input('press 1 for voice search or press 2 for text search : '))
    data=''
    if choice == 1 :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('heya mini here ,say something')
            audio = r.listen(source)
            data = r.recognize_google(audio)
    elif choice == 2:
        data = (input('hey mnini here, what you want to do : '))
    else :
        print('invalid choice ,retry')

        def Response(text):
            myobj = gTTS(text, lang='en', slow=False)
            myobj.save('response.mp3')
            os.system('start response.mp3')
            print('you said : ' + data)
        text = data



        if (data == 'good morning' or data == 'good night' or data == 'good afternoon' or data == 'good evening'):
            Response(text + 'rudranil')


        elif data == 'real madrid':
            print('hala madrid forever')


            def Response(text):
                myobj = gTTS(text, lang='en', slow=False)
                myobj.save('response.mp3')
                os.system('start response.mp3')


            text = data
            Response('hala madrid')


        elif data == 'date' or data == 'say the date' or data == 'what is todays date':
            def getdate():
                now = datetime.datetime.now()
                my_date = datetime.datetime.today()
                weekday = calendar.day_name[my_date.weekday()]
                dayNum = now.day
                monthname = now.month
                yearnum = now.year
                month = ['0', 'jan', 'feb', 'mar', 'apl', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']
                day = ['0', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                       '13th', '14th',
                       '15th', '16th', '17th', '18th', '19th', '20th', '21th', '22th', '23th', '24th', '25th',
                       '26th',
                       '27th', '28th', '29th', '30th', '31th']
                return 'todays date : ' + day[dayNum], month[monthname], yearnum


            print(getdate())
            Response(getdate())

        elif data == 'search':

            s=int(input('input 1 for voice search or input 2 for text input'))

            if s==1:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('what you want to search')
                    audio = r.listen(source)
                    i = r.recognize_google(audio)

                    def find(text):

                        print('the search result are here : ')
                        print(wikipedia.summary(i, sentences=2))
                        myobj = gTTS(text, lang='en', slow=False)
                        myobj.save('response.mp3')
                        os.system('start response.mp3')

                    text = i
                    Response(wikipedia.summary(i,sentences=2))
            elif s==2:
                i=(input('what you want to search'))
                print(wikipedia.summary(i,sentences=2))

                def find(text):
                    print('the search result are here : ')
                    print(wikipedia.summary(i, sentences=2))
                    myobj = gTTS(text, lang='en', slow=False)
                    myobj.save('response.mp3')
                    os.system('start response.mp3')
                text = i
                Response(wikipedia.summary(i, sentences=2))

            else :
                print('invalid request ,retry')

        elif data == 'check time' or data == 'what is the time':

            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)


        #this is incomplte

        elif data=='search website' or data=='website' or data=='webpage':
            print('which website to you like to open ')
            website =(input('enter : '))
            print(wikipedia.page(website).url)

        elif data == 'when if your birthday' or data ==  'when were you created ':
            print('i dont have a exact birthday but you can wish me now if you want ')
            b=(input('will you like to wish me today ? '))
            if b== 'yes' :
                print ('thank you :) ')
            else :
                print ('wish me or else i wont talk to your again ')

        elif data == 'who created you ':
            print('I am craeted by "MASTER RUDRANIL SHIL"')

        elif data == 'do you have a religion':
            print('NO!! i dont  have a personal religion but my users religion is my religion ')

        elif data == 'can i change your name ':
            print('absolutely no, you are not allowed to change my name.')
            Response('i love my name,so dont even think of changing it')

        elif data == 'i love you':
            Response('I LOVE YOU TWO and even more')

        elif data== 'do you like me ':
            Response ('yes!! i absolutly like you')


        elif data == 'simple calculation':
            num1= int(input('enter a number'))
            num2=int(input('enter another number'))
            cal=int(input('which funtion do you want to  use : '
                       '1: ADD'
                       '2: substract'
                       '3: multiply'
                       '4: divide'))
            def add (x,y):
                return x+y
            def substract(x,y):
                return x-y
            def multiply(x,y):
                return x*y
            def divide (x,y):
                return x/y
            if cal == '1':
                print(num1+' + '+num2+' = '+add(num1,num2))
            elif cal=='2':
                print(num1 + ' - ' + num2 + ' = ' + substract(num1, num2))
            elif cal=='3':
                print(num1 + ' * ' + num2 + ' = ' + multiply(num1, num2))
            elif cal == '4':
                print(num1 + ' / ' + num2 + ' = ' + divide(num1, num2))
            else :
                print('invalid choice')


        else:
            def Response(text):
                myobj = gTTS(text, lang='en', slow=False)
                myobj.save('response.mp3')
                os.system('start response.mp3')
                print('you said : ' + data)

else:
    print('wrong password,retry')
