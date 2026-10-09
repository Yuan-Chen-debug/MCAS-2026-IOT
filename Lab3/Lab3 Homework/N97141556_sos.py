import RPi.GPIO as GPIO
import time

LED_PIN = 11
BUZ_PIN = 7
SHORT, LONG, GAP, LETTER_GAP = 0.2, 0.6, 0.2, 0.6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZ_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZ_PIN, 1000)

def beep(duration):
    GPIO.output(LED_PIN, True)
    pwm.start(50)
    time.sleep(duration)
    GPIO.output(LED_PIN, False)
    pwm.stop()
    time.sleep(GAP)

try:
    for d in (SHORT, SHORT, SHORT):   # S
        beep(d)
    time.sleep(LETTER_GAP)
    for d in (LONG, LONG, LONG):      # O
        beep(d)
    time.sleep(LETTER_GAP)
    for d in (SHORT, SHORT, SHORT):   # S
        beep(d)
finally:
    pwm.stop()
    GPIO.cleanup()