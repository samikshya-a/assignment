#!/usr/bin/env python
# coding: utf-8

# Q1.

# The two values of Boolean data type are True and False . The value returns as , True = 1 and False = 0 . To define a boolean we have to assign True or False to a variable or an expression which will evaluate a value . We can check the type of variable by a built in function .

# In[1]:


1 == 1


# In[3]:


1<0


# Q2.

# The three different types of boolean operators are and , or and not . 

# Q3.

# truth table of and                   truth table of or                truth table of not
# x    and    y    return              x    or    y    returns          not x    returns   
# True       True   True               True       True    True             True    False
# True       False  False              True       False   True             False   True
# False      True   False              False      True    True
# False      False  False              False      False   False

# Q4.

# In[1]:


(5>4) and (3==5)


# In[2]:


not (5>4)


# In[3]:


(5>4) or (3==5)


# In[4]:


not ((5>4) or (3==5))


# In[6]:


(True and True) and (True == False)


# In[7]:


(not False) or (not True)


# Q5.

# The six comparison operators are less than(<) , greater than(>) , less than or equal(<=) , greater than operator(>=) , equal to(==) , not equal(!=) . 

# Q6.

# The difference between equal to and assignment operator is , the equal to operator checks if the given operands are equal or not whereas the assignment operator is used to assign value to variable .

# In[4]:


a = 1
b = 4
a == b


# Q7.

# In[5]:


spam = 0
if spam == 10:
    print('eggs')      #block 1
    if spam > 5:
        print('bacon') #block 2
    else:
        print('ham')   #block 3
        print('spam')
        print('spam')
        


# Q8.

# In[3]:


spam = int(input("enter a number: "))
if spam == 1:
    ptint("hello")
else:
    if spam == 2:
        ptint("howdy")
    else:
        print("greetings!")


# Q9.

# If programme stuck in an endless loop , we will press the ctrl+c key .

# Q10.

# Break terminates the current loop and passes control to the next loop and continue skips the current iteration and execcutes the next one in the loop .

# Q11.

# In a for loop , range(10) refers to call ranges from 0 upto 10(excluded) , range(0,10) refers the loop to starts at 0 and goes upto 10(excluded) , range(0,10,1) refers the loop stars at 0 , increase the variable by 1 on each iteration and goes upto 10 .

# Q12.

# In[8]:


for i in range(1,11):
    print(i)


# In[10]:


a = 1
while a < 11:
    print(a)
    a = a+1


# Q13.

# spam.bacon()
