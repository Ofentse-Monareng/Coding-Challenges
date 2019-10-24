#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Swaps(object):
    def __init__(self,sequence):
        self.sequence = sequence
    def minimum_swaps(self):
        expected = min(self.sequence)
        for element in self.sequence:
            if element == expected:
                expected += 1

        return len(self.sequence) - (expected - min(self.sequence))


# In[11]:


Swaps([4,3,2,1]).minimum_swaps()

