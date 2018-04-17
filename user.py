import pickle
#{userid:{dish_id, step_id, time_stamp}}
users = dict()

#search user info by id
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

#save user info
def save_user():
	global users
	f_user = open("data/users.pkl", "wb")
	pickle.dump(users, f_user)
	f_user.close()