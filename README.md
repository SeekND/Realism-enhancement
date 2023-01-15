# Realism-enhancement
Contains python code to allow YAWVR motion chair and bHaptics haptic vest to work with your keyboard/mouse/joystick

Such devices like bHaptics and YawVR are made for VR almost exclusively, but with a bit of tweaking and lots of code you can easily alter them to enhance flatscreen gaming experience to something amazing!
The code provided was designed to be use in Star Citizen but can work for any game as it simple uses keyboard/mouse/joystick inputs.
I've commented the code so hopefully you can change it to your liking.

## See explanation video here:
https://youtu.be/j6GlcPmM9nI



## bHaptics

Keyboard inputs:
- Key 1: Buzzes the vest on bottom left
- Key 2: Buzzes the vest on back left
- Key 3: Buzzes the vest on back right
- Key r (press and hold): Disables buzzing until the pressing another key above
- Key 0: Disables all system (no buzzing)
- Key 9: Enables all system

Joystick inputs:
- Joy 1 shooting button: Buzzes the vest heavily in the center
- Joy 2 throttle: Buzzes the vest in the sides depending on throttle
- Joy 2 boost button: Adds 20% buzz to throttle

Mouse inputs:
- Left mouse: Buzzes front top right heavily
- Right mouse: Buzzes front top right slightly


## YAW VR

- Joy 2 button 2: Turns on chair, enables color
- Joy 2 button 3: Stops chair, disables color 

All movement is handled by YAWVR main app under DirectInput profile.
![Alt text](direcinput.png?raw=true "1")
![Alt text](direcinput2.png?raw=true "2")


## Python libraries required:
- win32api
- websocket-client
- pygame
- socket
- Requires bHaptics vest installed and running for bhaptics to work


## Special thanks:
@RelativelyQuantum in bHaptics discord
@Dániel in YAWVR discord


** Like my work and want to give me a little support? **
http://paypal.me/SeekND
