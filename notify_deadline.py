#!/usr/bin/python
#coding:utf-8

import time
import datetime
import sys
from sys import argv

def get_message(msg, year, month, day):
    today = datetime.date.today()
    deadline = datetime.date(int(year),int(month),int(day))
    result = deadline - today
    print(msg)
    if result.days < 0:
        print("距離 {}-{}-{} 已經到期!!".format(year, month, day))
    else:
        print("距離 {}-{}-{} 還剩 {} 天!!".format(year, month, day, result.days))

get_message("提醒宇柏,心無旁鶩\n大學學測考試:", argv[1], argv[2], argv[3])
get_message("\n提醒宇柏,再接再勵\n大學音樂組術科考試:", argv[4], argv[5], argv[6])
