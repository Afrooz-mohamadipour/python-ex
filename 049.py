#!/usr/bin/env python
# coding: utf-8

# In[1]:


compnum=50
num=int(input("Please enter a number => "))
count=0
while num!= compnum:
    count=count+1
    if num<compnum:
        print("Too low")
    elif num>compnum:
        print("Too high")
    num=int(input("Please enter a number => "))
print("Well done , you took ",count," attepms")
    


# In[ ]:




