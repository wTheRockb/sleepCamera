#!/usr/bin/env python
from picamera import PiCamera
from time import sleep
import datetime
import time

INITIAL_DELAY_HOURS = 1
MAX_HOURS = 10
STILLS_PER_HOUR = 12

def record_still():
    with PiCamera() as camera:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d::%H:%M:%S')
        camera.start_preview()
        time.sleep(2)
        camera.capture('stills/' + current_time + '.jpg')

if __name__ == "__main__":
    i = 0
    sleep(3600 * INITIAL_DELAY_HOURS)
    max_stills = MAX_HOURS * STILLS_PER_HOUR
    while(i < max_stills):
        record_still()
        sleep(3600 / STILLS_PER_HOUR)
        i +=1
