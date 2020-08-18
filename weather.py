#import libraries
from selenium import webdriver
#opening google
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")
#Taking inputs
month='august'#input("Enter any month in lower case :")
year='2020'#input("Enter  year :")
#https://www.accuweather.com/en/in/mangalore/188760/august-weather/188760?year=2020&view=list
url='https://www.accuweather.com/en/in/mangalore/188760/'+month+'-weather/188760?year='+year+'&view=list'
browser.get(url)
#Getting high temparature list
high=browser.find_elements_by_class_name('high')
#create a list to store the temparatures in integer form
high_list=[]
for i in high:
	j=i.get_attribute('textContent')
	high_list.append(int(j[:2]))
#print(high_list)

	
#Getting low temparature list
low=browser.find_elements_by_class_name('low')
#create a list to store the temparatures in integer form
low_list=[]
for i in low:
	j=i.get_attribute('textContent')
	low_list.append(int(j[3:5]))
#print(low_list)
#Get precipitation data
pr=browser.find_elements_by_xpath('//div[@class="info precip"]/p[2]')
pre_list=[]
for i in pr:
	j=i.get_attribute('textContent')
	pre_list.append(float(j[:2]))
#print(pre_list)
#create a date list 
date=[]
for i in range(len(pre_list)):
	d=i+1
	date.append(d)
#print(date)
#create a dictionary
dic={'Date':date,'High temparature':high_list,'Low temparature':low_list,'Precipitation':pre_list}
print(dic)
#create a dataframe
import pandas as pd 
df=pd.DataFrame(dic)
print(df)
#Creating a csv file to store the dataframe
df.to_csv("C:\\Users\\ASUS\\mangalore"+month+".csv",index=False)
print("Done!!!")