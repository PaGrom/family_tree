#-*- coding: utf-8 -*-

# родитель ли?
def is_parent(parent, child):
	if child.father == parent or child.mother == parent:
		return True
	else:
		return False

# мужчна ли?
def is_man(human):
	if human.sex == 'male':
		return True
	else:
		return False

# женщина ли?
def is_woman(human):
	if human.sex == 'female':
		return True
	else:
		return False

# отец ли?
def is_father(parent, child):
	if is_parent(parent, child):
		if is_man(parent):
			return True
		else:
			return False
	else:
		return False

# внучка ли?
def is_granddaughter(grandparent, granddaughter):
	if not is_woman(granddaughter):
		return False

	for child in grandparent.female_childs:
		for grandchild in child.female_childs:
			if grandchild == granddaughter:
				return True

	for child in grandparent.male_childs:
		for grandchild in child.female_childs:
			if grandchild == granddaughter:
				return True

	return False

# дядя ли?
def is_uncle(uncle, nephew):
	if not is_man(uncle):
		return False
	# так никогда нельзя писать
	if nephew.father:
		if nephew.father.father:
			for human in nephew.father.father.male_childs:
				if human == uncle:
					return True

		if nephew.father.mother:
			for human in nephew.father.mother.male_childs:
				if human == uncle:
					return True

	if nephew.mother:
		if nephew.mother.father:
			for human in nephew.mother.father.male_childs:
				if human == uncle:
					return True

		if nephew.mother.mother:
			for human in nephew.mother.mother.male_childs:
				if human == uncle:
					return True

	return False

# двоюродная сестра ли?
def is_cousin(cousin1, cousin2):
	if not is_woman(cousin2):
		return False
	# а так темболее никогда нельзя писать
	if cousin1.father:
		if cousin1.father.father:
			for human1 in cousin1.father.father.male_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True
			for human1 in cousin1.father.father.female_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True

		if cousin1.father.mother:
			for human1 in cousin1.father.mother.male_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True
			for human1 in cousin1.father.mother.female_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True

	if cousin1.mother:
		if cousin1.mother.father:
			for human1 in cousin1.mother.father.male_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True
			for human1 in cousin1.mother.father.female_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True

		if cousin1.mother.mother:
			for human1 in cousin1.mother.mother.male_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True
			for human1 in cousin1.mother.mother.female_childs:
				for human2 in human1.female_childs:
					if human2 == cousin2:
						return True

	return False

class Node():
	"""
	Класс, описывающий узел генеалогического дерева
	"""
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

		self.mother = None
		self.father = None
		self.male_childs = []
		self.female_childs = []

	def add_child(self, child):
		"""
		Добавить ребенка
		"""
		if child.sex == 'male': #если мальчик
			self.male_childs.append(child)
		elif child.sex == 'female': #если девочка
			self.female_childs.append(child)

		child.add_parent(self)

	def add_parent(self, parent):
		"""
		Добавить родителя
		"""
		if parent.sex == 'male':
			self.father = parent
		elif parent.sex == 'female':
			self.mother = parent

	def __str__(self):
		"""
		Красивый вывод информации
		"""
		print "Name:\t", self.name
		print "Sex:\t", self.sex

		if self.mother == None:
			print "Mother:\tNone"
		else:
			print "Mother:\t", self.mother.name

		if self.father == None:
			print "Father:\tNone"
		else:
			print "Father:\t", self.father.name

		print "Childs:"
		print "\tMale childs:"
		if self.male_childs:
			for child in self.male_childs:
				print "\t\t", child.name
		else:
			print "\t\tNone"
		print "\tFemale childs:"
		if self.female_childs:
			for child in self.female_childs:
				print "\t\t", child.name
		else:
			print "\t\tNone"

		return ""

def main():
	# инициализация узлов
	ivan = Node('Иван', 'male')
	maria = Node('Мария', 'female')

	polina = Node('Полина', 'female')
	petya = Node('Петя', 'male')
	dasha = Node('Даша', 'female')
	denis = Node('Денис', 'male')

	aleksandr = Node('Александр', 'male')
	sereja = Node('Сережа', 'male')
	sveta = Node('Света', 'female')

	# инициализация связей
	ivan.add_child(petya)
	maria.add_child(petya)

	ivan.add_child(dasha)
	maria.add_child(dasha)

	petya.add_child(aleksandr)
	polina.add_child(aleksandr)

	dasha.add_child(sereja)
	denis.add_child(sereja)

	dasha.add_child(sveta)
	denis.add_child(sveta)

	print "Является ли Света внучкой Ивана?"
	print is_granddaughter(ivan, sveta) # True
	print "Является ли Петя дядей Светы?"
	print is_uncle(petya, sveta) # True
	print "Является ли Света двоюродной сестрой Пети?"
	print is_cousin(petya, sveta) # False
	print "Является ли Света двоюродной сестрой Александра?"
	print is_cousin(aleksandr, sveta) # True

if __name__ == '__main__':
	main()