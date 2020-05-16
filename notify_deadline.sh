#!/bin/sh
python notify_deadline.py $1 $2 $3 > /tmp/log
python line_notify.py $4 "" "`cat /tmp/log`"
