# -*- coding: utf-8 -*-
"""HackerRank_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wh3d2f0FwuGJMRkcUhBJDkD-6Wq-t3rM
"""

def table():
  which_table = int(input("Which table do you want to know : "))

  print('Okay, so you want to know the the table of this number. Okay, no worries.')
  print('The table of the input number is as follows : ')
  print('\n')

  for i in range(1,11):
    print(which_table * i)

table()

