import os
import time
import schedule
import Temp as t
import Schedule

def task(temp):
	def inner():
		t.change_temp(temp)
	return inner


#schedule.every().wednesday.at("11:08").do(job(65))

def convert():
	ui_data = Schedule.Schedule('wednesday','11:33',78)

	job  = schedule.every()
	job.start_day=str(ui_data.day)
	job.unit='weeks'
	job.at(str(ui_data.time)).do(task(ui_data.temp))
#schedule.run_all()

	while True:
		schedule.run_pending()
		time.sleep(1)