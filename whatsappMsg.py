# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:28:47 2019

@author: Youssef Kishk

Whatsapp automated messages sending system
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#connect to whatsapp web driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

#Determing user name, message and nymber of times to send that message
user_name = input('Enter user name: ')
message = input('Enter message: ')
number_of_times = int(input('Enter count: '))

#pause for 15 seconds to scan QR code and get into your whatsapp web
print('Scan your whatsapp QR code and wait\n')
time.sleep(15)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name))
user.click()

#have an access to message box by its class name 
message_box = driver.find_element_by_class_name('_3u328')

print('Sending\n')
#looop for number of times its required to send the message
for i in range(number_of_times):

   #write the message to the box
   message_box.send_keys(message)
   #Access the send button by its class name 
   button = driver.find_element_by_class_name('_3M-N-')
   button.click()

print('Done')