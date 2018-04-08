# -*- coding: utf-8 -*-
import time
import pickle
#[dish_name:string, sources:list[string], steps:list[step:[info, time]], key_words:list[string]]
cuisine = []
#{userid:{dish_id, step_id, time_stamp}}
users = dict()

def find_user(user_id):
	global users
	f_user = open("data/users.pkl", "rb")
	users = pickle.load(f_user)
	f_user.close()
	try:
		return users[user_id]
	except:
		users[user_id] = {'dish_id': -1, 'step_id': 0, 'time_stamp': 0}
		return users[user_id]

def save_user():
	global users
	f_user = open("data/users.pkl", "wb")
	pickle.dump(users, f_user)
	f_user.close()

def server_dish(dish_id, step_id):
	global cuisine
	if step_id >= len(cuisine[dish_id][2]):
		return [-2, 0]
	return cuisine[dish_id][2][step_id]

# -1 means no such dish
def find_dish(dish_name):
	global cuisine
	for i in range(len(cuisine)):
		if (cuisine[i][0] == dish_name):
			return i
	return -2

#request_type: 0: new dish, 1: next step, 2: repeat
def ret_voice(dish_name, user_id, request_type):
	global users
	info = find_user(user_id)
	info['time_stamp'] = time.time()
	dish_id = info['dish_id']
	step_id = info['step_id']
	if request_type == 1:
		if dish_id == -1:
			return -1, "请问您要做什么菜？", 0
		step_id += 1
		ret = server_dish(dish_id, step_id)
		info['step_id'] = step_id
	elif request_type == 2:
		if dish_id == -1:
			return -1, "请问您要做什么菜？", 0
		ret = server_dish(dish_id, step_id)
	elif request_type == 0:
		dish_id = find_dish(dish_name)
		if dish_id == -2:
			return -1, "我还不会这个菜哦？", 0
		info['dish_id'] = dish_id
		info['step_id'] = 0
		step_id = 0
		ret = server_dish(dish_id, 0)
	elif request_type == -1:
		return -1, "我不太明白您的意思。", 0
	else:
		return -1, "你好，我是芭乐大厨，您想做什么菜呢？", 0
	users[user_id] = info
	if ret[0] == -2:
		del users[user_id]
	return step_id, ret[0], ret[1]

def find_audio(time):
	url = ""
	time_used = 0
	if time <= 0:
		url = ""
		time_used = 0
	else:
		url = "60.mp3"
		time_used = 60
	return {"type": "audio", "url": url}, time_used

def ret_list(step_id, words, time):
	if step_id == -1:
		return words, [], False
	if words == -2:
		return "您的菜已经做完啦！", [], True
	words = '第%d步，' % (step_id + 1) + words
	ret = []
	while time > 0:
		audio, time_used = find_audio(time)
		time -= time_used
		ret.append(audio)
	#return words, ret, False
	return words, [], False

def extract(dish):
	ret = [dish[0]]
	ret.append(dish[1].split(' '))
	steps = dish[2].split('\n')
	steps = [step.split('$') for step in steps]
	for step in steps:
		if len(step) == 1:
			step.append(0)
		else:
			step[1] = int(step[1])
	ret.append(steps)
	ret.append(dish[3].split(' '))
	return ret

def load_data():
	global cuisine
	f = open('data/cuisine.txt', 'r')
	t = f.read().split('\n##\n')
	cuisine = [dish.split('\n#\n') for dish in t]
	cuisine = list(map(extract, cuisine))

def select(request_type, dish_name, user_id):
	step_id, words, time = ret_voice(dish_name, user_id, request_type)
	save_user()
	return ret_list(step_id, words, time)

def test_dish():
	print(select(0, '宫保鸡丁', True, '01'))
	print(select(0, 'aaa', True, '01'))
	print(select(1, '宫保鸡丁', True, '01'))

if __name__ == '__main__':
	load_data()
	test_dish()