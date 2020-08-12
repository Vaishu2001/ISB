
'''---Automatic Wifi connector bot------
Here we will work with the networks which are being saved in our system
Steps to follow:
1)Check for the saved networks
2)Check for the available networks
3)Ask the user which saved network wants to login
4)Disconnect the currrently connected network
5)If the preferred network is not saved then end the program
6)If preferred network is in saved then check whether they are available or not
7)If it is avaiable,then connect.''''





import os
import sys


#step 1
saved_profiles=os.popen('netsh wlan show profiles').read()
print(saved_profiles)
#step 2
available_profiles=os.popen('netsh wlan show networks').read()
print(available_profiles)
#step 3
preferred_ssid=input('Enter the preferred wifi for your connection:')
#step 4
response=os.popen('netsh wlan disconnect').read()#to disconnect the currently connected network
print(response)
#step 5
if preferred_ssid not in saved_profiles:
	print("profile for"+preferred_ssid+"is not saved in your system")
	print("sorry but cant establish the connection")
	#Now we need to end the program once the prefered network is not found after that no other code written after this will not be executed
	sys.exit()
else:
	print("profile for"+preferred_ssid+"is  saved in your system")
#step 6
#The while loops will break only if preferred network is found in available network and then it prepares for connecting 
#Else while loop keep on executing infinite times till it breaks and wont come out of execution
while True:
	avail=os.popen('netsh wlan show networks').read()
	if preferred_ssid in avail:
		print("Found")
		break
#step 7
print("--------connecting--------")#connecting the preferred network
resp=os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
print(resp)
