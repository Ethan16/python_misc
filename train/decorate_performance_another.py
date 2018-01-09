#!C:\python27

import time

def performance(f):
	def exec_time(*args,**kw):
		time_s=time.time()
		res=f(*args,**kw)
		time_e=time.time()
		print 'call %s in %fs'%(f.__name__,(time_e-time_s))
		return res
	return exec_time

@performance
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print factorial(20)