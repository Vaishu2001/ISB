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