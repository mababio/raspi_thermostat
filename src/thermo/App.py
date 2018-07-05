'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: This is the main method the thermostat flask application. All variables that need to be set are declared here
And also routes are configured here as well
'''


from config import config
import HVAC
from flask import Flask, render_template, request, jsonify
import Temp
from threading import Thread
import sys

app = Flask(__name__)




hvac = HVAC.HVAC()
t = Thread(target=hvac.sensor_checker)
t.start()

def kill_threads():
    hvac._run = False
    schedule_queue._run = False



@app.route('/')
def index():
    temp = Temp.get_temp()
    return render_template('index.html', temp=temp)


@app.route('/handle', methods=['GET', 'POST'])
def handle():
    if request.args.get('control', 0, type=str) == 'UP':
        print("UP ^^^^^^")
        Temp.increment_temp(1,hvac.temp_compare)
    if request.args.get('control', 0, type=str) == 'DOWN':
        print("DOWN ^^^^^^^")
        Temp.increment_temp(-1, hvac.temp_compare)
    return jsonify(result=Temp.get_temp())


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html')


@app.route('/schedule_process', methods=['GET', 'POST'])
def schedule_process():
    dow = request.form.get('dow')
    hour = request.form.get('hour')
    minute = request.form.get('minute')
    temp = request.form.get('temp')

    #print(dow + '   ' + ' ' +hour + '  ' + minute +' '+ temp)
    #sys.exit(1)
    Temp.activate_schedule(temp, hour, minute, dow)
    current_temp = Temp.get_temp()
    return render_template('index.html', temp=current_temp)


if __name__ == "__main__":
    #pass
    app.run(threaded=True, host='0.0.0.0', port=8080)
