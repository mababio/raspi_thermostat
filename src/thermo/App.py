from config import config
import HVAC
import Schedule
from flask import Flask, render_template, request, jsonify
import ScheduleContainer
import Temp
'''
author: Michael
email: michaelkwasi@gmail.com
website: ababio.me

purpose: This is the main method the thermostat flask application. All variables that need to be set are declared here
And also routes are configured here as well
'''

app = Flask(__name__)

schedule_queue = ScheduleContainer.ScheduleContainer()

hvac = HVAC.HVAC()


def kill_threads():
    hvac._run = False
    schedule_queue._run = False


def init():
    config.set_temp_file()


@app.route('/')
def index():
    temp = Temp.get_temp()
    return render_template('index_b.html', temp=temp)


@app.route('/handle', methods=['GET', 'POST'])
def handle():
    if request.args.get('control', 0, type=str) == 'UP':
        print("UP ^^^^^^")
        Temp.increment_temp(1)
    if request.args.get('control', 0, type=str) == 'DOWN':
        print("DOWN ^^^^^^^")
        Temp.increment_temp(-1)
    return jsonify(result=Temp.get_temp())


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html')


@app.route('/schedule_process', methods=['GET', 'POST'])
def schedule_process():
    dow = request.form.get('dow')
    time = request.form.get('time')
    temp = request.form.get('temp')
    schedule_queue.append(Schedule.ThermoSchedule(dow, time, temp))
    current_temp = Temp.get_temp()
    return render_template('index_b.html', temp=current_temp)


if __name__ == "__main__":
    init()
    app.run(threaded=True, host='0.0.0.0', port=8080)


