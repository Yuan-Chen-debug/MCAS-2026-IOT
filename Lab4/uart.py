import serial
import time
import RPi.GPIO as GPIO

LED_PIN = 17    # BCM 編號,依你的接線修改

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    timeout=1
)

def send_data(data):
    if ser.is_open:
        ser.write(data.encode('utf-8'))
        print(f"已傳送: {data.strip()}")

def receive_data():
    if ser.is_open:
        incoming = ser.readline().decode('utf-8').strip()
        if incoming:
            print(f"收到資料: {incoming}")
        return incoming

try:
    n = 0
    while True:
        send_data(str(n % 2) + "\n")
        incoming = receive_data()
        if incoming == "1":
            GPIO.output(LED_PIN, True)
        elif incoming == "0":
            GPIO.output(LED_PIN, False)
        n += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("程式中斷")
finally:
    if ser.is_open:
        ser.close()
        print("串列埠已關閉")
    GPIO.cleanup()