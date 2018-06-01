# -*- coding: utf-8 -*-
import time
import pickle
import random
import numpy as np

class Meal(object):
	def __init__(self, mealName, material, style, mealSteps):
		self.mealName = mealName
		self.material = material
		self.style = style
		self.mealSteps = mealSteps

	def queryByName(self, name):
		return name == self.mealName

	def queryByMaterial(self, material):
		score = 0
		for m in material:
			if m in self.material:
				score += 1
		return score ** 2 / len(self.material)

	def queryStep(self, step_id, hint_words):
		if step_id < len(self.mealSteps):
			if step_id < len(self.mealSteps) - 1:
				return self.mealSteps[step_id][0] + hint_words, self.mealSteps[step_id][1]
			else:
				return self.mealSteps[step_id][0], self.mealSteps[step_id][1]
		else:
			return "您的菜已经做完啦！", 0

	def queryAll(self):
		ret = ""
		for i in range(len(self.mealSteps)):
			ret += self.mealSteps[i][0] + "。"
		return ret


class Ad(object):
	def __init__(self, adVoice, adTime, adType=1):
		self.adVoice = adVoice
		self.adTime = int(adTime)
		self.adType = int(adType)

	def queryByTime(self, time):
		return self.adTime <= time


class Response(object):
	def __init__(self, meals = [], keywords = dict(), ads = []):
		self.meals = meals
		self.keywords = keywords
		self.ads = ads
		self.hint_words = "，做完后您可以说下一步。"
		self._load_data()

	def _load_data(self):
		f = open('data/cuisine.txt', 'r')
		t = f.read().split('\n##\n')
		cuisine = [dish.split('\n#\n') for dish in t]
		for dish in cuisine:
			mealName = dish[0]
			material = dish[1].split(' ')
			style = dish[2]
			steps = dish[3].split('\n')
			steps = [step.split('$') for step in steps]
			for step in steps:
				if len(step) == 1:
					step.append(0)
				else:
					step[1] = int(step[1])
			self.meals.append(Meal(mealName, material, style, steps))
		f.close()

		f = open('data/keyword.txt', 'r')
		t = f.read().split('\n##\n')
		l = [m.split('#') for m in t]
		for m in l:
			self.keywords[m[0]] = [m[1], m[2]]
		f.close()

		f = open('data/ad.txt', 'r')
		t = f.read().split('\n##\n')
		l = [m.split(' ') for m in t]
		for m in l:
			self.ads.append(Ad(m[0], m[1], m[2]))
		#self.ads = sorted(self.ads, key=lambda d:d.adTime, reverse=True)
		random.shuffle(self.ads)
		f.close()

	def _replace_keywords(self, words):
		words = words.split('%')
		ret = ""
		for w in words:
			if w in self.keywords:
				if random.random() <= 1:
					ret += self.keywords[w][1]
				else:
					ret += self.keywords[w][0]
			else:
				ret += w
		return ret

	def _find_ads(self, tim):
		ret = []
		time_left = tim
		voice_ad = False
		flag = 1
		random.shuffle(self.ads)
		while time_left and not voice_ad:
			for ad in self.ads:
				if ad.queryByTime(time_left) and ad.adType == 0:
					voice_ad = True
					ret.append({"type": "audio", "url": ad.adVoice})
					time_left -= ad.adTime
					break

		while time_left and flag:
			flag = 0
			for ad in self.ads:
				if ad.queryByTime(time_left) and ad.adType == 1:
					flag = 1
					ret.append({"type": "audio", "url": ad.adVoice})
					time_left -= ad.adTime
			random.shuffle(self.ads)

		return ret

	def makeResponseStep(self, name, step_id):
		if name == "":
			return "请问您要做什么菜？", [], False
		for m in self.meals:
			if m.queryByName(name):
				words, tim = m.queryStep(step_id, self.hint_words)
				if words == "您的菜已经做完啦！":
					return words, [], True
				words = '第%d步，' % (step_id + 1) + words
				return self._replace_keywords(words), self._find_ads(tim), False

	def makeResponseAll(self, name):
		if name == "":
			return "请问您要做什么菜？", [], False
		for m in self.meals:
			if m.queryByName(name):
				words = m.queryAll()
				return self._replace_keywords(words), [], False

	def makeResponseMaterial(self, material):
		scores = []
		for m in self.meals:
			scores.append([m.mealName, m.queryByMaterial(material)])
		scores = sorted(scores, key=lambda d: d[1], reverse=True)
		ret = "为您推荐菜品"
		for i in range(3):
			if scores[i][1] == 0:
				break
			ret += "," + scores[i][0]
		if ret == "为您推荐菜品":
			return "暂时没找到您想要的菜", [], False
		else:
			return ret, [], False

	def makeResponseName(self, name):
		for m in self.meals:
			if m.queryByName(name):
				words, tim = m.queryStep(0, self.hint_words)
				words = "第1步，" + words + "还可以说'所有步骤'来一次性听完所有步骤。"
				return self._replace_keywords(words), self._find_ads(tim), False
		return "我还不会这个菜哦？", [], False