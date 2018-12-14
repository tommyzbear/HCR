import speech_recognition as sr
import snowboydecoder
import sys
import signal
import time
import multiprocessing
import rospy
import std_msgs 

interrupted = False
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
        audio = r.listen(source,phrase_time_limit=6)
    
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
    if (command.lower() == 'start'):
        print('command recognized')
        output = 'start'
    elif (command.lower() == 'stop'):
        print('command recognized')
        output = 'stop'
    elif (command.lower() == 'follow'):
        print('command recognized')
        output = 'follow'
    elif (command.lower() == 'take picture' or command.lower() == 'take a picture'):
        print('command recognized')
        output = 'take picture'
    elif (command.lower() == 'exit'):
        print('exit program')
        output = 'exit'    
    else:
        output = 'error'
         
    return output
        
##main
while True:    
    hotword_detection('Tracer_Tracer.pmdl')
      
    cmd = voice_command()
    while(cmd == 'error'):
        print ('pls say again')
        cmd = voice_command()
    if(cmd == 'exit'):
        break
    else:
        print('your command is ',cmd)
'''
if __name__ == '__main__':
    rospy.init_node('voice_recognition')
    pub = rospy.Publisher('voice_cmd', Bool, queue_size=1)
    if not rospy.is_shutdown():
        while True:
            start = voice_command()
            pub.publish(start)
 '''   
    
    

    
    