#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums=[]
for i in range(1,4):
    num=int(input("enter a number"))
    nums.append(num)
    print(nums)
ans = input("Do you still want the last number saved ? ")
if ans=="no":
    nums.pop()
    print(nums)


# In[ ]:




