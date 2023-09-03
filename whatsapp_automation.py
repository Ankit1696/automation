#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[6]:


import pywhatkit 
import pyautogui
import time
"""
ENTER THE PHONE NO. WITH COUNTRY CODE
VIZ +91 FOR INDIA
"""
def automate_whatapp_msg(phone_no, no_of_reapetitions):
    pywhatkit.sendwhatmsg_instantly(phone_no,"This is first message")
    time.sleep(5)
    for i in range(no_of_reapetitions):
        msg = "This is an example of automation "+str(i+1)+"test"
        pyautogui.typewrite(msg)
        pyautogui.press("enter")


# In[ ]:





# In[7]:





# In[ ]:




