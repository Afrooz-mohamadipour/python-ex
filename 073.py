#!/usr/bin/env python
# coding: utf-8

# In[18]:


favourite_foods={}
print("Please enter 4 of your favourite foods")
for i in range(1,5):
    favourite_food=input("==> ")
    favourite_foods[i]=favourite_food
print(favourite_foods)
not_desigred_food=int(input("Which of theese do you want to get rid of 'enter its number'? => "))
favourite_foods.pop(not_desigred_food)
print(favourite_foods)


# In[ ]:





# In[ ]:




