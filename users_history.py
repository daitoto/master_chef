from user_oo import Users

users = Users()
for user_id in users.user_list:
	user = users.getUser(user_id)
	print(user_id)
	print(user.history)