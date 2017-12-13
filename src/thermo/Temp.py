import json
import argparse
import os


def increment_temp(amount):
    new_temp = get_temp() + amount
    change_temp(new_temp)


def change_temp(temp):
    file_path = os.path.join(os.sep, 'Users','mababio','Desktop','data','thermo','temp.json')
    if is_valid_val(int(temp)):
        with open(file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            data['temp'] = temp
        with open(file_path, "w") as jsonFile:
            json.dump(data, jsonFile)
    else:
                print('failed ---->')


def get_temp():
    file_path = os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'data', 'thermo', 'temp.json')
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return int(data['temp'])


def is_valid_val(temp):
    if 65 <= temp <= 85:
        return True
    else:
        return False


def main():

        parser = argparse.ArgumentParser()
        parser.add_argument("temp", help=" Set temp", type=int)
        # args = parser.parse_args()
        # val  = change_temp(int(args.temp))
        # print(val)


if __name__ == "__main__":
        main()
