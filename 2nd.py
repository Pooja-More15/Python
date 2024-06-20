#!/usr/bin/env python
# coding: utf-8

# In[1]:


#if-else statement
a=630
b=1250
if a>b:
    print("a is greater")
    print("In True block")
    c=a+b
    print(c)
else:
    print("b is greater")
    print("In False Block")
    c=a*b
    print(c)


# In[2]:


a=12000
b=1300
if(a>b):
    print(a,"is greater")
else:
    print("greater number is:",b)


# In[8]:


for i in range(5,10):
    print(i)
print("bye")



# In[9]:


for i in range(1,11):
    print(i)


# In[10]:


for i in range(1,11,2):
    print(i)


# In[11]:


for i in range(2,11,2):
    print(i)


# In[12]:


for i in range(1,11,3):
    print(i)


# In[14]:


for i in range(1,11):
    if i==5:
        print("same")
        break
    else:
        print(i)


# In[15]:


for num in range(11):
    print(num,num*num)


# In[17]:


for num in range(11):
    print(num,num**num)


# In[18]:


for i in range(1,31,5):
    print(i,"@")


# In[19]:


subject="Science"
for i in subject:
    print(i)


# In[20]:


name="Snehal"
for i in range(3,7):
    print(name*i)


# In[21]:


movie="Drishyam"
for letter in movie:
   # print(letter)
    print(letter.swapcase(),end="")


# In[22]:


movie="Drishyam"
for letter in movie:
   # print(letter)
    print(letter.swapcase(),end="       ")


# In[23]:


movie="Drishyam"
for letter in movie:
   # print(letter)
    print(letter.swapcase(),end="*")


# In[25]:


for i in range(1, 11):
    if i % 2 == 0:
        print("Even number:",i)
    else:
            print("odd number:",i)


# In[27]:


print("even number=")
for i in range(1,11):
    if i%2==0:
        print(i, end=" ")
        
print("odd number=")
for i in range(1,11):
    if i%2!=0:
        print(i, end=" ")        


# In[28]:


len("my name")


# In[30]:


l1=[1.2,1.3]
type(l1)


# In[ ]:




