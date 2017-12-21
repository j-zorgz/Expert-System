from globalx import *
from is_x import *

def exec_operand(stack, operand):
	val1 = stack.pop()
	val2 = stack.pop()
	if (operand == '+'):
		if (val1 == -1 and val2 == -1):
			stack.append(-1)
		elif (val1 == 0 or val2 == 0):
			stack.append(0)
		elif (val1 == -1 or val2 == -1):
			stack.append(-1)
		else:
			stack.append(1)
	elif (operand == '|'):
		if (val1 == -1 and val2 == -1):
			stack.append(-1)
		elif (val1 == 1 or val2 == 1):
			stack.append(1)
		elif (val1 == -1 or val2 == -1):
			stack.append(-1)
		else:
			stack.append(0)
	elif (operand == '^'):
		if (val1 == -1 or val2 == -1):
			stack.append(-1)
		elif (val1 == val2):
			stack.append(0)
		else:
			stack.append(1)
		pass

def is_true(expression):
	stack = []
	while (True):
		if (len(expression) == 0):
			return stack.pop()
		if (is_fact(expression[0])):
			stack.append(dico[expression[0]])
		elif (is_b_operand(expression[0])):
			exec_operand(stack, expression[0])
			print stack
		elif (expression[0] == '!'):
			value = stack.pop()
			if (value == 1):
				value = 0
			elif (value == 0):
				value = 1
			else:
				value = -1
			stack.append(value)
		expression = expression[1:]
