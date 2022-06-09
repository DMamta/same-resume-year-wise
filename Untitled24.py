#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
ans is true and false are the two boolean values


# In[ ]:


get_ipython().set_next_input('What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
ans- and, or,not


# In[ ]:


Make a list of each Boolean operator&#truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

Ans :- True and True is True.

True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.


# In[ ]:


get_ipython().set_next_input('What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 &gt; 4) and (3 == 5)
not (5 &gt; 4)
(5 &gt; 4) or (3 == 5)
not ((5 &gt; 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[2]:


(5>4) and (3 == 5)


# In[3]:


not(5>4)


# In[4]:


(5>4) or (3 == 5)


# In[5]:


not((5>4) or (3==5))


# In[6]:


(true and true ) and (true == false)


# In[7]:


(not false) or (not true)


# In[ ]:


get_ipython().set_next_input('What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
ans :- comparison operator compares two values and returns a boolean value, either True or False . Python has six comparison operators: less than ( < ), less than or equal to ( <= ), greater than ( > ), greater than or equal to ( >= ), equal to ( == ), and not equal to ( != ).
    


# In[ ]:


How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
The “=” is an assignment operator is used to assign the value on the right to the variable on the left. The '==' operator checks whether the two given operands are equal or not. 
If so, it returns true. Otherwise it returns false


# In[ ]:


Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[9]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# In[ ]:


Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


# In[13]:


Spam = input(int)
if spam ==1:
    print("howdy")
if spam ==2:
    print("spam")
else :
    print("Greetings")


    


# In[ ]:


get_ipython().set_next_input('if your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
we can press control+C


# In[ ]:


get_ipython().set_next_input('How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
The primary difference between break and continue statement in C is that the break statement leads to an immediate exit of the innermost switch or enclosing loop. On the other hand, the continue statement begins the next iteration of the while, enclosing for, or do loop.


# In[14]:


range(10)


# In[18]:


list(range(10))


# In[16]:


range(0,10)


# In[17]:


list(range(0,10))


# In[21]:


list(range(0,10,1))


# In[ ]:


Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


# In[28]:


for i in range(1,11) :
    print(i)


# In[ ]:


i = 1 
while i <= 10: 
    print(i) 
    i += 1 


# In[ ]:


get_ipython().set_next_input('If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
ans :- bacon spam


# In[ ]:




