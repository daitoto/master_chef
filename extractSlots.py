# -*- coding: utf-8 -*-
import re

def extractSlots(text):
	#启动技能
	pattern = re.compile('(打开|启动|进入).*芭乐大厨')
	if re.match(pattern, text):
		return '', 3

	#下一步
	pattern = re.compile('(让芭乐大厨)?(查(询)?((一)?下)?)?(下一(个)?步(骤)?|接下来|接着)((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text):
		return '', 1

	#重复当前步骤
	pattern = re.compile('(让芭乐大厨)?(重复|再说|回到)?(((一)?下)|(一(次|遍)))?(((当前)|((这|上|前)一))步((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?)?')
	if re.match(pattern, text):
		return '', 2

	#查询菜品做法
	pattern = re.compile('(让芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)(这(道|个)?菜)?((怎么(做|弄))|((的)?做法(是(什么|啥)?)?))')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0

	return "", -1

# text1 = "打开芭乐大厨"
# text2 = "下一步"
# text3 = "重复上一步的做法"
# text4 = "查询下宫保鸡丁怎么做"
# print(extractSlots(text4))

