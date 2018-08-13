'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: The Air Conditioner object is a representation of real world Furnace.

'''

from singleton_decorator import singleton
import subprocess
import shlex
from config import config
import redis

@singleton
class AirConditioner():
    def __init__(self, air_conditioner_script_path=''):
        self.air_conditioner_script_path = air_conditioner_script_path
        self.r = redis.Redis(
            host='localhost',
            port=6379
            )
        if not self.r.exists('furnace'):
            self.r.set('ac','off')


    def on(self):
        if self.r.get('ac').decode('utf-8') == 'off':
            print('ac turn on')
            cmd = self.air_conditioner_script_path + ' 1'
            #subprocess.call(shlex.split(cmd))
            self.r.set('ac','on')
        else:
            print('AC already On')

    def off(self):
        if self.r.get('ac').decode('utf-8') == 'on':
            print('ac turn off')
            cmd = self.air_conditioner_script_path + ' 0'
            #subprocess.call(shlex.split(cmd))
            self.r.set('ac','off')
        else:
            print('AC already Off')




if __name__ == '__main__':
        obj = AirConditioner()
        obj.on()
