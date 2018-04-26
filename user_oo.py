import pickle
import time
import os
import pickle
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

	def addUser(self, user_id):
		self.user_list[user_id] = User()

	def getUserInfo(self, user_id):
		if not self.user_list[user_id]:
			self.addUser(user_id)
		return self.user_list[user_id].dish_name != ""

	def getUser(self, user_id):
		if user_id not in self.user_list:
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
		ret = response.makeResponseName(name)
		if ret[0] != "我还不会这个菜哦？":
			self.dish_name = name
			self.step_id = 0
		return ret