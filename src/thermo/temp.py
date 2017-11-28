import json
import argparse



def increment_temp(amount):
	new_temp = get_temp() + amount
	change_temp(new_temp)


def change_temp(temp):
 
	if is_valid_val(int(temp)):
                with open('/data/thermo/temp.json', 'r') as jsonfile:
                        data = json.load(jsonfile)
                data['temp'] = temp
                with open('/data/thermo/temp.json', "w") as jsonFile:
                        json.dump(data, jsonFile)
	else:
                print('failed ---->')



def get_temp():
        with open('/data/thermo/temp.json', 'r') as jsonfile:
                data = json.load(jsonfile)
        return data['temp']



def is_valid_val(temp):
        if temp>=65 or temp<=85:
                return True
        else:
                return False

def main():

        parser =  argparse.ArgumentParser()
        parser.add_argument("temp", help=" Set temp", type=int)
        args = parser.parse_args()
        val  = change_temp(int(args.temp))
        print(val)

if __name__ =="__main__":
        main()

