from crontab import CronTab


class Schedule(object):
	
			def __init__(self,day,sch_type,time,temp): 	
				self.cron_obj = CronTab(user=True)
				self.day = day
				self.sch_type =  sch_type
				self.time = time
				self.temp = temp
				self.command = "/usr/local/bin/thermo " + str(self.temp)
				self.comment = self.sch_type +'_'+ self.day +'_time'

			def day_to_num(self,day):
				if day == 'mon':
					return 1
				elif day == 'tues':
					return 2
				elif day == 'wed':
					return 3
				elif day == 'thurs':
					return 4
				elif day == 'fri':
					return 5
				elif day == 'sat':
					return 6
				elif day == 'sun':
					return 0



			def to_cron_time(self, day,human_time):
				hour = human_time.split(":")[0]
				minute =  human_time.split(":")[1]
				day_num = self.day_to_num(day)
				return minute+' '+hour+' * * '+ str(day_num)
		
			

			def set_schedule(self):
				cron_time = self.to_cron_time(self.day,self.time)
				job =  self.cron_obj.new(command=self.command, comment = self.comment)
				job.setall(cron_time)
				self.cron_obj.write()	
			
			def get_schedule(self):
				iterp = self.cron_obj.find_comment("day_sun_time")
				print(list(iterp))

if __name__ == '__main__':
	obj  = Schedule('sun','day',"21:11",13)
	obj.set_schedule()
	obj.get_schedule()
