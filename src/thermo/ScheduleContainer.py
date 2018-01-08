import schedule
import time
import Temp as t
from multiprocessing import JoinableQueue
from threading import Thread
from threading import Lock
from singleton_decorator import singleton

'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: ScheduleContainer class contains thermostat schedules 
that get appended to a Queue and activated using a continuous loop mechanism

'''


@singleton
class ScheduleContainer(object):

    def __init__(self):
        self.schedule_container = JoinableQueue(maxsize=0)
        self.scheduler = schedule
        self._run = True
        worker = Thread(target=self.work)
        worker.start()

    def append(self, request_form):
        self.schedule_container.put(request_form)

    @staticmethod
    def task(temp):
        def inner():
            t.change_temp(temp)
        return inner

    def work(self):
        lock = Lock()

        while self._run:
            lock.acquire()
            if not self.schedule_container.empty():
                schedule_obj = self.schedule_container.get()
                job = self.scheduler.every()
                job.start_day=str(schedule_obj.day)
                job.unit = 'weeks'
                job.at(str(schedule_obj.time)).do(self.task(schedule_obj.temp))
                print('schedule made into job')
                schedule_obj.save()
                self.schedule_container.task_done()
            lock.release()
            schedule.run_pending()
            time.sleep(1)

