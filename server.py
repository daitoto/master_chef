#coding=utf-8
from flask import Flask
from flask import request
from flask import jsonify
# from regrex import regrex
from menu import select
from menu import load_data

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chef():
	text = request.get_json()
	utterance = text['request']['utterance']
	meal_name, res_type = regrex(utterance)
	# meal_name, res_type = "宫保鸡丁", 1
	print(res_type, meal_name, text['session']['user']['userId'])
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
	load_data()
	app.run(host = "localhost", port = 22120)
