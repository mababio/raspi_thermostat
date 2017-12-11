from subprocess import call

from singleton_decorator import singleton


@singleton
class AirConditioner(object):
    def __init__(self):
        self.air_conditioner_script_path = ''
        pass

    def on(self):
        # turn AirConditioner on
        call(self.air_conditioner_script_path, '1')
        pass

    def off(self):
        # turn AirConditioner off
        call(self.air_conditioner_script_path, '0')
        pass
