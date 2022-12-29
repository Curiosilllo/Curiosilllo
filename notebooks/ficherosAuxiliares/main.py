import machine
import time

pin = machine.Pin(5, machine.Pin.OUT)

pin.on()

def toggle(p):
    p.value(not p.value())

for i in range(100):
    toggle(p)
    time.sleep_ms(500)
