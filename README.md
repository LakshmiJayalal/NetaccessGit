# Requirements 
1. Selenium
2. Python (seperate environment if possible)

# OS - Windows
# How to:

1. Edit the batch file automation.bat
2. Add your LDAP Username and LDAP Password in the py code. <span style="color:red">.(keep in a secure location as anyone having access to this file can see your username and password)</span>
3. Open the taskScheduler.
  ![alt text](taskStarup.png "Task Scheduler")
4. Click on create task and fill in the details.
  ![alt text](CreateTask.png)
5. Goto Actions, create a new one. In the script portion add loction to your bat (batch file).
  ![alt text](actions.png)
9. Goto triggesrs - set time whenever you want to run the netaccess script. 
10. Save.

<span style="color:red">Caution: Always try to run it once attended before leaving it unattended to ensure seemless access</span>

## Happy networking! 
