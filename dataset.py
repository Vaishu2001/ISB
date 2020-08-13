#importing the libraries
from selenium import webdriver
import pandas as pd 
import time
import os
#step 1
browser=webdriver.Chrome("C:\\Users\\ASUS\\Desktop\\chromedriver.exe")
#step 2
browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(15)
#creating a dataframe
df=pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Deaths','New Deaths','Recovered','Active Cases','Critical'])
#step 3 and step 4
for i in browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'):
#i is representing each row
#we are interested in tbody and we are moving to each of the row
    td_list=i.find_elements_by_tag_name("td")
    # creating an empty list
    row=[]
    for td in td_list:
    	row.append(td.text) # create a row having each countries
    	#create a new dictionary
    data={}

    for j in range(len(df.columns)):
        data[df.columns[j]] = row[j] 
    df = df.append(data, ignore_index=True)
df=df[1:]
#print(df)
#step 5
path="C:\\Users\\ASUS"
path1=os.path.join(path,'Covid.csv')#This func helps us to join path with our file name
df.to_csv(path1,index=False)#to convert dataframe into csv file
print("The data has been stored at"+path1+".")
#step 6
browser.quit()