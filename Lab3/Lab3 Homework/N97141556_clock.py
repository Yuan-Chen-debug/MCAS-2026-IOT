import time
import tm1637

CLK, DIO = 23, 24
tm = tm1637.TM1637(clk=CLK, dio=DIO)

try:
    while True:
        t = time.localtime()
        tm.numbers(t.tm_hour, t.tm_min, colon=True)
        time.sleep(0.5)
        tm.numbers(t.tm_hour, t.tm_min, colon=False)
        time.sleep(0.5)
except KeyboardInterrupt:
    tm.write([0, 0, 0, 0])