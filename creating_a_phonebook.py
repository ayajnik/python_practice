# -*- coding: utf-8 -*-
"""creating a phonebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mTahABHrYxq6ilTzpQbH6tmmA1DmzLFb
"""

def entries():
    global a 
    global b
    global res
    global res_1

    a = list(map(str, input("Enter a multiple value: ").split(','))) 
    b = list(map(int, input("Enter a multiple value: ").split(','))) 
    print('\n')
    #print (a)
    #print('\n')
    #print (b)
    #print('\n')
    res = {a[i]: b[i] for i in range(len(a))}
    res_1 = dict(zip(a, b)) 

    print(res)
    print('\n')
    print('Dictionary made from other method : ',res_1)
    print('\n')
    print('Dictionary has been made.')

    
entries()

def findone():
  global c
  global d
  c = input("Enter a name to find if there's someone there or not : ")
  d = input("Enter the number you wish to find : ")
  if c not in res.keys():
    print('There is no such person in the phonebook.')
  else:
    if d not in res.values():
      print('There is no such number in phonebook.')

    for c in res.keys():
      print('You found the right guy.', c)

    for d in res.values():
      print('You found the right number.', d) 



findone()
