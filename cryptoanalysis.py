# -*- coding: utf-8 -*-
"""Cryptoanalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c1Gv04UM54sAFkV5-IAVZ0cTCQM9i-T0
"""

import collections
import pprint
with open('/content/Cryptogram.txt', 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)

# words = []
# with open('/content/quiz2.txt','r') as f:

#     for row in f:
#         for each_char in str(row):
#             words.append(each_char)
# print(words)
# digraphs = []
# for i in cr:
#   digraphs.append(words[i]:words[i+1])
# print(digraphs)

import operator
x = open('/content/Cryptogram.txt')
x = x.read()
n = 2
split = [x[i : i + n] for i in range(0, len(x)-n+1)]
d = {x:split.count(x) for x in split}
di = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print ("The Digrpahs are:\n",di)

x = open('/content/Cryptogram.txt')
x = x.read()
n = 3
split = [x[i : i + n] for i in range(0, len(x)-n+1)]
d = {x:split.count(x) for x in split}
di = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print ("The Trigraphs are:\n",di)

x = open('/content/Cryptogram.txt')
x = x.read()
n = 4
split = [x[i : i + n] for i in range(0, len(x)-n+1)]
d = {x:split.count(x) for x in split}
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print ("The Trigraphs are:\n",sorted_d)

x = open('/content/Cryptogram.txt')
x = x.read()
n = 5
split = [x[i : i + n] for i in range(0, len(x)-n+1)]
d = {x:split.count(x) for x in split}
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print ("The Trigraphs are:\n",sorted_d)

vcount =  0
x = open('/content/Cryptogram.txt')
for i in x:
    if( i=='A','E','I','O','U'):
        vcount +=1
#      count = collections.Counter(info.read().i)
#       value = pprint.pformat(count)
#    print(value)
        
print('The Number of Vowels in text file :', vcount)



