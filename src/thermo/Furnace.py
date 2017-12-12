from subprocess import Popen
import subprocess

from singleton_decorator import singleton
import os


@singleton
class Furnace(object):
    def __init__(self):
        self.furnace_script_path = os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'fur.sh')
        pass

    def on(self):
        # turn furnace on
        cmd = self.furnace_script_path + ' 1'
        Popen(cmd, stdout=subprocess.PIPE, shell=True)

    def off(self):
        # turn furnace off
        cmd = self.furnace_script_path + ' 0'
        Popen(cmd, stdout=subprocess.PIPE, shell=True)
