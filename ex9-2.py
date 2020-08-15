#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from math import pi


# In[6]:


def cardoid(ro,theta):
    r=ro+np.cos(theta)
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    plt.plot(x,y)


# In[11]:


theta = np.linspace(0,2*pi)
for i in [.8,1,1.2]:
    cardoid(i,theta)
plt.legend(["0.8","1.0","1.2"])


# In[ ]:




