import sys
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/..')
import App
import os


class TestClass:
    App.init()
    client = App.app.test_client()
    client.testing = 'True'

    def test_routes(self):

        assert TestClass.client.get('/').status_code == 200
        assert TestClass.client.get('/handle').status_code == 200
        assert TestClass.client.get('/schedule').status_code == 200
        assert TestClass.client.get('/schedule_process').status_code == 200

    def test_clean_up(self):
        App.kill_threads()
        
    def test_env_check(self):
        assert os.path.isfile('data/thermo/temp.json')
        # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&' + str(oct(os.stat("data/thermo/temp.json")[ST_MODE])))
        # assert os.path.isfile('data/thermo/sensor.txt')


