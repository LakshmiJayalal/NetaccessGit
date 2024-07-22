#!/usr/bin/env python3

'''
Author: LakshmiJayalal
'''

#Change this
rollNo = 'LDAPUserNAme' #Update your LDAP USERNAME
pwd = 'LDAPPass'    #UpdateYourLDAP Password

import time
import selenium
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
# chrome_options.add_argument("--headless") #Add this to hide the process
driver = selenium.webdriver.Chrome(options=chrome_options)

driver.get('https://netaccess.iitm.ac.in/account/login')

rollNo_box = driver.find_element(By.ID, "username")
rollNo_box.send_keys(rollNo)

pwd_box = driver.find_element(By.ID, "password")
pwd_box.send_keys(pwd)
time.sleep(1)
login_button = driver.find_element(By.ID, 'submit').send_keys("\n")
driver.get("https://netaccess.iitm.ac.in/account/approve")
time.sleep(1)
oneDay = driver.find_element(By.ID, "radios-2")
oneDay.click()
time.sleep(1)
approve_button = driver.find_element(By.ID, 'approveBtn')
approve_button.click()
time.sleep(5)
#print("Successfully authenticated")
