#C:\python27

import time,functools

def performance(unit):
    def performance_info(f):
    	@functools.wraps(f)
        def wrapper(*args,**kw):
            r=f(*args,**kw)
            print '[%s] call %s() in %s'%(unit,f.__name__,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            return r
        return wrapper
    return performance_info

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

@performance('UNIX')
def add(x,y):
	return x+y

print factorial(10)
print factorial.__name__
print add(35555554,78)
print add.__name__