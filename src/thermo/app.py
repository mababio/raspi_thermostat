from flask import Flask, render_template, request, jsonify, redirect
import json
import os
import ScheduleContainer
import Schedule
import Temp as Temp
import HVAC

app = Flask(__name__)

temp_dir = os.path.join('data', 'thermo')
desired_temp_file_path = os.path.join('data', 'thermo','temp.json')
sensor_file_pat = os.path.join('data', 'thermo','sensor.txt')
furnace_script_path = os.path.join('data','script', 'gpio.sh')
air_conditioner_script_path = os.path.join('data','script', 'ac.sh')


schedule_queue = ScheduleContainer.ScheduleContainer()
Temp_instance = Temp.Temp(desired_temp_file_path)
hvac=HVAC.HVAC(sensor_file_pat, furnace_script_path, air_conditioner_script_path, Temp_instance)


def kill_threads():
    hvac._run = False
    schedule_queue._run =  False


def init():\
    set_temp_file()





def set_temp_file():
    default_temp = 65
    data = '{"temp": ' + str(default_temp) + '}'
    json_data = json.loads(data)
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    with open(desired_temp_file_path, 'w+') as outfile:
        json.dump(json_data, outfile)


@app.route('/')
def index():
    temp = Temp_instance.get_temp()
    return render_template('index_b.html', temp=temp)


@app.route('/handle', methods=['GET', 'POST'])
def handle():
    if request.args.get('control', 0, type=str) == 'UP':
        print("UP ^^^^^^")
        Temp_instance.increment_temp(1)
    if request.args.get('control', 0, type=str) == 'DOWN':
        print("DOWN ^^^^^^^")
        Temp_instance.increment_temp(-1)
    return jsonify(result=Temp_instance.get_temp())


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html')


@app.route('/schedule_process', methods=['GET', 'POST'])
def schedule_process():
    dow = request.form.get('dow')
    time = request.form.get('time')
    temp = request.form.get('temp')
    schedule_queue.append(Schedule.ThermoSchedule(dow, time, temp))
    current_temp = Temp_instance.get_temp()
    return render_template('index_b.html', temp=current_temp)


if __name__ == "__main__":
    init()
    app.run(threaded=True,host='0.0.0.0', port=8080)
