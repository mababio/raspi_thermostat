import json
from config import config
import sys
from crontab import CronTab
import redis

'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: Temp class manipulate the desire temperature
'''


cron = CronTab(user=True)
r = redis.Redis(
    host='localhost',
    port=6379
    )


def activate_schedule(temp, hour, minute, dow):
    job  = cron.new(command='/usr/local/bin/thermo ' + temp, user='root')
    job.dow.on(dow)
    job.hour.on(hour)
    job.minute.on(minute)
    cron.write()

def increment_temp( amount, funt):
    new_temp = get_temp() + amount
    change_temp(new_temp)
    funt()

def change_temp_cli():
    if sys.argv[1]:
        change_temp(int(sys.argv[1]))



def change_temp(temp):
    if is_valid_val(temp):
        r.set('set_temp', temp)



def get_temp():
    if r.exist('set_temp'):
        return int(r.get('set_temp'))
    else:
        r.set('set_temp', 65)


def save(key,value):
    print('saving data ---> ' + key+':'+value)
    r.set(key,value)


def is_valid_val(temp):
    if 65 <= temp <= 87:
        return True
    else:
        return False


if __name__ == "__main__":
    change_temp(100)
    val = get_temp()
    print(val)
