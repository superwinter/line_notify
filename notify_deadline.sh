#!/bin/sh
python /Users/winter/line_notify/notify_deadline.py $1 $2 $3 $4 $5 $6 > /tmp/log
python /Users/winter/line_notify/line_notify.py $7 "" "`cat /tmp/log`"
