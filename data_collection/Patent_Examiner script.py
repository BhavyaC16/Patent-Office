import pandas as pd
import requests
from bs4 import BeautifulSoup
t=0
char=1
lis=[]
while t<200:
	page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anA'+str(char)+'.htm')
	while page.status_code!=200:
		char=char+1
		page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anA'+str(char)+'.htm')
	char=char+1
	soup = BeautifulSoup(page.text, 'html.parser')

	last_links = soup.find(class_='AlphaNav')
	last_links.decompose()

	artist_name_list = soup.find(class_='BodyText')
	artist_name_list_items = artist_name_list.find_all('a')

	# Use .contents to pull out the <a> tag’s children
	for artist_name in artist_name_list_items:
		names = artist_name.contents[0]
		k=0
		for i in range(len(names)):
			if names[i]==',':
				k=i
		st=names[k+2:]+' '+names[:k]
		lis.append(st)
		for i in range(len(st)):
			if (ord(st[i]) not in range(65,91)) and (ord(st[i]) not in range(97,123)) and ord(st[i])!=32:
				print(st)
				print("this-"+st[i])
				lis.remove(st)
				print("removed...................................................")
				t=t-1
				break

		t=t+1
		print(str(t)+" "+st)

sub={"Patent_Examiner_ID":[],"Name":[],"Salary":[]}
for i in range(len(lis)):
	sub["Patent_Examiner_ID"].append(500001+i)
	sub["Name"].append(lis[i])
	sub["Salary"].append(1625000)
data=pd.DataFrame(sub)
data.to_csv('Patent_Examiner.csv',index=False)
