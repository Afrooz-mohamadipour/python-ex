#!/usr/bin/env python
# coding: utf-8

# In[2]:


first_num=int(input("Please enter a number => "))
second_num=int(input("please enter another number => "))
total=first_num+second_num
ans = 'y'
while ans=='y':
    ans=input("Do you want to add another number ?  press 'y' if your answer is yes")
    if ans!='y':
        print("The total is =>",total)
        break
    new_num=int(input("Please Enter the new number"))
    total=total+new_num


# In[ ]:




