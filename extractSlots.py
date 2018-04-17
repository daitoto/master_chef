# -*- coding: utf-8 -*-
import re

def extractSlots(text, state):
	# state为0表示没有在做菜，state为1表示正在做菜
	
	resulttext = ''
	resulttype = -1

	# 启动技能
	pattern = re.compile('(打开|启动|进入).*芭乐大厨')
	if re.match(pattern, text):
		resulttext = ''
		resulttype = 3

	# 先匹配一下所有的菜名
	pattern = re.compile('(鱼香肉丝|宫保鸡丁|番茄炒鸡蛋|地三鲜|糖醋排骨|可乐鸡翅|红烧肉|水煮肉片|水煮肉|麻婆豆腐)')
	if re.match(pattern, text) and state == 0:
		resulttext = text
		resulttype = 0

	# 下一步 关键词为下一步|接下来|接着|然后|继续
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(下一(个)?步(骤)?|接下来|接着|然后|继续)((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄))|呢)?')
	if re.match(pattern, text) and state == 1:
		resulttext = ''
		resulttype = 1
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('下一(个)?步(骤)?|接下来|接着|然后|继续')
	# if re.search(pattern, text):
	# 	return '', 1 

	# 重复当前步骤
	# 关键词是当前步|这一步|上一步|前一步
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)?(((一)?下)|(一(次|遍)))?((当前)|((这|上|前)一))步(骤)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text) and state == 1:
		resulttext = ''
		resulttype = 2
	# 关键词是重复|再说|回到|重说|重新说
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)(((一)?下)|(一(次|遍)))?(((当前)|((这|上|前)一))步(骤)?)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text) and state == 1:
		resulttext = ''
		resulttype = 2
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('重复|再说|回到|重(新)?说|((当前)|((这|上|前)一))步(骤)?')
	# if re.search(pattern, text):
	# 	return '', 2 

	# 根据原料推荐菜名
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(我有|用|使用)?(?P<raw>.+)?(可以|能够|能)(用来|拿来)?(做|作)(些)?什么(菜)?')
	result = re.match(pattern, text)
	if result:
		raw = result.group("raw")
		resulttext = raw
		resulttype = 5

	# 查询菜品做法 分四种为了能精准分离出菜名
	# 这道菜怎么做
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(这(道|个)?菜)((怎么(做|弄))|(的做法(是(什么|啥)?)?))')	
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0
	# 怎么做
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(((怎么(做|弄))|(的做法(是(什么|啥)?)?)))')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0
	# 查这道菜
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)(?P<food>.+)?(这(道|个)?菜)')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0
	# 查
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)(?P<food>.+)?')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0
	# 根据原料推荐三种菜名后，用户选择一种
	# 这道菜
	pattern = re.compile('(我)?(想要|想|要)做(?P<food>.+)?(这(道|个)?菜)')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0
	# 不说这道菜
	pattern = re.compile('(我)?(想要|想|要)做(?P<food>.+)?')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		resulttext = food
		resulttype = 0

	# 用户退出
	pattern = re.compile('.*退出.*')
	result = re.match(pattern, text)
	if result:
		resulttext = ''
		resulttype = 4

	return resulttext, resulttype

# text1 = "打开芭乐大厨"
# text2 = "下一步"
# text3 = "重复上一步的做法"
# text4 = "查询下宫保鸡丁怎么做"
# print(extractSlots("番茄炒鸡蛋", 1))
