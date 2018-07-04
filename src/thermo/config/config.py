import configparser
import os
import json

config_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(config_path + '/config.ini')
data_path = config_path + '/..'


temp_dir = os.path.join(data_path, config['FILE_LOCATION']['temp_dir'].strip("'"))
sensor_path = os.path.join(data_path, config['FILE_LOCATION']['sensor'].strip("'"))
furnace_path = os.path.join(data_path, config['FILE_LOCATION']['furnace_script'].strip("'"))
air_conditioner_path = os.path.join(data_path, config['FILE_LOCATION']['air_conditioner'].strip("'"))


if __name__ == "__main__":


    print(data_path+'config.ini')

    print(temp_dir)
