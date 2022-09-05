import wikipedia                                # For searching and finding the things on google
import webbrowser                               # For opening the youtube, mail and other commands in browser
import datetime                                 # For finding the date and time
import sys                                      # for closing the system command
import pyjokes                                  # For cracking the jokes
import pyttsx3                                  # For converting the text to speech
import speech_recognition as sr                 # For converting the speech to text
import pywhatkit                                # For sending whatsapp message, opening youtube etc
llllllll//
engine = pyttsx3.init('sapi5')                  # pyttsx3.init() is the function which is used to generate the sound and sapi5 consists the voices opf male and female
sound = engine.getProperty('voices')            # this is use to take the property of voices 
engine.setProperty('voice',sound[1].id)         # setproperty is used to set the voice to male and female ie. 0 for male and 1 for female
engine.setProperty('rate',190)                  # This defines the rate ie the speed of the pronounciation

# This function is for wishing user according to the system time
def wishme():
    
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        speak("Good morning, sir")

    elif(hour>=12 and hour<15):
        speak("Good afternoon, sir")

    elif(hour>=15 and hour<20):
        speak("Good evening, sir ")

    else:
        speak("Good night, sir")


# This functaion is created which takes the input manually from the user
def speak(text):
    
    engine.say(text)                             # Here the manual command is taken by the user 
    engine.runAndWait()                          # This function take sthe command and calls the init() function 

    
# This function is created for taking the inputs from the user 
def takecommand():

    r = sr.Recognizer()                         # Recognizer helps to recognize the sound from the user to the system

    # This is used to take the input from the microphone as a source
    with sr.Microphone() as source:

        print("start speaking...")              # It is used to know that the microphone is perfectly working
        r.pause_threshold = 1                   # It is used to generate the output after the given seconds 
        audio = r.listen(source)                # It is used to listen the users voice as a source

    # try and except is used sometimes sound is not properly reached to the microphone so, in that case system should say something like please say again.. or anything.if it heared the voice proerly so, it should perform that task.
    try:

        print("recognizing")                                       # It is used so that after listening user should know the it is working.. 
        statement = r.recognize_google(audio, language='eng-in')   # It stores the sound in a variable as an audio which is in indian eng language
        statement = statement.lower()                              # It converts the input to lowercase because it may give error if system takes the input in uppercase

        if 'alexa' in statement:

            statement = statement.replace('alexa','')              #If there is word "alexa" said by user then it should be replaced 
            print("You said: ", statement)                         # It is used to print the statements which is recognized by the system

        else:

            print("You said: ", statement)                         # It is used to print the statements which is recognized by the system


        # For each and every command given by the user you have to write the code for it
        if 'hello' in statement:

            speak('hello!! sir, I am alexa, do you have any task for me')
            print("hello!! sir, I am alexa, do you have any task for me")

        elif 'who are you' in statement:
    
            speak('I am alexa, a virtual assistant which is made to help people if you want you can know about me more')
            print("I am alexa, a virtual assistant which is made to help people if you want you can know about me more")

        elif 'what can you do' in statement:
    
            speak('I can a lot of work like i can open the maps , files , search on googles, i can crack jokes and much more you wanna try? you can ask me anything i will try to help you out sir..')
            print("I can a lot of work like i can open the maps , files , search on googles, i can crack jokes and much more you wanna try? you can ask me anything i will try to help you out sir..")


        elif 'date and time' in statement:

            today = datetime.date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            date = today.strftime("%B %d, %Y")
            print("Today's date is : ", date , "Current time is : " , time)
            speak('The current date and time is')
            speak(date+time)

        elif 'time and date' in statement:
            
            today = datetime.date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            date = today.strftime("%B %d, %Y")
            print("Today's date is : ", date , "Current time is : " , time)
            speak('The current time and date is')
            speak(time+date)

        elif 'date' in statement:

            today = datetime.date.today()
            date = today.strftime("%B %d, %Y")
            print("Today's date is : ", date)
            speak('The current date is')
            speak(date)

        elif 'time' in statement:

            time = datetime.datetime.now().strftime('%I:%M %p')
            print("Current time is : " , time)
            speak('The current time is')
            speak(time) 

        elif 'tell me a joke' in statement:

            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'location of' in statement:

            speak('locating..')
            location = statement.replace("find location of",'')
            url = 'https://google.nl/maps/place/'+location+'/&amp;'
            webbrowser.get().open(url)
            print("Here is the location of " + location[1])
            speak('Here is the location of' + location[1])

        elif 'on map' in statement:

            speak('locating..')
            location = statement.split(" ")
            print(location[1])
            url = 'https://google.nl/maps/place/'+location[1]+'/&amp;'
            webbrowser.get().open(url)
            print("Here is the location of " + location)
            speak('Here is the location of' + location)


        elif 'where is' in statement:

            speak('locating..')
            location = statement.replace("find location of",'')
            url = 'https://google.nl/maps/place/'+location+'/&amp;'
            webbrowser.get().open(url)
            print("Here is the location of " + location)
            speak('Here is the location of' + location)
        
        elif 'play' in statement:

            song = statement.replace('play', '')
            print("playing..." + song)
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'open google' in statement:
    
            speak('opening google')
            print("opening google")
            webbrowser.open_new("https://www.google.com/")

        elif 'open map' in statement:
            speak('opening map')
            print("opening map")
            webbrowser.open_new("https://maps.google.com/")


        elif 'open mail' in statement:

            print("Opening mail..")
            speak('opening mail')
            webbrowser.open_new('https://mail.google.com/')

        elif 'open youtube' in statement:

            print("Opening Youtube..")
            speak('opening youtube')
            webbrowser.open_new("https://www.youtube.com/")

        elif 'open instagram' in statement:

            print("Opening instagram..")
            speak('opening instagram')
            webbrowser.open_new("https://www.instagram.com/")

        elif 'open wikipedia' in statement:

            print("Opening wikipedia..")
            speak('opening wikipedia')
            webbrowser.open_new('https://www.wikipedia.com/')

        elif 'open stackoverflow' in statement:

            print("Opening stackoverflow..")
            speak('opening stackoverflow')
            webbrowser.open_new('https://www.stackoverflow.com/')

        elif 'open github' in statement:
            
            print("Opening github..")
            speak('opening github')
            webbrowser.open_new('https://www.github.com/')

        elif 'search' in statement:

            statement = statement.replace("search","")
            search = 'https://www.google.com/search?q=' + statement
            speak('searching..')
            webbrowser.open(search)

        elif 'what is' in statement:

            name = statement.replace('what is', '')
            info = wikipedia.summary(name,1)
            print(info)
            speak(info)

        elif 'who is' in statement:

            name = statement.replace('who is', '')
            info = wikipedia.summary(name,1)
            print(info)
            speak(info)
            
        elif 'thankyou' in statement:
            
            print("welcome sir, i am glad that i helped you")
            speak('welcome sir, i am glad that i helped you')
            
        elif 'stop' in statement:

            print("Thank you sir, i am glad that i have helped you, have a nice day sir")
            speak('Thank you sir, i am glad that i have helped you, have a nice day sir')
            sys.exit()

        elif 'shut up' in statement:
    
            print("Thank you sir, i am glad that i have helped you, have a nice day sir")
            speak('Thank you sir, i am glad that i have helped you, have a nice day sir')
            sys.exit()


        engine.runAndWait()                       # It calls the engine.say() function

    # Handling the exception case 
    except Exception as e:

        print("Please say that again..")          # If the computer haven't listened the sound then it should be reflected and it calls the takecommand function again
        speak("Please say that again..")   
        return takecommand()

    return statement


# Main function to start the execution of the program
if _name_ == '_main_':
    
    wishme()                                                    # For wishing the users
    speak("I am Alexa, How may i help you sir ?")               # calling the speak function

    #For asking the input from the user unless user stops the alexa 
    while True:
        takecommand()                                           # calling  takecommand function
