#!/usr/bin/env python
# coding: utf-8

# In[264]:


import tkinter as tk
from tkinter import *


# In[265]:


HEIGHT = 700
WIDTH = 800


# In[266]:


root = tk.Tk()


# In[267]:


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# In[268]:


frame = tk.Frame(root, bg='red', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


# In[ ]:





# In[269]:


lower_frame = tk.Frame(root, bg='red', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


# In[270]:


label = tk.Label(lower_frame, bg='white')
label.place(relwidth=0.5, relheight=0.65, relx=0.25, rely=0.1)


# In[271]:


button = tk.Button(lower_frame, text="Start!", bg='white', fg='black')
button.place(relx=0.35, rely=0.8, relheight=.2, relwidth=0.3)


# In[250]:


root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




