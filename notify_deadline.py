#!/usr/bin/python
#coding:utf-8

import time
import datetime
import sys
from sys import argv

today = datetime.date.today()
deadline = datetime.date(int(argv[1]),int(argv[2]),int(argv[3]))
result = deadline - today
if result.days < 0:
    message = "距離 {}-{}-{} 已經到期!!".format(argv[1], argv[2], argv[3])
else: 
    message = "距離 {}-{}-{} 還剩 {} 天!!".format(argv[1], argv[2], argv[3], result.days)
print("提醒大家再接再勵\n全民英檢考試:")
print(message)
