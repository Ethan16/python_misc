#!C:\python27

import functools

#sorted(...):sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

sorted_ignore_case=functools.partial(sorted,key=str.upper)

print sorted_ignore_case(['mango','Critical','haha','laming','bob', 'about', 'Zoo', 'Credit'])