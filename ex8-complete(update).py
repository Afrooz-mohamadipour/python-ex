#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
from math import pi
import scipy.linalg as la


# In[24]:


vec1=np.array([-1.,4.,-9])
mat1=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
##   1=> calculating vec2
vec2=(pi/4)*vec1
##   2=> recalculate vec2 (it's cosines)
vec2=np.cos(vec2)
##   3=> calculating vec3
vec3= vec1 + 2*vec2
##   4=> norm of vec3
norm_vec3=la.norm(vec3)
##   5=> matrix row-column multiplication
vec4=vec3.dot(mat1)
##   6=> transpose calculation
mat1_transpose=np.transpose(mat1)
##   7=> determinate calculation
mat1_det=la.det(mat1)
##   8=> trace computation
mat1_trace=np.trace(mat1)
##   9=> find the smallest element
smallest_elm_in_vec1=np.min(vec1)
##   10=> index_finding_in_array
j = np.where(vec1==(np.min(vec1)))[0]
##   11=> find the smallest element in matrix
smallest_elm_in_mat1=np.min(mat1)


# In[40]:


##   12=> magic square
a = np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])
sum_of_columns=np.sum(a,0)
sum_of_rows=np.sum(a,1)
diag_of_a=np.diag(a)
diag_fliplr_of_a=np.diag(np.fliplr(a))
sum_of_diag=np.sum(diag_of_a)
sum_of_diag_fliplr_of_a=np.sum(diag_fliplr_of_a)
if np.min(sum_of_columns)==np.max(sum_of_columns):
    each_column_sum=np.min(sum_of_columns)
if np.min(sum_of_rows)==np.max(sum_of_rows):
    each_row_sum=np.min(sum_of_rows)

if each_column_sum==each_row_sum==sum_of_diag==sum_of_diag_fliplr_of_a:
    print("A is a magic matrix and all six number is equal to ",each_column_sum)


# In[46]:


##   13=> creatin random matrix
M=np.random.rand(10,10)
print(M)


# In[49]:


##   14=> creating sub matrixes
MUL=M[0:5,0:5]
MUR=M[0:5,5:10]
MLL=M[5:10,0:5]
MLR=M[5:10,5:10]

