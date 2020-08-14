#step 1
from selenium import webdriver
import time
from bs4 import BeautifulSoup
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")
browser.get("https://www.facebook.com")
user_id="9188496929"
password="facebookchakke"
'''
print(user_id)
print(password)'''
ep=browser.find_element_by_id("email")
ep.send_keys(user_id)
pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()
time.sleep(30)
#step 2
pro=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
pro.click()
time.sleep(4)
#step 3
fr=browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
fr.click()
# Scroll the page to fetch the friend list
while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')#Come back to first page
	time.sleep(0.1)
	try:
		exit_control=browser.find_element_by_xpath("//*[contains(text(),'More About You')]")
		break
	except:
		continue
#Finding the page source to parse the html document
#step 5
ps=browser.page_source#return html file of page which our browser is currently  holding
soup=BeautifulSoup(ps,'html.parser')#html.parser helps us to parse the source code
flist=soup.find('div',{'class':'_3i9'})
friends=[]
for i in flist.findAll('a'):
	friends.append(i.text)
#print(friend)
#step 6
names_list=[]
for name in friends:
	if(name=="FriendFriends"):
		continue
	if('friends' in name):
		continue
	if(name==''):
		continue
	else:
		names_list.append(name)
print(names_list)
#step 7
browser.quit()