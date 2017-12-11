from flask import Flask, render_template, request, jsonify, redirect
import json
import os
import ScheduleContainer
import Schedule
import Temp as Temp

app = Flask(__name__)

temp_dir = os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'data', 'thermo')  # os.path.join(os.sep,'data','thermo')
temp_file = os.path.join(os.sep, 'Users', 'mababio', 'Desktop', 'data', 'thermo','temp.json')  # os.path.join(os.sep,'data','thermo','temp.json')
schedule_queue = ScheduleContainer.ScheduleContainer()


def init():
    set_temp_file()


def set_temp_file():
    default_temp = 65
    data = '{"temp": ' + str(default_temp) + '}'
    json_data = json.loads(data)
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    with open(temp_file, 'w+') as outfile:
        json.dump(json_data, outfile)


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
    app.run(threaded=True)
