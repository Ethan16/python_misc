#!C:\python27

import functools

sorted_ignore_case=functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.lower(),s2.lower()))

print sorted_ignore_case(['mango','Critical','haha','laming','bob', 'about', 'Zoo', 'Credit'])