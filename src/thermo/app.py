from flask import Flask,render_template, request,jsonify
import json
import os
import Schedule as cron
import temp as Temp
from flask_cors import CORS
app =  Flask(__name__)
CORS(app)
def  init():
	default_temp =  65
	data = '{"temp": ' + str(default_temp)+ '}'
	json_data = json.loads(data)
	if not os.path.exists('/data/thermo'):
    		os.makedirs('/data/thermo')
	with open('/data/thermo/temp.json', 'w+') as outfile:
		json.dump(json_data,outfile)
	


@app.route('/')
def index():
	temp  = Temp.get_temp()
	
	return render_template ('index.html', temp = temp)


@app.route('/handle', methods=['GET','POST'])
def handle():
	if request.args.get('control', 0, type=str) == 'UP':
		print("UP ^^^^^^")
		Temp.increment_temp(1)
	if request.args.get('control', 0, type=str) == 'DOWN':
		print("DOWN ^^^^^^^")
		Temp.increment_temp(-1)
	return jsonify(result=Temp.get_temp()) 

@app.route('/setsch', methods=['GET','POST'])
def setsch():
	time = request.args.get('time', 0, type=str) 
	temp = request.args.get('temp', 0, type=str)
	print(time)
	cron.set_sch(time, "echo fgfg") 
	return " hello"

@app.route('/schedule', methods=['GET','POST'])
def schedule():
	
	return render_template ('schedule.html')


@app.route('/schedule_process', methods=['GET','POST'])
def schedule_process():
	time =  request.form['wake_mon_time']
	temp =  request.form['wake_mon_temp']
	sch_obj =  Schedule()


if __name__ == "__main__":
	init()
	app.run()
