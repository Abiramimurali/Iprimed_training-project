#!/usr/bin/env python
# coding: utf-8

# In[25]:


alldatas={}
aval_tic={'master':50,'chakra':46,'eswaran':10}
m={'master':300,'chakra':250,'eswaran':275}
combo={'combo_1': 500, 'combo_2':450,'combo_3':300}


# In[43]:


def snacks_order():

    print("-----------------list of combo-----------------------")
    for i in combo:
        print(i,":",combo[i],".Rs")
    print("-----------------------------------------------------")
    c=input("Enter your combo: ").lower()
    values['snacks']=c
    n_c= int(input("No. of quality: "))
    values['quality']=n_c
    s_p=n_c*combo[c]
    rate.append(s_p)
    values['snacks_price']=s_p
    print("Your total snack amount is: ",rate[1])
    
    
def book_tickets(m):
    global x,n
    x=input("choose the movie: ").lower()
    values['movie_name']=x
    n=int(input("No. of ticket: "))
    values['no_tickets']=n
    if n<=int(aval_tic[x]):
        rate.append(n*m[x])
        values['ticket_price']=n*m[x]
        aval_tic[x]-=n
     
    else:
        print("Tickets are not available for your required, only we have",aval_tic[x],"tickets")
    print("Your total ticket price is: ",*rate)
    snacks=input("Do you want snacks? Type y/N: ")
    if(snacks=='y'):
        snacks_order()
    else:
        values['snacks']='null'
        values['quality']=0
        values['snacks_price']=0
        print("Your total ticket amount is: ",*rate)
        
    

def display_movies():
    print("------List of movies & price of the tickets--------")
    for i in m:
        print(i,":",m[i],".Rs")
    print("---------------------------------------------------")
    book_tickets(m)

    
print("press 1 for booking tickets \npress 2 for ticket cancel")
choice=int(input())
user_name=input("Enter your User Name: ")
rate=[]
data={}
values={}
if(choice==1):
    display_movies()
    print("Thank you! Your total price is: ",sum(rate))
    values['Total_price']=sum(rate)
    data[user_name]=values
    alldatas[user_name]=data[user_name]
    cancel=input("If you want to cancel the ticket? yes-> press 1 No-> press 2: ")
    ticket_cancel

else:
    ticket_cancel()



# In[44]:


print("ALL DATAS ")
for i,j in alldatas.items():
    print(i,':',j)
print(aval_tic)


# In[33]:


import random

def ticket_cancel():
    #print(alldatas)
    if(user_name not in alldatas):
        print("Check your user name")
    elif(user_name in alldatas):
        code=random.randrange(1000,9999)
        print(code)
        code_inp=input("Enter your four digit code: ")
        if(int(code_inp)==int(code)):
            #print("y")
            m1=alldatas[user_name]['movie_name']
            #print(m1)
            aval_tic[m1]+=alldatas[user_name]['no_tickets']
            print(aval_tic)
            del alldatas[user_name]
            print(alldatas)
   


# In[ ]:




