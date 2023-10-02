import pyttsx3
print('This is a Program which pronounce your words')
while True:
 a = input('Enter your Text: ')
 def say(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()
 say(a)
