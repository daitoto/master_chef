# -*- coding: utf-8 -*-
import re

def extractSlots(text, state):
	# state为0表示没有在做菜，state为1表示正在做菜

	# 启动技能
	pattern = re.compile('(打开|启动|进入).*芭乐大厨')
	if re.match(pattern, text):
		return '', 3

	# 先匹配一下所有的菜名
	pattern = re.compile('(水煮肉片|水煮鱼|麻婆豆腐|鱼香肉丝|蚂蚁上树|辣子鸡|回锅肉|酸汤肥牛|糯米蒸排骨|肉末茄子|粉蒸排骨|干煸肥肠|青椒肉丝|鱼香茄子|'
		 				+'剁椒鱼头|小炒肉|湘西土匪鸭|干锅花菜|啤酒鸭|麻辣小龙虾|菠萝咕咾肉|蜜汁叉烧肉|腊肠煲仔饭|盐焗鸡|梅菜扣肉|糖醋排骨|宫保鸡丁|番茄炒鸡蛋|红烧肉|糯米丸子|'
		 				+'地三鲜|东北乱炖|溜肉段|锅包肉|小鸡炖蘑菇|猪肉炖粉条|四喜丸子|黄焖鸡|糖醋鲤鱼|九转大肠|木须肉|溜肝尖|可乐鸡翅|酱肘子|油焖大虾|'
		 				+'东坡肉|西湖醋鱼|龙井虾仁|桂花糯米藕|干炸响铃|油焖笋|溜肥肠|红烧狮子头|盐水鸭|腌笃鲜|松鼠桂鱼|小米蒸排骨|'
		 				+'客家酿豆腐|佛跳墙|海蛎煎|沙茶面|大盘鸡|手抓羊肉|手抓饭|孜然羊肉|馕包肉|台湾卤肉饭|台式三杯鸡|避风塘炒蟹|三杯虾|苍蝇头|'
		 				+'过桥米线|汽锅鸡|菠萝饭|黑三剁|京酱肉丝|宫保虾球|炸酱面|褡裢火烧|葱爆羊肉|拔丝鸡盒|醋溜木须|八宝饭|醋溜白菜|炸八块|红焖羊肉|胡辣汤|'
		 				+'带把肘子|油泼裤带面|烩肉三鲜|煨鱿鱼丝|清蒸武昌鱼|排骨藕汤|皮条鳝鱼|糍粑鱼|酸辣藕带|热干面|南昌炒米粉|粉蒸肉|藜蒿炒腊肉|莲花血鸭'
		 				+')$')
	if re.match(pattern, text) and state == 0:
		return text, 0

	# 听所有步骤
	pattern = re.compile('(所有|全部)步骤')
	if re.search(pattern, text) and state == 1:
		return '', 6

	# 下一步 关键词为下一步|接下来|接着|然后|继续
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(下一(个)?步(骤)?|接下来|接着|然后|继续)((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄))|呢)?')
	if re.match(pattern, text) and state == 1:
		return '', 1
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('下一(个)?步(骤)?|接下来|接着|然后|继续')
	# if re.search(pattern, text):
	# 	return '', 1 

	# 重复当前步骤
	# 关键词是当前步|这一步|上一步|前一步
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)?(((一)?下)|(一(次|遍)))?((当前)|((这|上|前)一))步(骤)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text) and state == 1:
		return '', 2
	# 关键词是重复|再说|回到|重说|重新说
	pattern = re.compile('((让)?芭乐大厨)?(重复|再说|回到|重(新)?说)(((一)?下)|(一(次|遍)))?(((当前)|((这|上|前)一))步(骤)?)?((((的)?做法)?(是|干)(什么|啥|嘛))|(怎么(做|弄)))?')
	if re.match(pattern, text) and state == 1:
		return '', 2
	# 因为不需要提取，也可以直接search关键词
	# pattern = re.compile('重复|再说|回到|重(新)?说|((当前)|((这|上|前)一))步(骤)?')
	# if re.search(pattern, text):
	# 	return '', 2 

	# 根据原料推荐菜名
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(我有|用|使用)?(?P<raw>.+)?(可以|能够|能)(用来|拿来)?(做|作)(些)?什么(菜)?')
	result = re.match(pattern, text)
	if result:
		raw = result.group("raw")
		return raw, 5

	# 查询菜品做法 分四种为了能精准分离出菜名
	# 这道菜怎么做
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(这(道|个)?菜)((怎么(做|弄))|(的做法(是(什么|啥)?)?))')	
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 怎么做
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)?(?P<food>.+)?(((怎么(做|弄))|(的做法(是(什么|啥)?)?)))')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 查这道菜
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)(?P<food>.+)?(这(道|个)?菜)')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 查
	pattern = re.compile('((让)?芭乐大厨)?(查(询)?((一)?下)?)(?P<food>.+)?')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 根据原料推荐三种菜名后，用户选择一种
	# 这道菜
	pattern = re.compile('(我)?(想要|想|要)做(?P<food>.+)?(这(道|个)?菜)')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0
	# 不说这道菜
	pattern = re.compile('(我)?(想要|想|要)做(?P<food>.+)?')
	result = re.match(pattern, text)
	if result:
		food = result.group("food")
		return food, 0

	# 用户退出
	pattern = re.compile('.*退出.*')
	result = re.match(pattern, text)
	if result:
		return '', 4

	return '', -1

# text1 = "打开芭乐大厨"
# text2 = "下一步"
# text3 = "重复上一步的做法"
# text4 = "查询下宫保鸡丁怎么做"
# print(extractSlots("带把肘子", 0))
