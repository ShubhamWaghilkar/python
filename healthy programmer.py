import pygame
import time
import  datetime
from pygame import mixer

current_time = time.strftime("%H:%M:%S")
work_start_time = '09:00:00'
work_end_time = '24:00:00'

water_limit = 200
glass_size = 5
no_of_glass = round(water_limit/glass_size)
total_work = 60 #8hours
water_interval = (total_work/no_of_glass)
eye_count =0
pys = 0

eye_interval = 60 ##30minutes
phy_interval = 60 ##45minutes

def playsong():
    mixer.init()
    mixer.music.load("wa.mp3")
    print("loaded")
    mixer.music.play()
    mixer.music.set_volume(1.0)
    print("music playing")

#
# user = input("Pleae select yes an no to start the program")
# user = user.lower()
# if user =="yes":
#     while current_time > work_start_time and current_time < work_end_time:
#         if water_count == 28 and water_count == 60:
#             playsong()
#             wat= input("to stop remainder hit 'drank'")
#             wat = wat.lower()
#             if wat == "drank":
#                 mixer.music.stop()
#                 f = open("water.txt","a")
#                 f.write(f"logged {datetime.datetime.now()} drank water")
#                 print("Music stop")
#                 break
#


def wr(file,text):
    f = open(file,"a")
    f.write(f"[ " + str(datetime.datetime.now()) + "] : "+ text)
    f.close()


def water(glass):
    i = ""
    while(i is not 'drank'):
        playsong()
        print("\n", end="")
        i = input("did you drank water type yes if drank").lower()
        if i == "drank":
            wr('water.text','Dranked')
            mixer.music.stop()
            time.sleep(water_interval)
            break
def eye():
    i = ""
    while(i is not "done"):
        playsong()
        print("\n", end="")
        i = input("have taken break from the screen").lower()
        if i == "done":
            wr('eye.txt', 'eyeBreak Taken')
            mixer.music.stop()
            time.sleep(eye_interval)
            break

def phy():
    i = ""
    while(i is not "ex"):
        playsong()
        print("\n ", end="")
        i = input("Have you done the exercise").lower()
        if i == "ex":
            wr('phy.txt','exercise Done')
            mixer.music.stop()
            time.sleep(phy_interval)
            break

try:
    glass = 0
    while(current_time is not work_end_time):
       if current_time>=work_start_time and current_time<= work_end_time:
           if glass == no_of_glass:
               pass
           else:
               water(glass)
               glass +=1
               eye()
               phy()
               current_time = time.strftime("%H:%M:%S")
               print(glass)

except Exception as e:
    print("something wrong")








