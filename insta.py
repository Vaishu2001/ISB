''''-----Instagram profile Pic downloader-----
Here we can download the profile pic of Instagram user's using python
Steps to follow:
1)Open the google
2)Go to instagram 
3)Take the user id of the profile as input
4)Go to profile
5)Download the profile picture ''''







#importing the required libraries
from selenium import webdriver
#step 1
#open the google
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")
#step 2
#Here we are not doing step 2 instead directly jump into profile page url to simplify our task
user_i=input("Enter user_id of the profile:")
#common url for all the user ids
url="https://www.instagram.com/"
user_id=url+user_i
#open the profile
browser.get(user_id)
#find the profile pic in the source code
#For public account and account which you do follow
try:
    image=browser.find_element_by_xpath('//img[@class="_6q-tv"]')
#For private accounts
except:
    image=browser.find_element_by_xpath('//img[@class="be6sR"]')
#print("done")
#To retrieve the link of the image
image_link=image.get_attribute("src")
path="C:\\Users\\ASUS\\Downloads\\"+user_i+".jpg"
import urllib.request
urllib.request.urlretrieve(image_link,path)
print("The profile pic has been downloaded at"+path)
