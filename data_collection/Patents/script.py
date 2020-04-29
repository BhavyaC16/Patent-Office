import csv
import pandas as pd
import random
import requests
from bs4 import BeautifulSoup

#---------------------------------------------------------------------------------

url = 'https://www.aresearchguide.com/40-sport-research-paper-topics.html'
page= requests.get(url)

soup =  BeautifulSoup(page.text,'html.parser')
#print(soup)
#----------------------------------------------------
Title=[]
inventors=[]
subject = []

#-----------------------------------------------------

test=soup.ol
containers=test.findAll("li")
for i in containers:
	Title.append(i.a.text)
	subject.append("Sports")


url= 'https://afajof.org/most-cited-articles/'
page=requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

containers= soup.findAll("div",{"class":"article-result-container"})



for i in containers:
	Title.append(i.p.a.text)
	x=i.findAll("p",{"style":"margin-bottom:1em;"})
	inventors.append(x[1].text)
	subject.append("Finance")





url= 'https://www.nature.com/collections/lbnlhhghdx/'
page=requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')


containers=soup.findAll("div",{"class":"c-article-item__text"})

inventor=soup.findAll("ul",{"class":"c-article-item__authors"})

for i in containers:
	Title.append(i.a.text.strip())
	subject.append("Physics")


for i in inventor:

	inventors.append(i.span.text.replace(",",""))




print(len(inventors))
#-------------------------------------------------------------------------------------------------------------------



data_patentees = pd.read_csv("Patentees.csv")

file_data = pd.read_csv("file.csv")
Lang_data = pd.read_csv("Lang.csv")
Valid_data = pd.read_csv("mock.csv")




#print(subject)

patents_id=[]
patents_Name=[]
pee_id= []
patents_Category=[]
Expense=[]
Language= []
Names=[]
Final_title=[]
Final_subject = []
Final_inventors= []

for i in Title:
	Final_title.append(i)



for i in file_data["Title"]:
	Final_title.append(i)

for i in  file_data['Subject']:
	Final_subject.append(i)

for i in subject:
	Final_subject.append(i)

inventors=inventors[:40]+inventors
for i in inventors:
	Final_inventors.append(i)

for i in file_data["Inventors"]:
	Final_inventors.append(i)

print(len(Final_subject),len(Final_title),len(Final_inventors))




count=0
i=171203
while(count<len(Final_title)):

	patents_id.append(i)
	count=count+1
	val=random.randint(1,9)
	Exp=random.randint(1000,1000000)
	Expense.append(Exp)
	i=i+val


for i in range(len(patents_id)):
	random_num = random.choice(data_patentees.Patentee_ID) 
	pee_id.append(random_num)



#print(len(set(patents_id)),len(pee_id),len(Final_title),len(Final_subject),len(Final_inventors))
output = pd.DataFrame({'Patent_ID':patents_id,'Patentee_ID':pee_id ,'Title':Final_title ,'Subject':Final_subject,'Inventor':Final_inventors,'Expense in US$':Expense,
  'Opposition_Filled_Status':Lang_data.Opp,
  'Filling_Language':Lang_data.Language,'Validation_States':Valid_data.Validation})
output.to_csv('patents.csv', index = False)
