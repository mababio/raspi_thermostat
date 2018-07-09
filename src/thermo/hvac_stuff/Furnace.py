'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: The Furnace object is a representation of real world Furnace.

'''

from singleton_decorator import singleton
from config import  config
import shlex
from config import config
import redis


@singleton
class Furnace():

    def __init__(self):
        self.r = redis.Redis(
            host='localhost',
            port=6379
            )
        if not self.r.exists('furnace'):
            self.r.set('furnace','off')


    def on(self):
        if self.r.get('furnace').decode('utf-8') == 'off':
            print('furnace turn  on')
            cmd = config.furnace_path + ' set 4 1'
            #subprocess.call(shlex.split(cmd))
            self.r.set('furnace','on')
        else:
            print('furnace already On' )

    def off(self):
        if self.r.get('furnace').decode('utf-8') == 'on':
            print('furnace turn off')
            ccmd = config.furnace_path + ' set 4 0'
            #subprocess.call(shlex.split(cmd))
            self.r.set('furnace','off')
        else:
            print('furnace already Off')
