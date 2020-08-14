#!/usr/bin/env python
# coding: utf-8

# In[1]:


day = int(input("please enter the day =>"))
month = int(input("please enter the month =>"))
year = int(input("please enter the desigred year =>"))
days=0
days_of_each_month=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year%400==0 or(year%4 == 0 and year%100 !=0)):
    print("It's a leap year")
    days_of_each_month[1]=days_of_each_month[1]+1
else:
    print("it's an ordinary year")
for i in range(0,(month-1)):
    days=days_of_each_month[i]+days
days=days+day


print("the final result is  ===>>  ",days)
        


# In[ ]:




