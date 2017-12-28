from singleton_decorator import singleton
import Furnace
import AirConditioner
import re
# import Temp as Desire
from threading import Thread
from threading import Lock
import os


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

    def __init__(self, sensor_file_path, furnace_script_path, air_conditioner_script_path,temp_obj):
        self._run = True
        self.sensor_file_path = sensor_file_path
        HVAC.furnace.furnace_script_path = furnace_script_path
        HVAC.ac.air_conditioner_script_path= air_conditioner_script_path
        self.Desire = temp_obj
        worker = Thread(target=self.task)
        worker.start()

    def extract_temp(self, file_data):
        p = re.compile('[0-9]{2}')
        temp = p.findall(file_data)[0]
        return temp

    def get_sensor_temp(self, file_path):
        try:
            with open(file_path) as file:
                file_data = file.read()
                sensor_temp = self.extract_temp(file_data)
        except FileExistsError:
            print('file in use!!!!!')
            self.get_sensor_temp(self.sensor_file_path)
        return int(sensor_temp)

    def task(self):
        lock = Lock()
        while self._run:
            lock.acquire()
            if (self.Desire.get_temp() + HVAC.sensitivity) > self.get_sensor_temp(self.sensor_file_path):
                HVAC.furnace.on()
                HVAC.ac.off()
            elif (self.Desire.get_temp() + HVAC.sensitivity) < self.get_sensor_temp(self.sensor_file_path):
                HVAC.ac.on()
                HVAC.furnace.off()
            elif (self.Desire.get_temp() + HVAC.sensitivity) == self.get_sensor_temp(self.sensor_file_path):
                HVAC.furnace.off()
                HVAC.ac.off()
            else:
                print('forgot about this corner case')
            lock.release()





