#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci(object):
    
    def __init__(self,n):
        self.n = n
    
    def first_n_fibonacci(self):
        prev_num = 0
        curr_num = 1
        print(prev_num)
        print(curr_num)

        for count in range(1,self.n - 1):
            next_num = prev_num + curr_num
            print(next_num)
            prev_num = curr_num
            curr_num = next_num

