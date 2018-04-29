#coding=utf-8
import pickle
import time
import os
from flask import Flask
from flask import request
from flask import jsonify
import logging
# from regrex import regrex
from extractSlots import extractSlots
from user_oo import Users
from materia import splitMateria

app = Flask(__name__)
users = Users()

@app.route('/', methods=['POST'])
def chef():
	text = request.get_json()
	utterance = text['request']['utterance']
	logging.info(utterance + ' ' + text['session']['user']['userId'])
	user_info = users.getUserInfo(text['session']['user']['userId'])
	meal_name, res_type = extractSlots(utterance, user_info)
	# print(meal_name, res_type)
	if res_type == 5:
		meal_name = splitMateria(meal_name)
	else:
		meal_name = [meal_name]
	res_string, drects, shouldEndSession = users.select(res_type, meal_name, text['session']['user']['userId'])
	if shouldEndSession:
		users.saveUsers()

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
	app.run(port = 22121)
