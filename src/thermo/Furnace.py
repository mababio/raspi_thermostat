from subprocess import call

from singleton_decorator import singleton


@singleton
class Furnace(object):
    def __init__(self):
        self.furnace_script_path = ''
        pass

    def on(self):
        # turn furnace on
        call(self.furnace_script_path, '1')
        pass

    def off(self):
        # turn furnace off
        call(self.furnace_script_path, '0')
        pass
