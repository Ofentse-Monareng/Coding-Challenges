#!/usr/bin/env python
# coding: utf-8

# In[1]:


class NumberPattern(object):
    
    def __init__(self,start,end = 0,step = -1):
        self.start = start
        self.end = end
        self.step = step
    
    def pattern(self):
        
        numbers = [i for i in range(self.start,self.end,self.step)]

        for iter_ in range(len(numbers)*2):
            if iter_ < len(numbers):
                length = 0
                for num in numbers[iter_:]:
                    print('',num,end='')
                    length += 1
                    if  length == len(numbers[iter_:]):
                        print('\n')
            else:
                length = 0
                for num in numbers[-(iter_- (len(numbers) - 1)):]:
                    print('',num,end='')
                    length += 1
                    if  length == len(numbers[-(iter_- (len(numbers) - 1)):]):
                        print('\n') 


# In[8]:


num_pattern = NumberPattern(10)
num_pattern.pattern()

