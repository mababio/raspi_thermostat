'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: The Air Conditioner object is a representation of real world Furnace.

'''

from singleton_decorator import singleton

@singleton
class AirConditioner():
    def __init__(self, air_conditioner_script_path=''):
        self.air_conditioner_script_path = air_conditioner_script_path
        # os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'ac.sh')
        pass

    def on(self):
        print('ac turn on')
        # turn AirConditioner on
        # cmd = self.air_conditioner_script_path + ' 1'
        # print(cmd)
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)

    def off(self):
        print('ac turn off')
        # turn AirConditioner off
        # cmd = self.air_conditioner_script_path + ' 0'
        # Popen(cmd, stdout=subprocess.PIPE, shell=True)


if __name__ == '__main__':
        obj = AirConditioner()
        obj.on()
