from bs4 import BeautifulSoup
from urllib.request import urlopen
#To get the page source of url
pg=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')
#passing page source to BeautifulSoup
soup=BeautifulSoup(pg,'html.parser')
body=soup.find('div',{'class':'ciPhotoContainer'})
#to find all h3 elements
head_list=soup.findAll('h3')
#To get all headings
name=[]
for i in head_list:
	j=i.text
	name.append(j)
#print(name)


#creating a dataframe
import pandas as pd 
columns=['pos','team','matches','points','rating']
df=pd.DataFrame(columns=columns)
#print(df)
#appending td elements to dataframe
tr_list=soup.findAll('tr')
#intialize the counter
n=0

for i in tr_list:
	row=[]
	td_list=i.findAll('td')
	for j in td_list:
		a=j.text
		row.append(a)
		dic={}
	try:
		for k in range(len(df.columns)):
			dic[df.columns[k]] = row[k]
		df = df.append(dic, ignore_index=True)
	except:
		df=pd.DataFrame(columns= columns)
		table_name=name[n]
		n=n+1
	df.to_csv('C:\\Users\\ASUS\\Cricinfo'+table_name+'.csv', index = False)


print("Done")

