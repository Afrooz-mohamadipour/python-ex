#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input("Please enter name of the person you want to invite to your party ")
print(name,"now has been invited to your party")
count=1
ans=input("Do you want to invite somebody else ?")
while ans=='y':
    count=count+1
    name=input("Please enter name of the person you want to invite to your party ")
    print(name,"now has been invited to your party")
    ans=input("Do you want to invite somebody else ?")
print(count,"people has been invited to your party")
    


# In[ ]:




