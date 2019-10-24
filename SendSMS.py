#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from twilio.rest import Client

account_sid = 'ACd3a2269fc8273b97257beb98a3af9a37'
auth_token = '52651022e8829241b217ee40506ae159'

client = Client(account_sid,auth_token)

body_of_message = 'Happy Birthday Neli: Enjoy your day. Stay Blessed'

message = client.messages.create(to = '+27814970489',from_='+12056274678',body = body_of_message)

print(message.sid)

