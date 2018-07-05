import json
from config import config
import redis


'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: Temp class manipulate the desire temperature
'''

r = redis.Redis(
    host='localhost',
    port=6379
    )

def increment_temp( amount, funt):
    new_temp = get_temp() + amount
    change_temp(new_temp)
    funt()


def change_temp(temp):
    if is_valid_val(temp):
        r.set('set_temp', temp)



def get_temp():
    return int(r.get('set_temp'))


def is_valid_val(temp):
    if 65 <= temp <= 87:
        return True
    else:
        return False


if __name__ == "__main__":
    change_temp(100)
    val = get_temp()
    print(val)
