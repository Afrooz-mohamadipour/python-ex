#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Pleae enter name of three people you want to invite to your party ")
guests=[]
for i in range(0,3):
    guest=input("=> ")
    guests.append(guest)
a=0
while a==0:
    question=input("Do you want to add another name ?")
    if question == "yes":
        new_guest=input("Please enter your new guest name => ")
        guests.append(new_guest)
    elif question=="no":
        number_of_invited_guests=len(guests)
        print("You've invited ",number_of_invited_guests," people to the party")
        a=1
    
        
        

