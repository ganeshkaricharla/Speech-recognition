#import the library
import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything")
    audio=r.listen(source) #activate microphone
    try:
        #recognize text uses google
        text=r.recognize_google(audio)
        #output recognized text
        print("You said :{}".format(text)) 
    except:
        print("Sorry !Could not recognize")
