#a redesign to add ranges instead of adding two conditions would be nice

class Condition:
	def __init__(self, type, operator, num):
		self.type = type
		self.operator = operator
		self.num = num
		
	def check(self, neighbors):
		if self.operator == "LESS":
			return neighbors[self.type] < self.num
		elif self.operator == "LESS_EQUAL":
			return neighbors[self.type] <= self.num
		elif self.operator == "EQUAL":
			return neighbors[self.type] == self.num
		elif self.operator == "GREATER_EQUAL":
			return neighbors[self.type] >= self.num
		elif self.operator == "GREATER":
			return neighbors[self.type] > self.num

class Rule:
	def __init__(self, status, conditions, result):
		self.status = status
		self.conditions = conditions
		self.result = result
		
	def check(self, value, neighbors):
		if value == self.status:
			for condition in self.conditions:
				if not condition.check(neighbors):
					return False
			return True
		else:
			return False

		
#DEPRECATED
class MooreRules:
	def conway(status, num):
		if status == 1 and num < 2:
			return 0
		elif status == 1 and num < 4:
			return 1
		elif status == 1:
			return 0
		elif status == 0 and num == 3:
			return 1
		else:
			return 0
