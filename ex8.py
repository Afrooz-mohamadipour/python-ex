#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import scipy.linalg as la
from math import pi
vec1 = np.array([-1. , 4. ,-9.])
mat1 = np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
vec2=(np.pi/4)*vec1
vec2=np.cos(vec2)
vec3=vec1+2*vec2
norm_vec3 = la.norm(vec3)
vec4=np.dot(vec3,mat1)
mat1_tr=mat1.transpose()
mat1_det=np.linalg.det(mat1)
mat1_trace=np.trace(mat1)
smallest_elm_vec1=vec1.min()




# In[11]:


a = np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
coloms_sum=np.sum(a)
row_sum=np.sum(a.transpose())

min_cl=np.min(coloms_sum)
min_r=np.min(row_sum)

max_cl=np.max(coloms_sum)
max_r=np.max(row_sum)

sum_diag=np.sum(np.diag(a))
sum_fliplr=np.sum(np.fliplr(a))
if min_cl==min_r and max_cl==max_r and sum_diag==sum_fliplr:
    print("All right")


# In[12]:


M = np.random.rand(10,10)


# In[ ]:




