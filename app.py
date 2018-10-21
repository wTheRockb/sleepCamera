from picamera import PiCamera
from time import sleep
import datetime
import time


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
    max_stills = MAX_HOURS * STILLS_PER_HOUR
    while(i < max_stills):
        record_still()
        sleep(3600 / STILLS_PER_HOUR)
        i +=1