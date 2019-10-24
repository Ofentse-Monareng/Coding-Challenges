#!/usr/bin/env python
# coding: utf-8

# In[1]:


class TimesTable(object):
    
    def __init__(self,number,end = 15):
        self.number = number
        self.end = end
    
    def times_table(self):

        for num in range(1,self.end + 1):
            print('{} * {} = {}'.format(self.number,num,self.number*num))

