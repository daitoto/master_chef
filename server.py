#coding=utf-8
from flask import Flask
from flask import request
from flask import jsonify
import logging
# from regrex import regrex
from extractSlots import extractSlots
from menu import select
from menu import load_data

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chef():
	text = request.get_json()
	utterance = text['request']['utterance']
	# print(utterance)
	logging.info(utterance + ' ' + text['session']['user']['userId'])
	meal_name, res_type = extractSlots(utterance)
	# print(meal_name, res_type)
	# meal_name, res_type = "宫保鸡丁", 1
	# print(res_type, meal_name, text['session']['user']['userId'])
	res_string, drects, shouldEndSession = select(res_type, meal_name, text['session']['user']['userId'])
	return jsonify(version = text['version'],
					requestId = text['request']['requestId'],
					response = {"outputSpeech": res_string,
								"reprompt": {
									"outputSpeech": "对不起，我不太明白你的意思"
								},
								"directives": drects,
								"shouldEndSession": shouldEndSession})

if __name__ == '__main__':
	print("start")
	logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%d %b %Y %H:%M:%S',
                filename='chef.log',
                filemode='a')
	load_data()
	app.run(port = 22121)
