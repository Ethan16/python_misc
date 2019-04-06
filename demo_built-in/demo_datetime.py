# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_datetime.py
@time: 19-4-6 上午12:41
"""

from datetime import datetime, timedelta, timezone

# now = datetime.now()
# print("[demo]Now is : ")
# print(now)

dt = datetime(2015, 4, 4, 20, 20, 20)
print(dt)

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)