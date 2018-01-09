#!C:\python27

import types

def fn_get_grade(self):
	if self.score>=80:
		return 'A'
	elif self.score>=60:
		return 'B'
	else:
		return 'C'
class Person(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
p1=Person('xiaoming',56)
p1.get_grade=types.MethodType(fn_get_grade,p1,Person)

print p1.get_grade
print p1.get_grade()
