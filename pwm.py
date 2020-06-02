import RPi.GPIO as GPIO #imports GPIO library
import time #inpirts time library

GPIO.setmode(GPIO.BOARD) #sets the pin referencing mode to that of the board (physical pins)
GPIO.setup(12, GPIO.OUT) #sets up pin 12 (PWM pin) as an output


freq = 1000 #the PWM frequency=1kHz=1000Hz
freq = input("Enter frequency [Hz]:\n")
pwm = GPIO.PWM(12, freq) #enables PWM on pin 12 at a frequency =freq

dc =0 #initial duty cycle 0 or OFF
pwm.start(dc) #begins pwm output at duty cycle =dc


while dc<=100: #runs while dc entered is a appropriate value
	dc_des = input('Enter Desired Duty cycle:\n')
	rise_time = input('Enter Desired Rise Time:\n')
	dc_initial = dc #takes current value of dc
	print("Current DC: ")
	print(dc)

	if dc_des>dc: 	#if rise
		while dc<dc_des:	#while duty cyce smaller than desired
			dc+=((dc_des-dc_initial)/rise_time)*0.1		#increments to get to target value in rise time in steps of 0.1s=100ms
			time.sleep(0.1)					#waits for 100ms to change to next dc
			if dc>dc_des:
				dc=dc_des				#prevents overshoot
			print(dc)
			pwm.ChangeDutyCycle(dc)				#changes to next value
		print("DC RISEN")

	elif dc_des<dc:	#if fall
		while dc>dc_des:	#while duty cycle larger than desired
			dc+=((dc_des-dc_initial)/rise_time)*0.1		#decrements (as dc_des<dc) therefore negative
			time.sleep(0.1)					#sleep time of 0.1 second to wait to change
			if dc<dc_des:
				dc=dc_des	#prevents undershoot
			print(dc)
			pwm.ChangeDutyCycle(dc)
		print("DC LOWERED")

pwm.stop()	#stops pwm output
GPIO.cleanup()	#sets all used pins to inputs to prevent Sh.Ccts

