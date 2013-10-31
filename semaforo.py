import piface.pfio as pfio
from time import sleep

green1 = 2
yellow1 = 3
red1 = 4
green2 = 5
yellow2 = 6
red2 = 7

green1Time = 5
yellowTime = 2
red1Time = 4
redGreenTime = 1

loop = True

pfio.init()

while (loop):
	pfio.digital_write(green1,1)
	pfio.digital_write(red2,1)
	sleep(green1Time)
	pfio.digital_write(green1,0)
	pfio.digital_write(yellow1,1)
	sleep(yellowTime)
	pfio.digital_write(yellow1,0)
	pfio.digital_write(red1,1)
	sleep(redGreenTime)
	pfio.digital_write(red2,0)
	pfio.digital_write(green2,1)
	sleep(red1Time)
	pfio.digital_write(green2,0)
	pfio.digital_write(yellow2,1)
	sleep(yellowTime)
	pfio.digital_write(yellow2,0)
	pfio.digital_write(red2,1)
	sleep(redGreenTime)
	pfio.digital_write(red1,0)
	
	if pfio.digital_read(0):
		loop = False
		pfio.digital_write(red2,0)

print("bye!")
