import win32api
import threading
from bhaptics import better_haptic_player as player
import time
from time import sleep
import pygame

######################### user changeable variables #########################

# Below all buttons that are used per joystick keyboard and mouse


# The values below represents the joystick number as it's seen by your system. 0 is the first joystick, 1 second joystick, etc
# If you have additional joysticks installed these values might change
joystick1 = 0
joystick2 = 1 #if you only want to use one joystick set this value the same as the above. You might need to change the throttle axis below as well.

j1button1 = 0 # shooting main gun
j2button1 =  7 # boost button
j2axis1 = 2 # throttle axis

mouse1 = 0x01 # this hexa represents the left mouse button
mouse2 = 0x02 # this hexa represents the right mouse button
key1 = 0x31 # this hexa represents the key 1
key2 = 0x32 # this hexa represents the key 2
key3 = 0x33 # this hexa represents the key 3
key4 = 0x52 # this hexa represents the key r
key5 = 0x46 # this hexa represents the key f
key6 = 0x30 # this hexa represents the key 0
key7 = 0x39 # this hexa represents the key 9

# all key codes available here: https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes


######################### END OF user changeable variables #########################

# don't modify anything after this line unless you know what you are doing :)


pygame.init()

j1 = pygame.joystick.Joystick(joystick1)
j1.init()

j2 = pygame.joystick.Joystick(joystick2)
j2.init()



player.initialize()
keypresstime = 0
interval = 0.005
durationMillis = 100
vibrate = False



state_left = win32api.GetKeyState(mouse1)  #
state_right = win32api.GetKeyState(mouse2)  #
state_1 = win32api.GetKeyState(key1)
state_2 = win32api.GetKeyState(key2)
state_3 = win32api.GetKeyState(key3)
state_r = win32api.GetKeyState(key4)
state_f = win32api.GetKeyState(key5)
state_0 = win32api.GetKeyState(key6)
state_9 = win32api.GetKeyState(key7)


#player.register("Circle", "Circle.tact")
#player.register("CenterX", "CenterX.tact")

durationMillis2 = 100
throttleintensity = 0

print("Started mouse monitor")
shootingmaingun = False

def shooting():
    global durationMillis2
    global shootingmaingun
    if j1.get_button(j1button1):
        player.submit_dot("frontFrame", "VestFront", [{"index": 18, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 18, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 17, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 17, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 14, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 14, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 13, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 13, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 10, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 10, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 9, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 9, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 6, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 6, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 5, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 5, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 2, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 2, "intensity": 100}], durationMillis2)
        sleep(interval)
        player.submit_dot("frontFrame", "VestFront", [{"index": 1, "intensity": 100}], durationMillis2)
        player.submit_dot("backFrame", "VestBack", [{"index": 1, "intensity": 100}], durationMillis2)
        sleep(interval)
    else:
        shootingmaingun = False


def shipon():
    global throttleintensity
    global durationMillis2
    player.submit_dot("frontFrame", "VestFront", [{"index": 19, "intensity": throttleintensity}], durationMillis2)
    player.submit_dot("backFrame", "VestBack", [{"index": 18, "intensity": throttleintensity}], durationMillis2)
    sleep(interval)
    player.submit_dot("frontFrame", "VestFront", [{"index": 16, "intensity": throttleintensity}], durationMillis2)
    player.submit_dot("backFrame", "VestBack", [{"index": 16, "intensity": throttleintensity}], durationMillis2)
    sleep(interval)
    player.submit_dot("frontFrame", "VestFront", [{"index": 15, "intensity": throttleintensity}], durationMillis2)
    player.submit_dot("backFrame", "VestBack", [{"index": 15, "intensity": throttleintensity}], durationMillis2)
    sleep(interval)
    player.submit_dot("frontFrame", "VestFront", [{"index": 12, "intensity": throttleintensity}], durationMillis2)
    player.submit_dot("backFrame", "VestBack", [{"index": 12, "intensity": throttleintensity}], durationMillis2)
    sleep(interval)




def map_range(value, low1, high1, low2, high2):
    newval = low2 + (high2 - low2) * (value - low1) / (high1 - low1)
    return newval


ison = True

while True:



    events = pygame.event.get()

    throttleintensity = int(map_range(j2.get_axis(j2axis1), 1, -1, 0, 50))
    #if throttleintensity == 20:
    #    throttleintensity = 0

    if throttleintensity > 0 and j2.get_button(j2button1):
        throttleintensity = throttleintensity + 20

    if shootingmaingun == True:
        shooting()

    lb = win32api.GetKeyState(mouse1)
    rb = win32api.GetKeyState(mouse2)
    k1 = win32api.GetKeyState(key1)
    k2 = win32api.GetKeyState(key2)
    k3 = win32api.GetKeyState(key3)
    kr = win32api.GetKeyState(key4)
    kf = win32api.GetKeyState(key5)
    k0 = win32api.GetKeyState(key6)
    k9 = win32api.GetKeyState(key7)

    # print(keypresstime)
    if k9 != state_9:
        ison = False

    if k0 != state_0:
        ison = True

    if ison:
        shipon()
        #print(throttleintensity)

        #for event in events:
        #    if event.type == pygame.JOYBUTTONDOWN:
        if j1.get_button(j1button1):
            shootingmaingun = True



        if lb != state_left:  # Button state changed

            if lb < 0 and vibrate:
                player.submit_dot("frontFrame", "VestFront", [{"index": 2, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("frontFrame", "VestFront", [{"index": 3, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("frontFrame", "VestFront", [{"index": 6, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("frontFrame", "VestFront", [{"index": 7, "intensity": 100}], durationMillis)
                sleep(interval)
            #else:
            #    state_left = lb
                #print('Left Button Released')

        if rb != state_right:  # Button state changed

            if rb < 0 and vibrate:
                for i in range(0, 2):
                    player.submit_dot("frontFrame", "VestFront", [{"index": 2, "intensity": 100}], durationMillis)
                    sleep(interval)
                    player.submit_dot("frontFrame", "VestFront", [{"index": 3, "intensity": 40}], durationMillis)
                    sleep(interval)
                state_right = rb
            else:
                state_right = rb


        if k1 != state_1:
            state_1 = k1
            for i in range(0, 2):
                player.submit_dot("frontFrame", "VestFront", [{"index": 16, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 16, "intensity": 100}], durationMillis)
                sleep(interval)

            vibrate = True
            print("Pistol in hand")
            keypresstime = 0


        elif k2 != state_2:
            for i in range(0, 2):
                player.submit_dot("backFrame", "VestBack", [{"index": 2, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 3, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 6, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 7, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 10, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 11, "intensity": 100}], durationMillis)
            vibrate = True
            print("Assault rifle in hand")
            keypresstime = 0
            state_2=k2
        elif k3 != state_3:
            for i in range(0, 2):
                player.submit_dot("backFrame", "VestBack", [{"index": 0, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 1, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 4, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 6, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 8, "intensity": 100}], durationMillis)
                sleep(interval)
                player.submit_dot("backFrame", "VestBack", [{"index": 9, "intensity": 100}], durationMillis)
            vibrate = True
            keypresstime = 0
            state_3 = k3
        elif kr != state_r:
            keypresstime +=1
            #player.submit_dot("frontFrame", "VestFront", [{"index": 17, "intensity": 100}], durationMillis)
            #sleep(interval)
            #player.submit_dot("frontFrame", "VestFront", [{"index": 18, "intensity": 100}], durationMillis)

            if kr < 0:
                if keypresstime > 40 and vibrate:
                    vibrate = False
                    for i in range(0, 2):
                        player.submit_dot("backFrame", "VestBack", [{"index": 16, "intensity": 100}], durationMillis)
                        sleep(interval)
                        player.submit_dot("backFrame", "VestBack", [{"index": 17, "intensity": 100}], durationMillis)
                        sleep(interval)
                    keypresstime = 0
                    print("Vibrate off")
            else:
                keypresstime = 0






    #sleep(0.001)