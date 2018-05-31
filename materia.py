raw = ['花生米', '剁椒', '茭白', '可乐', '黄花菜', '青辣椒', '肉桂粉', '碱', '莲子', '土豆', '排骨', '鸡翅', '鱿鱼', '菠萝', '鲍鱼', '红糖', '草鱼', '大葱', '龙井茶', '猪大肠', '白菜', '泡红椒', '白芝麻', '猪肉', '青蒜', '扯面', '猪颈肉', '芹菜', '鸡肉', '蒸肉粉', '蜜枣', '猪前肘', '黄豆芽', '红尖椒', '鸡架', '里脊肉', '绿豆芽', '鲤鱼', '火腿', '细香葱', '竹笋', '油豆皮', '葱', '野山椒', '生蚝', '馕', '地瓜粉', '九层塔', '大米', '花椒', '鱼翅', '春笋', '金针菇', '洋葱', '芝麻', '青红椒', '三黄鸡', '卷心菜', '木耳', '母鸡', '藜蒿', '油豆腐', '猪蹄', '豆瓣酱', '豆沙', '糯米粉', '羊排', '黄酱', '羊肉', '鱼膘', '豆豉', '面粉', '酱牛肉', '小龙虾', '豆腐', '腊肠', '香菜', '大虾', '鳜鱼', '酸豆角', '粉条', '糯米', '粉丝', '蔓越莓', '生菜', '朝天椒', '冬笋', '酸菜', '蕃茄酱', '腊肉', '韭菜', '干香菇', '沙茶酱', '线椒', '鸭肉', '荸荠', '童子鸡', '小米', '鸡蛋', '米粉', '梅干菜', '鳝鱼', '豌豆', '羊里脊肉', '粽叶', '黑木耳', '大闸蟹', '茄子', '猪肉馅', '米线', '藕', '西兰花', '菜花', '海带', '明虾', '香菇', '花生', '鸭腿', '玉米淀粉', '糖桂花', '葡萄干', '面条', '宽面', '樱桃', '莴笋', '米酒', '蒜苔', '青椒', '黑芥', '榨菜', '虾', '海参', '猪肘', '鹌鹑蛋', '鸡油', '豆腐皮', '甜辣酱', '葱花', '鸡蛋清', '猪大排', '面包糠', '啤酒', '叉烧酱', '红葱头', '莲藕', '韭薹', '鸭血', '大白菜', '米饭', '柿子椒', '尖椒', '胡萝卜', '黄瓜', '干辣椒', '杏鲍菇', '干贝', '辣椒酱', '茶树菇', '鸭胗', '鸡', '碱水面', '大蒜', '豆角', '墨鱼丸', '虾米', '土豆淀粉', '蜂蜜', '葱白', '红椒', '蒜苗', '肥牛', '咸肉', '鱼唇', '番茄酱', '小白菜', '羊腿', '鸡胸脯肉', '西红柿', '鸡腿肉', '鱼头', '虾仁', '猪肝', '芦笋', '小葱', '武昌鱼', '白酒', '藕带', '五花肉', '豆腐片', '果脯', '红枣', '盐焗粉', '鸡腿', '白萝卜', '猪里脊肉', '番茄']

def splitMateria(raw_string):
	materias = []
	if raw_string == None:
		return []
	for materia in raw:
		if raw_string.find(materia) != -1:
			materias.append(materia)
	return materias
