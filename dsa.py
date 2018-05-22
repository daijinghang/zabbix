#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
if os.path.exists('1232.log'):
    data=open('1232.log')

    for each_line in data:
        if not each_line.find(':') == -1:
            (role,line_spoken)= each_line.split(':',1)
            print(role,end='')
            print('info:',end='')
            print(line_spoken,end='')
        data.close()
else:
    print('123123123213123123123!3')