import csv
import random

file = open("Renewal_Applications.csv","w")
write = csv.writer(file)
write.writerow(["Renewal_Application_ID","Patent_ID","Application_Office_ID","Examiner_ID","Fees_Paid","Renewal_Status"])

expired = open("ExpiredPatents.csv","r")
read = csv.reader(expired)
rows = []
for i in read:
	rows.append(i)
for i in range(1,len(rows),2):
	row=[]
	row.append(str(312500+i//2))
	row.append(str(rows[i][0]))
	row.append(str(random.randint(1,4)))
	row.append(str(random.randint(500001,500320)))
	row.extend(["False","False"])
	write.writerow(row)




