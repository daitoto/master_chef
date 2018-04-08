# -*- coding: utf-8 -*-
import re

def extractSlots(text):
	# 启动技能
	pattern = re.compile('(打开|启动|进入).*芭乐大厨')
	if re.match(pattern, text):
		return '', 3

	# 下一步 关键词为下一步|接下来|接着|然后|继续
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(下一(个)?步(骤)?|接下来|接着|然后|继续)((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄))|呢)?')
	if re.match(pattern, text):
		return '', 1
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('下一(个)?步(骤)?|接下来|接着|然后|继续')
	# if re.search(pattern, text):
	# 	return '', 1 

	# 重复当前步骤
	# 关键词是当前步|这一步|上一步|前一步
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)?(((一)?下)|(一(次|遍)))?((当前)|((这|上|前)一))步(骤)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text):
		return '', 2
	# 关键词是重复|再说|回到|重说|重新说
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)(((一)?下)|(一(次|遍)))?(((当前)|((这|上|前)一))步(骤)?)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text):
		return '', 2
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('重复|再说|回到|重(新)?说|((当前)|((这|上|前)一))步(骤)?')
	# if re.search(pattern, text):
	# 	return '', 2 

	# 查询菜品做法 分三种为了能精准分离出菜名
	# 这道菜和怎么做都要说 
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(这(道|个)?菜)((怎么(做|弄))|(的做法(是(什么|啥)?)?))')	
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 这道菜或怎么做说一个
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?((这(道|个)?菜)|((怎么(做|弄))|(的做法(是(什么|啥)?)?)))')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 都不说 就需要前面有查询
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)(?P<food>.+)(这(道|个)?菜)?((怎么(做|弄))|(的做法(是(什么|啥)?)?)?)')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# pattern = re.compile('(让芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(这(道|个)?菜)?((怎么(做|弄))|((的)?做法(是(什么|啥)?)?))')
	# result = re.match(pattern, text)
	# if result:
	# 	food = result.group("food")
	# 	return food, 0

	return '', -1

# text1 = "打开芭乐大厨"
# text2 = "下一步"
# text3 = "重复上一步的做法"
# text4 = "查询下宫保鸡丁怎么做"
# print(extractSlots(text4))

