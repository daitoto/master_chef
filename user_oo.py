import pickle
import time
import os
from menu_oo import *

response = Response()

class Users(object):
	def __init__(self, path = "data/users.pkl"):
		if os.path.exists(path):
			f = open(path, "rb")
			try:
				self.user_list = pickle.load(f)
			except:
				self.user_list = dict()
			f.close()
		else:
			self.user_list = dict()

	def select(self, request_type, names, user_id):
		user = self.getUser(user_id)
		print(request_type, names)
		if request_type == -1:
			return "我不太明白您的意思。", [], False
		elif request_type == 0:
			return user.user_queryName(names[0])
		elif request_type == 1:
			return user.user_Next()
		elif request_type == 2:
			return user.user_Again()
		elif request_type == 3:
			if user.dish_name == "":
				return "你好，我是芭乐大厨，您想做什么菜呢？", [], False
			else:
				return "您上次在做，%s，请问要继续下一步吗？" % (user.dish_name), [], False
		elif request_type == 4:
			return "好的，再见", [], True
		elif request_type == 5:
			return user.user_queryMaterial(names)
		elif request_type == 6:
			return 
		else:
			pass

	def addUser(self, user_id):
		self.user_list[user_id] = User()

	def getUserInfo(self, user_id):
		try:
			return self.user_list[user_id].dish_name != ""
		except:
			self.addUser(user_id)		
			return self.user_list[user_id].dish_name != ""	

	def getUser(self, user_id):
		try:
			user = self.user_list[user_id]
			user.hint = 0
			return user
		except:
			self.addUser(user_id)
			return self.user_list[user_id]

	def saveUsers(self, path = "data/users.pkl"):
		f = open(path, "wb")
		pickle.dump(self.user_list, f)
		f.close()

	def __del__(self):
		self.saveUsers()

class User(object):
	def __init__(self, dish_name = "", step_id = 0, history = []):
		self.dish_name = dish_name
		self.step_id = step_id
		self.history = history
		self.hint = 0

	def addHistory(self, string, time):
		self.history.append([string, time])

	def user_Next(self):
		if self.dish_name != "":
			self.step_id += 1
		ret = response.makeResponseStep(self.dish_name, self.step_id)
		if ret[0] == "您的菜已经做完啦！":
			self.addHistory(self.dish_name, time.time())
			self.dish_name = ""
			self.step_id = 0
		return ret

	def user_Again(self):
		ret = response.makeResponseStep(self.dish_name, self.step_id)
		if ret[0] == "您的菜已经做完啦！":
			self.addHistory(self.dish_name, time.time())
			self.dish_name = ""
			self.step_id = 0
		return ret

	def user_queryMaterial(self, material):
		return response.makeResponseMaterial(material)

	def user_queryName(self, name):
		print(name)
		ret = response.makeResponseName(name)
		if ret[0] != "我还不会这个菜哦？":
			self.dish_name = name
			self.step_id = 0
		return ret