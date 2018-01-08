import Furnace
import AirConditioner
import re
from threading import Thread
from threading import Lock
import Temp as Temp
from config import config

'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: HVAC is a model of the real life HVAC. It is responsible for constantly checking if the furnace is needed or
the ac is needed
by comparing the desire temp and the actual temp 

'''


class HVAC(object):

    sensitivity = 2
    ac = AirConditioner.AirConditioner()
    furnace = Furnace.Furnace()

    def __init__(self):
        self._run = True
        worker = Thread(target=self.task)
        worker.start()

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

    def task(self):
        lock = Lock()
        while self._run:
            lock.acquire()
            if (Temp.get_temp() + HVAC.sensitivity) > self.get_sensor_temp():
                HVAC.furnace.on()
                HVAC.ac.off()
            elif (Temp.get_temp() + HVAC.sensitivity) < self.get_sensor_temp():
                HVAC.ac.on()
                HVAC.furnace.off()
            elif (Temp.get_temp() + HVAC.sensitivity) == self.get_sensor_temp():
                HVAC.furnace.off()
                HVAC.ac.off()
            else:
                print('forgot about this corner case')
            lock.release()


if __name__ == "__main__":

    obj = HVAC()






