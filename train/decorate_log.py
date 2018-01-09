#!C:\Python27\python.exe

def log(f):
	def fn(x):
		print 'call '+f.__name__+'()...'
		return f(x)
	return fn
@log
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))

print factorial(10)
