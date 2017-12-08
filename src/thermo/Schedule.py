import yaml


class ThermoSchedule(object):

    def __init__(self, day, time, temp):
        self.day = day  # expecting monday, tuesday ...
        self.time = time  # expecting hh:mm format
        self.temp = temp
        self.data = self.create_schedule_datagram()

    def create_schedule_datagram(self):
        data = {self.day: {'time': self.time, 'temp': self.temp}}
        return data

    def save(self):
        with open('/Users/mababio/Desktop/data.yml', 'a') as outfile:
            yaml.dump(self.data, outfile, default_flow_style=False)
            print('hello')


if __name__ == '__main__':
    print('main')
