from pygame import mixer
from datetime import datetime
from time import time
def musloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        a==stopper
        mixer.music.stop()
        break

def log(msg):
    with open("alarm.txt","a") as f:
        f.write(f"{msg} at {datetime.now()}\n")
#just put your favourite tune in your project folder and write the name of the audio file
init_water=time()
init_eyes=time()
init_exercise=time()
watersecs=5 #just for demonstration it should be after 30-60 mints(1800-3600 secs)
eyesecs=10#same
exsecs=20#same

while True:
    if time() - init_water > watersecs:
        print("Drink water and enter 'done' to stop the alarm\n")
        musloop("alarm.mp3","done")
        init_water=time()
        log("drank water")

    if time() - init_eyes > eyesecs:
        print("Do your eye exercise and enter 'done' to stop the alarm\n")
        musloop("alarm.mp3", "done")
        init_eyes = time()
        log("eye exercise is done")

    if time() - init_exercise > exsecs:
        print("Do your exercises and enter 'done' to stop the alarm\n")
        musloop("alarm.mp3", "done")
        init_exercise = time()
        log("exercises are done")
