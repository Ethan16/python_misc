#!C:\Python27\

def log(f):
	def fn(*args,**kw):
		print 'call '+f.__name__+'()...'
		return f(*args,**kw)
	return fn

@log
def add(x,y):
	return x+y
print add(45,88)