import csv

patentees = open("Patentees.csv","r")
attorney = open("Patent_Attorney.csv","r",encoding='latin')
applicants = open("Applicants.csv","r")
examiner = open("Patent_Examiner.csv","r")
login = open("Login_Credentials.csv","w")

writer = csv.writer(login)
writer.writerow(["Username","Password","Role"])

read = csv.reader(patentees)
rows = []
flag=1
for i in read:
	if flag:
		flag=0
		continue
	rows.append(i)
for i in rows:
	writer.writerow([i[0],i[1],"Patentee"])

read1 = csv.reader(attorney)
rows = []
flag=1
for i in read1:
	if flag:
		flag=0
		continue
	rows.append(i)
for i in rows:
	writer.writerow([i[0],i[1],"Patent_Attorney"])

read2 = csv.reader(applicants)
rows = []
flag=1
for i in read2:
	if flag:
		flag=0
		continue
	rows.append(i)
for i in rows:
	writer.writerow([i[1],i[2],"Applicant"])

read3 = csv.reader(examiner)
rows = []
flag=1
for i in read3:
	if flag:
		flag=0
		continue
	rows.append(i)
for i in rows:
	writer.writerow([i[0],i[1],"Patent_Examiner"])
