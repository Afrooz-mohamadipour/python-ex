#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
print("You'r invited guests are : ")
print(guests)
choosen_name=input("Please type one of the names => ")
ind =guests.index(choosen_name)
print("The position of your typed name in list is ",ind)
making_sure_for_invitation=input("Do you still want this person to come to your paty ? ")
if making_sure_for_invitation=="no":
    guests.pop(ind)
print(" ")
print(guests)

