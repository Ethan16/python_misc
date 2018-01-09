#!C:\python27

import functools

def log(f):
	@functools.wraps(f)
	def wrapper(*args,**kw):
		print 'call ...'
		return f(*args,**kw)
	return wrapper
@log
def f2(x):
	pass
print f2.__name__