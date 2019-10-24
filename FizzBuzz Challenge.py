#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Printing(object):
    def __init__(self,start = 1,end = 101):
        self.start = start
        self.end = end
    
    def print_words(self):

        for i in range(self.start,self.end):

            if i % 3 == 0 and i % 5 == 0:
                print('Fizz Buzz')

            elif i % 3 == 0:
                print('Fizz')

            elif i % 5 == 0:
                print('Buzz')

