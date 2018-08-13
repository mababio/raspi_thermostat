'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me
purpose: Whenever sensor temp changes push to remote redis DB
'''
import sys
sys.path.insert(0, '../lib')
import thermo_util
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def run():
    event_handler = Current_temp_handler(thermo_util.push_sensor_temp)
    observer = Observer()
    observer.schedule(event_handler, path="data/thermo/", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

class Current_temp_handler(FileSystemEventHandler):

    def __init__(self, funt):
        self.job =  funt

    def on_modified(self, event):
        self.job()


if __name__ == "__main__":
    run()
