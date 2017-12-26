import sys
sys.path.append('../')
import app
import os


class TestClass:
    app.init()
    client = app.app.test_client()
    client.testing = 'True'

    def test_env_check(self):
        assert os.path.isfile('../data/thermo/temp.json')
        assert os.path.isfile('../data/thermo/sensor.txt')

    def test_routes(self):

        assert TestClass.client.get('/').status_code == 200
        assert TestClass.client.get('/handle').status_code == 200
        assert TestClass.client.get('/schedule').status_code == 200
        assert TestClass.client.get('/schedule_process').status_code == 200

    def test_clean_up(self):
        app.kill_threads()


