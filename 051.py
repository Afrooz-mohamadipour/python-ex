#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("there are 10 green bottles hanging on the wall")
num = 10
while num>0:
    print("there are ",num," green bottles hanging on the wall ",num," green bottles hanging on the wall, and if 1 green bottle should accidently fall ")
    num=num-1
    new_num=int(input("How many green bottles will be hanging on the wall ? "))
    while new_num!=num:
        print("NO , try again")
        new_num=int(input("How many green bottles will be hanging on the wall ? "))
    print("There will be ",num," green bottles hanging on the wall")
print("There are no more green bottles hanging on the wall")


# In[ ]:




