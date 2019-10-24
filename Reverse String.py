#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class StringReverse(object):
    
    def __init__(self,string):
        self.string = string
    
    def reverse_string(self):
        str_ = ''
        for letter in self.string:
            str_ = letter + str_
        return str_

