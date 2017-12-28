import json
import argparse
import os

'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: Temp class manipulate the desire temperature
'''


class Temp(object):

    def __init__(self, desired_temp_file_path=''):
        self.desired_temp_file_path = desired_temp_file_path

    def increment_temp(self, amount):
        new_temp = self.get_temp() + amount
        self.change_temp(new_temp)

    def change_temp(self, temp):
        if self.is_valid_val(int(temp)):
            with open(self.desired_temp_file_path, 'r') as jsonfile:
                data = json.load(jsonfile)
                data['temp'] = temp
            with open(self.desired_temp_file_path, "w") as jsonFile:
                json.dump(data, jsonFile)
        else:
            print('failed ---->')

    def get_temp(self):
        with open(self.desired_temp_file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
        return int(data['temp'])

    def is_valid_val(self, temp):
        if 65 <= temp <= 85:
            return True
        else:
            return False

