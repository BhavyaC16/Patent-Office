import csv
import random

file = open("Patent_Offices.csv","w")
write = csv.writer(file)
write.writerow(["Office_ID","Office_Location","Office_Postal_Address","Office_Website","Office_Contact"])
write.writerow(["1","Delhi","Intellectual Property Office Building, Plot No. 32, Sector 14, Dwarka, New Delhi-110078","http://www.ipindia.nic.in","delhi-patent@nic.in"])
write.writerow(["2","Mumbai","Boudhik Sampada Bhawan, Antop Hill, S. M. Road, Mumbai - 400 037.","http://www.ipindia.nic.in","mumbai-patent@nic.in"])
write.writerow(["3","Chennai","Patent Office Intellectual Property Building G.S.T. Road, Guindy, Chennai-600032","http://www.ipindia.nic.in","chennai-patent@nic.in"])
write.writerow(["4","Kolkata","Intellectual Property Office Building, CP-2 Sector V, Salt Lake City,Kolkata-700091","http://www.ipindia.nic.in","kolkata-patent@nic.in"])

