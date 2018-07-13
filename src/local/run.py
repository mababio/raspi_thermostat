'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: HVAC is a model of the real life HVAC. It is responsible for constantly checking if the furnace is needed or
the ac is needed
by comparing the desire temp and the actual temp

'''

from hvac_stuff import Furnace, ac
import re
from threading import Thread
from threading import Lock
import Temp as Temp
from config import config
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class HVAC(object):

    sensitivity = 2
    ac = ac.AirConditioner()
    furnace = Furnace.Furnace()

    def sensor_checker(self):
        event_handler = Current_temp_handler(self.push_sensor_temp)
        observer = Observer()
        observer.schedule(event_handler, path="data/thermo/", recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    # push sensor temp to remote redis db    
    def push_sensor_temp(self):
        pass

    def extract_temp(self, file_data):
        p = re.compile('[0-9]{2}')
        temp = p.findall(file_data)[0]
        return temp

    def get_sensor_temp(self):
        try:
            with open(config.sensor_path) as file:
                file_data = file.read()
                sensor_temp = self.extract_temp(file_data)
        except FileExistsError:
            print('file in use!!!!!')
            self.get_sensor_temp()
        return int(sensor_temp)

class Current_temp_handler(FileSystemEventHandler):

    def __init__(self, fun):
        self.fun =  fun

    def on_modified(self, event):
        self.fun()


if __name__ == "__main__":

    obj = HVAC()
