raw = ['五花肉', \
		'里脊肉', '黄豆芽', '大白菜', '鸡蛋清', \
		'草鱼', '大葱', '干辣椒', '大蒜', \
		'豆腐', '猪肉馅', '豆瓣酱', \
		'土豆', '青辣椒', '茄子', \
		'鸡翅', '可乐', \
		'排骨', \
		'猪里脊肉', '胡萝卜', '竹笋', '茭白', '木耳', '青椒', \
		'鸡腿肉', \
		'鸡蛋', '西红柿']

def splitMateria(raw_string):
	materias = []
	if raw_string == None:
		return []
	for materia in raw:
		if raw_string.find(materia) != -1:
			materias.append(materia)
	return materias
