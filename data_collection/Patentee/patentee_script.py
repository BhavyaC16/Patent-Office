import csv
import pandas as pd
import random

data_institute = pd.read_csv("export.csv")
data_companies = pd.read_csv("companies.csv")
data_individuals = pd.read_csv("Individuals.csv")

patentees_id=[]
patentees_Name=[]
patentees_Category=[]


for i in data_individuals["Individuals"]:
	patentees_Name.append(i)
	patentees_Category.append("Individuals")


for i in data_companies["Company"]:
	patentees_Name.append(i)
	patentees_Category.append("Company")

for i in data_institute["Institution"]:
	patentees_Name.append(i)
	patentees_Category.append("Institute")




count=0
i=100000
while(count<500):

	patentees_id.append(i)
	count=count+1
	val=random.randint(1,9)
	i=i+val

output = pd.DataFrame({'Patentee_ID':patentees_id , 'Patentee_Name':patentees_Name,'Patentee_Category':patentees_Category })
output.to_csv('Patentees.csv', index = False)
