#!/usr/bin/env python
# coding: utf-8

# In[6]:


three_digit_numbers=[121,454,787,159]
for i in three_digit_numbers:
    print(i)
new_number = int(input("Please enter a three-digit number => "))
try:
    ind=three_digit_numbers.index(new_number)
    print("The index of your chosen number in list is ",ind)
except:
    print("That is not in the list")


# In[ ]:




