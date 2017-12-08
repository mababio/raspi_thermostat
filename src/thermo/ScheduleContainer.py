import Schedule
import schedule
import time
import Temp as t
from multiprocessing import JoinableQueue
from threading import Thread
from threading import Lock
from singleton_decorator import singleton


@singleton
class ScheduleContainer(object):

    def __init__(self):
        self.schedule_container = JoinableQueue(maxsize=0)
        self.scheduler = schedule
        worker = Thread(target=self.work)
        # worker.setDaemon(True)
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

        while True:
            lock.acquire()
            if not self.schedule_container.empty():
                print('schedule in the queue .....')
                schedule_obj = self.schedule_container.get()
                print('type of: ---> ' + str(type(schedule_obj)))
                print('dow---> ' + schedule_obj.day)
                print('time---> ' + schedule_obj.time)
                print('temp---> ' + str(schedule_obj.temp))
                job = self.scheduler.every()
                job.start_day=str(schedule_obj.day)
                job.unit='weeks'
                job.at(str(schedule_obj.time)).do(self.task(schedule_obj.temp))
                print('schedule made into job')
                self.schedule_container.task_done()
            lock.release()
                # time.sleep(5)
            schedule.run_pending()
            print('checking ************************')
            time.sleep(1)


if __name__ == '__main__':
    obj = ScheduleContainer()
    obj.append(Schedule.ThermoSchedule('thursday', '22:34', 8))
    # obj.append(Schedule.Thermo_Schedule('thursday', '12:56', 83))
