import AControllable

from singleton_decorator import singleton

'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: The Furnace object is a representation of real world Furnace. 

'''


@singleton
class Furnace(AControllable.AControllable):
    def __init__(self, furnace_script_path=''):
        self.furnace_script_path = furnace_script_path
        # os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'fur.sh')
        pass

    def on(self):
        # turn furnace on
        #print('furnace turn on')
        cmd = self.furnace_script_path + ' set 4 1'
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)

    def off(self):
       # print('furnace turn off')
        cmd = self.furnace_script_path + ' set 4 0'
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)
