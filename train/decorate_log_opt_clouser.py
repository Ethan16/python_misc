#!C:\python27

def log(prefix):
	def log_decorate(f):
		def wrapper(*args,**wk):
			print '[%s] call %s()...'%(prefix,f.__name__)
			return f(*args,**wk)
		return wrapper
	return log_decorate
@log('DEBUG')
def add(x,y):
	return x+y
@log('INFO')
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print add(45,88)
print factorial(8)