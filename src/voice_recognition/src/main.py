#! /usr/bin/env python
import speech_recognition as sr
import snowboydecoder
import sys
import signal
import rospy
from std_msgs.msg import String 
import pyglet

import pyttsx


interrupted = False

def speak(arg):
    import pyttsx
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()
    

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted
    
def hotword_detection(hot_word):
    model = hot_word
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Detecting trigger word...Robot is doing other things...')
    
    # main loop
    detector.start(detected_callback=snowboydecoder.play_audio_file,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    
    detector.terminate()

def voice_command():
    print("entering voice command")
    command = None
    output = None
    r = sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source, duration = 0.5 )
        audio = r.listen(source,phrase_time_limit=4)
    
    try:
        print(r.recognize_google(audio))
        command = r.recognize_google(audio)
        '''print(r.recognize_sphinx(audio))
        command = r.recognize_sphinx(audio)'''
    except sr.RequestError:
        print('error1')
        output = 'error'
        return output
    except sr.UnknownValueError:
        print('could not recognized')
        output = 'error'
        return output
    if ('start' in command.lower()):
        print('command recognized')
        output = 'start'
    elif ('stop' in command.lower()):
        print('command recognized')
        output = 'stop'
    elif ('generate' in command.lower()):
        print('command recognized')
        output = 'generate'
    elif ('take picture' in command.lower()):
        print('command recognized')
        output = 'take picture'
    elif ('exit' in command.lower()):
        print('exit program')
        output = 'exit'    
    else:
        output = 'error'
         
    return output


if __name__ == '__main__':
    rospy.init_node('voice_recognition')
    #pub = rospy.Publisher('voice_cmd', twist, queue_size=1)
    pub = rospy.Publisher('/voice_command', String, queue_size=1)
    
    engine = pyttsx.init()
    while not rospy.is_shutdown():
	    hotword_detection('Tracer_Tracer.pmdl')
	    cmd = voice_command()
	    while(cmd == 'error'):
             speak('Please say again!')
             cmd = voice_command()
	    if(cmd == 'start'):
             speak('Start recording!')
             pub.publish(cmd)
	    if(cmd == 'stop'):
             speak('Stop recording!')
             pub.publish(cmd)
	    if(cmd == 'generate'):
             speak('video generated!')
             pub.publish(cmd)
	    if(cmd == 'exit'):
             speak('ByeBye!')
             song = pyglet.media.load('tjintro.wav')
             song.play()
             pyglet.app.run()
             break
  

    

    
    
