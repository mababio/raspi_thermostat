import AControllable

from singleton_decorator import singleton
from config import  config
'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: The Furnace object is a representation of real world Furnace. 

'''


@singleton
class Furnace(AControllable.AControllable):

    def on(self):
        # turn furnace on
        #print('furnace turn on')
        cmd = config.furnace_path + ' set 4 1'
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)

    def off(self):
       # print('furnace turn off')
        cmd = config.furnace_path + ' set 4 0'
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)
