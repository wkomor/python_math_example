# -*- coding: utf-8 -*-
"""
title              :pand
description        :
date               :15.11.16
"""
from pandas import read_csv

__author__ = 'Vitold Komorovski'

df1 = read_csv("df1.csv")
df2 = read_csv("df2.csv")

print(df1)
print('\n')
print(df2)
print('+++++++++++++++++++++++++++++\n\n')

country = [u'Украина',u'РФ',u'Беларусь',u'РФ',u'РФ']
df2.insert(1,'country',country)

print(df2)
print('+++++++++++++++++++++++++++++\n\n')

t = df2[df2.country == u'Украина']
t.shop = 345

df2 = df2.append(t)

print(df2)

print('+++++++++++++++++++++++++++++\n\n')

res = df2.merge(df1, 'left', on='shop')

pivot_table = res.pivot_table(['qty'],['country'], aggfunc='sum', fill_value = 0)

print(pivot_table)