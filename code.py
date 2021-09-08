import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.5

while True:
    if cp.touch_A1:
        cp.pixels[6] = (255, 0, 0)
        cp.play_file("1.wav")
        time.sleep(0.25)
        cp.pixels[6] = (0, 0, 0)
    if cp.touch_A2:
        cp.pixels[7] = (0, 255, 0)
        cp.play_file("2.wav")
        time.sleep(0.25)
        cp.pixels[7] = (0, 0, 0)
    if cp.touch_A3:
        cp.pixels[8] = (0, 255, 0)
        cp.play_file("3.wav")
        time.sleep(0.25)
        cp.pixels[8] = (0, 0, 0)
    if cp.touch_A4:
        cp.pixels[0] = (40, 15, 210)
        cp.play_file("4.wav")
        time.sleep(0.25)
        cp.pixels[0] = (0, 0, 0)
    if cp.touch_A5:
        cp.pixels[1] = (0, 0, 255)
        cp.play_file("5.wav")
        time.sleep(0.25)
        cp.pixels[1] = (0, 0, 0)
