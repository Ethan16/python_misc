#!C:\python27

class Person(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
		self.get_grade=lambda :'A'
p1=Person('yuanyuan',70)

print p1.get_grade
print p1.get_grade()