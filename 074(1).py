#!/usr/bin/env python
# coding: utf-8

# In[1]:


colors=["pink","purple","orange","green","gray","white","black","yellow","blue","red"]
choosed_colors=[]
print(colors)
starting_number=int(input("Please choose a starting number between 0 to 4 => "))
end_number=int(input("Please choose an end number between 5 to 9 => "))
for i in range(starting_number,end_number):
    choosed_colors.append(colors[i])
print(choosed_colors)


# In[ ]:




