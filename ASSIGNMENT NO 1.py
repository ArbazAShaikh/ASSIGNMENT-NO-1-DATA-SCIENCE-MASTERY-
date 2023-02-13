#!/usr/bin/env python
# coding: utf-8

# # Assignment No 1[29th jan]

# # 1. Who develop python programming language?
# ### Ans.Python was developd by Guido Van Rossume.

# # 2.Which type of programming does python support?
# ### Ans.Python is multi-paradigm programming language which support object oriented programming(OOP), Imperative programming, procedural programming and scripting.

# # 3.Is  case sensitive when dealing with identifiers?
# ### Ans.Yes,Python is case sensitive when dealing with identifiers,which includes varible names,function names,class names,and others.

# # 4.What is the correct extension of the python file?
# ### Ans.The correct extension for a python file is ".py"

# # 5.Is python code compiled or interpreted?
# ### Ans. Python is an interpreted language ,not a compiled language. It means that the code is executed line by line, rather than being compiled into machine code and executed directly
# 

# ## 6.Name a few blocks of code used to define in python language
# Ans.

# In[2]:


num1=int(input("Enter the frist number:"))
num2=int(input("Enter the second number:"))
op=str(input("Enter the operator:"))

if op=='+':
    print("Addition is:",num1+num2)
elif op=='*':
    print("Multiplication is:",num1*num2)
elif op=='/':
    print("Division is:",num1/num2)
else:
    print("Subtraction is:",num1-num2)
         
    


# # 7.State a character used to give single-line comments in python?
# ### Ans.'#' is the character used in python to give a single line command. This is used to indicate comments in the code , and interpreter will ignore everything following the "#" on that line.

# In[1]:


# This is simple python program
print("Hello Pwskills")


# # 8.Mention function which can help us to find the version of python that we are currently working on?
# ### Ans. You can use the 'sys' module in python to determine the version of python that you are currently working with. Specifically you can use the 'sys.version' and 'sys.version_info' attributes to get information about the version of python.

# In[2]:


# Example
import sys
print("Version of Pyhton")
print(sys.version)
print(sys.version_info)


# # 9.Python support the creation of anonymous functions at runtime,using a construct called_____
# ### Ans. Python support the creation of anonymous functions at runtime, using a construct called 'lambda'. A lambda fuction is small anonymous function that can take any number of arguments,but can only have one expression. The expression is executed and returned when the function is called.
# 

# In[3]:


#Example
mult=lambda x,y:x*y
print(mult(12,19))


# # 10.What does pip stand for python?
# ### Ans.'pip' is an acronym for "Pip install packages".It is a package manager for python, which allows you to easily install and manage packages for use in your python projects.

# ## 11.Mension a few built-in function in python?
# ### Ans.There are many built-in functions in Python, here are a few examples:
# 
# ### print(): This function is used to display output on the console.
# 
# ### len(): This function is used to return the length of an object. For example, len("Hello World") returns 11.
# 
# ### int(), float(), str(): These functions are used to convert data types. For example, int("123") returns 123, float("3.14") returns 3.14, and str(123) returns "123".
# 
# ### min(), max(): These functions are used to return the minimum and maximum values from a list or tuple. For example, min([1, 2, 3]) returns 1 and max([1, 2, 3]) returns 3.

# # 12.What is the maximum possible length of an identifier in python?
# ### Ans.There is no specific maximum length for an identifier in Python, but there are some naming conventions that you should follow when defining an identifier. According to PEP 8, the style guide for Python code, the maximum length of an identifier should be 79 characters. Additionally, it is recommended to use descriptive, lowercase names with underscores to separate words.However, it is important to note that the actual maximum length of an identifier is determined by the underlying system and its available memory, so it could potentially be much longer than 79 characters.

# # 13.What are the benefits of using python?
# ### Ans.There are many benefits to using Python as a programming language, some of the key benefits are:
# 
# ### Easy to learn and use: Python has a simple and straightforward syntax, which makes it easy to learn and use, even for those who have no prior programming experience.
# 
# ### Versatile: Python is a general-purpose language, which means it can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more.
# 
# ### Large community and rich ecosystem: Python has a large and active community of developers, which provides a wealth of resources and support. It also has a rich ecosystem of libraries and frameworks, making it easy to find solutions to common problems and get up and running quickly with new projects.
# 
# ### High-level language: Python is a high-level language, which means it abstracts away many of the underlying details of the hardware and operating system, making it easier to focus on the problem you're trying to solve.
# 
# ### Dynamic typing: In Python, you don't have to declare the data type of a variable, which makes it easier to write and maintain code, as well as providing more flexibility in how you use your data.
# 
# ### Interpreted: Python is an interpreted language, which means you don't have to compile your code before you can run it. This makes the development process faster and more iterative.
# 
# ### Cross-platform: Python code can run on any platform that has a Python interpreter installed, making it a great choice for cross-platform development.
# 
# ### These are just some of the benefits of using Python, and there are many more that make it a great choice for a wide range of applications and use cases.
# 
# 
# 
# 

# # 14.How is memory managed in python?
# ### Ans.In Python, memory management is done automatically and efficiently by the Python memory manager, which is part of the Python interpreter. The memory manager is responsible for allocating and freeing memory for objects as needed, and for keeping track of which objects are in use and which are not.
# 
# ### The memory manager uses a combination of techniques to manage memory, including reference counting and garbage collection.
# 
# ### Reference counting is a technique that keeps track of the number of references to an object in memory. When the reference count of an object reaches zero, it means that the object is no longer being used, and the memory manager can safely free it.
# 
# ### Garbage collection is another technique used by the memory manager to reclaim memory that is no longer in use. The garbage collector periodically scans the memory and identifies objects that are no longer accessible, and then frees their memory.
# 
# ### Together, these techniques provide an efficient and effective way to manage memory in Python, allowing you to focus on writing code, without having to worry about memory management. However, it is important to keep in mind that the memory manager can only free memory that is no longer being used, so if you have objects that are still in use, but not needed, they will not be freed, and will continue to consume memory.
# 
# 
# 
# 
# 

# ## 15.How to install python on windows and set path varibles?
# ### Ans.Here are the steps to install Python on Windows and set the PATH environment variable:
# 
# ### 1.Download the latest version of Python from the official website: https://www.python.org/downloads/
# 
# ### 2.Run the Python installer and follow the on-screen instructions to install Python. During the installation process, make sure to select the option to add Python to the PATH environment variable.
# 
# ### 3.After the installation is complete, open the Start menu and search for "Environment Variables". Click on "Edit the system environment variables".
# 
# ### 4.In the System Properties window, click on the "Environment Variables" button.
# 
# ### 5.Under "System Variables", scroll down and find the "Path" variable, then click on "Edit".
# 
# ### 6.In the Edit environment variable window, click on "New" and add the path to the Python executable, which is usually C:\PythonXX\, where XX is the version number of Python you installed.
# 
# ### 7.Click "OK" to close all windows and save the changes.
# 
# ### 8.Open a new Command Prompt window and type python to verify that the Python installation and PATH variable are working correctly. You should see the Python interactive shell, which means Python is installed and ready to use.
# 
# ### That's it! You've successfully installed Python on Windows and set the PATH environment variable. You can now start using Python and write your first program.
# 
# 
# 
# 
# 

# ## 16.Is indentation required in python?
# ### Ans.Yes, indentation is required in Python. Indentation is used to define blocks of code, such as loops and functions, and is an important part of the syntax in Python. Unlike many other programming languages, Python uses indentation to indicate the structure of the code, rather than using curly braces or other punctuation marks.
# 

# In[4]:


for i in range(0,10):
    print(i)


# In[6]:


for i in range(0,10):
print(i) 

