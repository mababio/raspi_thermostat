'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: main method to run  hardware local processes.

'''

from hvac_stuff import Furnace, ac
import asycio


def check furnace_ac():
    ac_local = None
    furnace_local =None
   while True:
    furnace_local = switch_logic(Furnace,Furnace_local,'furnace')
    ac_local = switch_logic(ac,ac_local,'ac')
            
def switch_logic(hvac_obj,local_value, hvac_type):
    remote_value = thermo_util.get_redis(hvac_type)
       if local_value != remote_value :
           if remote_value == 'on':
                hvac_obj.on()
                return 'on'
           else:
               hvac_obj.off()
               return 'off'

        
        
def run():
    loop = asyncio.get_event_loop()
    loop.call_soon(check furnace_ac, loop)
    loop.run_forever()
  

if __name__ == "__main__":
    run()
