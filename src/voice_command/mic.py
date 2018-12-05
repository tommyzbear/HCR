import speech_recognition as sr



print("entering voice command")
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))
except sr.RequestError:
    print('error1')
except sr.UnknownValueError:
    print('error2')

