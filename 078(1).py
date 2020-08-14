#!/usr/bin/env python
# coding: utf-8

# In[6]:


tv_programmes=["خندوانه","فوتبال برتر","دورهمی ","اخبار شبانگاهی"]
for program in tv_programmes:
    print(program)
new_program=input("please add another show")
ind=int(input("please enter the position of your added program"))
tv_programmes.insert(ind,new_program)
for program in tv_programmes:
    print(program)


# In[ ]:




