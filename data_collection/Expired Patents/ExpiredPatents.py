import csv
import random

file = open("ExpiredPatents.csv","w")
write = csv.writer(file)
write.writerow(["Patent_ID","Date_of_Expiry","Renewal_Fees"])

patents = open("patents.csv","r")
read = csv.reader(patents)
rows = []
for row in read:
	rows.append(row)

for i in rows:
	if i[0]=="Patent_ID":
		continue
	ep_row = []
	if "Expired" in i:
		ep_row.append(i[0])
		ep_row.append(i[rows[0].index("Date_of_Expiry")])
		ep_row.append(str(random.randint(1,20)*2000))
		write.writerow(ep_row)
