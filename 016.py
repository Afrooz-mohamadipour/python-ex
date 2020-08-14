#!/usr/bin/env python
# coding: utf-8

# In[6]:


rainy = input("Is it rainy today ?")
rainy=rainy.lower()
if rainy=='yes':
    windy=input("Is it also windy today?")
    windy=windy.lower()
    if windy =='yes':
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")


# In[ ]:




