import speech_recognition as sr     #Installing speech recoganition
import pyttsx3  #Installing text to audio[To access the Microphone]
import pywhatkit    #Package for accessing youtube and many more
import datetime
import wikipedia
import pyjokes

listen_audio = sr.Recognizer()  #creating a variable to hold speech recognition
engine = pyttsx3.init()     #setting pyttsx3 engin

voices = engine.getProperty('voices')    #getting voices of Pyttsx3
engine.setProperty('voice', voices[1].id)   #Setting voice of AI to femail voice

engine.say('I am BEBBOOO your AI')
engine.say('How may I help You')
engine.runAndWait()

# Intitiazing function for talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Initilizing function for taking command from user by
def take_command():
    try:
        with sr.Microphone() as source:  # Acessing MicroPhone
            print("Listning...")
            voice = listen_audio.listen(source)  # Listning the audio
            command = listen_audio.recognize(voice)  # converting audio to text
            command = command.lower()
            if 'bebbooo' in command:
                command = command.replace('bebbooo', '')
            return command
    except:
        return "Microphone Error!!!"

#takinig command and processing
def run_AI():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing'+song)
        print('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk("It's " + time)
    elif 'who is ' in command or 'what is ' in command:
        searchItem = command.replace('who is ' or 'what is', '')
        info = wikipedia.summary(searchItem, 2)
        print(info)
        talk(info)
    elif 'tell me a joke ' in command or 'entertain me ' in command or 'tell me some jokes ' in command:
        joke = pyjokes.get_joke()
        print("Here is some joke for you "+joke)
        talk(joke)
    else:
        print("Sorry,please repeat!")


while True :
    run_AI()