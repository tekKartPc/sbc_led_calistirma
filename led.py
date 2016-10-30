import RPi.GPIO as GPIO
import time

hangiPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(hangiPin,GPIO.OUT)

try:

	while True:

		GPIO.output(hangiPin,True)
 		time.sleep(1)
 		GPIO.output(hangiPin,False)
 		time.sleep(9)

except KeyboardInterrupt: 
#cikis yapildi
	GPIO.output(hangiPin,False)
	print("led uygulamasindan cikis yapildi")
finally:
	GPIO.cleanup()
