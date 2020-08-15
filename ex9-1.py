#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from math import pi


# In[2]:


def f(x):
    y=(np.sin(pi*x))*(np.exp(-x/10))
    return y
def g(x):
    y=x*(np.exp(-x/3))
    return y


# In[21]:


x=np.linspace(0,10)
plt.plot(x,f(x))
plt.plot(x,g(x))
plt.ylabel("Y-axis")
plt.xlabel("x-axis")
plt.legend("f""g")

