''' Automatic login in Facebook
steps to follow:
We’ll need to install a couple of things:
1)Selenium, which allows you to control browsers from Python
2)ChromeDriver, which allows software to control Chrome (like Selenium!)
1)Open the browser
2)provide facebook link
3)Store the email and password in user_id and password variables
4)Finding  the email id in the source code and passing my user_id as a parameter #source code is entire code in which a webpage is written
5)Finding the password id in the source code and passing my password as a parameter
6)Finding the login id in the souce code 
7)clicking the login button'''


from selenium import webdriver
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")
browser.get("https://www.facebook.com")
user_id="abcd@gmail.com"
password="123456"
'''
print(user_id)
print(password)'''
ep=browser.find_element_by_id("email")
ep.send_keys(user_id)
pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()
