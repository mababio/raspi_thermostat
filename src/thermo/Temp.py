import json
from config import config


'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: Temp class manipulate the desire temperature
'''


def increment_temp( amount):
    new_temp = get_temp() + amount
    change_temp(new_temp)


def change_temp(temp):
    if is_valid_val(int(temp)):
        with open(config.desired_temp_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            data['temp'] = temp
        with open(config.desired_temp_path, "w") as jsonFile:
            json.dump(data, jsonFile)
    else:
        print('failed ---->')


def get_temp():
    with open(config.desired_temp_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return int(data['temp'])


def is_valid_val(temp):
    if 65 <= temp <= 85:
        return True
    else:
        return False


if __name__ == "__main__":
    val = get_temp()
    print(val)

