import pygame
import socket


######################### user changeable variables #########################

# The value below represents the joystick number as it's seen by your system. 0 is the first joystick, 1 second joystick, etc
# If you have additional joysticks installed these values might change
joystick1 = 1

j1button1 = 30 # TURN CHAIR ON
j1button2 = 18 # PARK CHAIR

TCP_IP = 'ENTER.YOUR.IPADDRES.HERE'

UDP_IP = 'ENTER.YOUR.IPADDRES.HERE'

######################### END OF user changeable variables #########################

# don't modify anything after this line unless you know what you are doing :)



TCP_PORT = 50020
MESSAGE1 = b'\xa1' # turn on
MESSAGE2 = b'\xa2' # turn off
MESSAGE3 = b'\xa2\x01' # turn off and parking
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

UDP_PORT = 50010
LIGHTSOFF = b'\xb2\x01\x01\x00\xff\x00'

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP


chairison = False

pygame.init()

j = pygame.joystick.Joystick(joystick1)
j.init()

def turnofflights():
    sock.sendto(LIGHTSOFF, (UDP_IP, UDP_PORT))

try:
    while True:

        if chairison == False:
            turnofflights()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(j1button1) and chairison == False:
                    chairison = True
                    s.send(MESSAGE1)
                    print("Chair is now on")
                elif j.get_button(j1button2) and chairison == True:
                    chairison = False
                    s.send(MESSAGE3)
                    print("Chair is now off")



except KeyboardInterrupt:
    s.close()
    print("Done")

s.close()
print("Done")