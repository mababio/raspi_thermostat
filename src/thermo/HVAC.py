from singleton_decorator import singleton
import Furnace
import AirConditioner
import re
import Temp as Desire
from threading import Thread
from threading import Lock


@singleton
class HVAC(object):

    # file_path file_path = os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'data', 'thermo', 'temp.json')

    sensitivity = 2
    ac = AirConditioner()
    furnace = Furnace()

    def __init__(self,sensor_file_path):
        self.sensor_file_path = sensor_file_path
        worker = Thread(target=self.work)
        worker.start()

    @classmethod
    def extract_temp(cls,file_data):
        p = re.compile('[0-9]{2}')
        temp = p.findall(file_data)[0]
        return temp

    @classmethod
    def get_sensor_temp(cls,file_path):
        # return sensor_temp
        with open(file_path) as file:
            file_data = file.read()
            sensor_temp = cls.extract_temp(file_data)
        return sensor_temp

    @staticmethod
    def task(cls):
        lock = Lock()
        while True:
            lock.acquire()
            if (Desire.get_temp() + HVAC.sensitivity) > cls.get_sensor_temp():
                HVAC.furnace.on()
                HVAC.ac.off()
            elif (Desire.get_temp() + HVAC.sensitivity) < cls.get_sensor_temp():
                HVAC.ac.on
                HVAC.furnace.off()
            elif (Desire.get_temp() + HVAC.sensitivity) == cls.get_sensor_temp():
                HVAC.furnace.off()
                HVAC.ac.off()
            else:
                print('forgot about this corner case')
            lock.release()



