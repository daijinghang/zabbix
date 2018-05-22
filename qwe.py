#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
# if os.path.exists('1232.log'):


os.chdir('/Users/daijing/PycharmProjects/untitled27')

the_file = open('1232.log')
print(the_file.readline(),end='')
the_file.seek(0)

for each_lione in the_file:
  print(each_lione,end='')

