raw = ['啤酒', '野山椒', '猪大排', '西红柿', '鸡', '白菜', '花生', '菠萝', '葱花', '酱牛肉', '鸭血', '鸡腿肉', '鸭胗', '黄花菜', '米粉', '米线', '尖椒', '羊腿', '鸡蛋清', '鳜鱼', '明虾', '青辣椒', '宽面', '油菜', '馕', '鸡架', '牛肉', '藜蒿', '虾', '干香菇', '冬笋', '鸡翅', '大葱', '肉桂粉', '小龙虾', '青红椒', '海带', '面条', '虾米', '鸡油', '地瓜粉', '小白菜', '红枣', '葡萄干', '茄子', '武昌鱼', '沙茶酱', '茭白', '猪蹄', '干辣椒', '榨菜', '肥牛', '细香葱', '大米', '荸荠', '藕', '芹菜', '猪前肘', '豌豆', '梅干菜', '土豆淀粉', '鱼翅', '面粉', '玉米淀粉', '葱白', '油豆腐', '酸豆角', '土豆', '蒜苔', '红糖', '鸭肉', '鸡胸脯肉', '莲子', '藕带', '碱水面', '木耳', '菜花', '大蒜', '芝麻', '盐焗粉', '朝天椒', '猪里脊肉', '杏鲍菇', '樱桃', '春笋', '牛筋', '红尖椒', '辣椒酱', '猪肉馅', '韭薹', '线椒', '三黄鸡', '红椒', '猪颈肉', '葱', '鱼头', '豆沙', '粽叶', '韭菜', '糖桂花', '黄瓜', '金针菇', '小米', '鱼唇', '蜜枣', '剁椒', '洋葱', '鲍鱼', '蕃茄酱', '鱿鱼', '猪肉', '白萝卜', '糯米', '香菇', '豆瓣酱', '虾仁', '蒸肉粉', '羊里脊肉', '莴笋', '生菜', '叉烧酱', '黄酱', '油豆皮', '火腿', '胡萝卜', '鹌鹑蛋', '猪肘', '茶树菇', '黑木耳', '碱', '粉丝', '豆豉', '香菜', '泡红椒', '咖喱', '糯米粉', '豆角', '青蒜', '猪肝', '青椒', '扯面', '母鸡', '鸡肉', '白酒', '腊肉', '鸡腿', '竹笋', '蜂蜜', '童子鸡', '花椒', '九层塔', '蒜苗', '酸菜', '腊肠', '豆腐片', '鱼膘', '干贝', '花生米', '生蚝', '鲤鱼', '黄豆芽', '咸肉', '羊排', '米饭', '卷心菜', '芦笋', '米酒', '豆腐皮', '果脯', '鳝鱼', '大虾', '大白菜', '鸡蛋', '可乐', '番茄酱', '猪大肠', '牛腩', '龙井茶', '西兰花', '红葱头', '大闸蟹', '面包糠', '草鱼', '莲藕', '鸭腿', '小葱', '墨鱼丸', '绿豆芽', '粉条', '排骨', '柿子椒', '海参', '黑芥', '豆腐', '白芝麻', '甜辣酱', '羊肉', '蔓越莓', '里脊肉', '五花肉']
def splitMateria(raw_string):
	materias = []
	if raw_string == None:
		return []
	for materia in raw:
		if raw_string.find(materia) != -1:
			materias.append(materia)
	return materias

if __name__ == '__main__':
	txt = '牛腩牛肉猪肉'
	print(splitMateria(txt))