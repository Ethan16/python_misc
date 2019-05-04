# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: 16_format_datetime.py
@time: 2019/5/3 下午9:04
@description: 题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""

import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d-%m-%Y'))

    # 创建日期对象
    birthDay = datetime.date(2019, 5, 3)
    print(birthDay.strftime('%d-%m-%Y'))

    # 日期运算
    nextDay = birthDay + datetime.timedelta(days=1)
    print(nextDay.strftime('%d-%m-%Y'))

    # 日期替换
    firstDay = birthDay.replace(year=birthDay.year+1)
    print(firstDay.strftime('%d-%m-%Y'))
