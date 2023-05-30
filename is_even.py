#!/usr/bin/env python
# coding: utf-8

# In[23]:



def is_even(x):
    if not isinstance(x, int):
        raise TypeError("Please input an integer")
    else:
        return (x % 2 == 0)


is_even(2)


# In[ ]:




