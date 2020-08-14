#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from math import pi
x = 10
#1  => calculation of square and cube is :
#      square **2  and cube**3
#      for square calculation you can use => np.square(x)
theta = 3.14
sin_of_theta=np.sin(theta)
cos_of_theta=np.cos(theta)
#4 =>  Radian
meshpoints = np.linspace(-1,1,500)
#6 as indexes start from 0 then 53th element is => meshpoints[52]
print(meshpoints[52])
plt.plot(meshpoints,np.sin(2*pi*meshpoints))


# In[5]:


np.cbrt(x)


# In[ ]:




