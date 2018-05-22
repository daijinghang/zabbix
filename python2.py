#!/usr/bin/env python
# -*- coding:utf-8 -*-
temp = input("你猜我心里想的数字是什么：")

guess = int(temp)
i = 2
while guess != 8 and i <= 3 :
    i=i+1
    if not i.strip():
        if  guess > 8:
            temp = input("猜大了 请重新输入：")
            guess = int(temp)
        elif guess < 8:
            guess = int(input("猜小了 请重新输入："))
    else:
        i != ""
        print("不能为空")


if i <3:
    print("恭喜你猜对了，游戏结束了")
else:
    print("三次都没有猜对，游戏结束了")



