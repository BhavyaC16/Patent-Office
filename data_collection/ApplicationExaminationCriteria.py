import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import datetime


sub={"Novelty_Status":[],"Inventive_Status":[],"Applicability_Status":[]}
for i in range(1,250):
	sub["Novelty_Status"].append(True)
	sub["Inventive_Status"].append(True)
	sub["Applicability_Status"].append(True)
for i in range(250,350):
	k=random.randint(0,3)
	if k==1:
		sub["Novelty_Status"].append(False)
		sub["Inventive_Status"].append(True)
		sub["Applicability_Status"].append(True)
	elif k==2:
		sub["Novelty_Status"].append(True)
		sub["Inventive_Status"].append(False)
		sub["Applicability_Status"].append(True)
	else:
		sub["Novelty_Status"].append(True)
		sub["Inventive_Status"].append(True)
		sub["Applicability_Status"].append(False)		
for i in range(350,450):
	k=random.randint(0,3)
	if k==1:
		sub["Novelty_Status"].append(False)
		sub["Inventive_Status"].append(False)
		sub["Applicability_Status"].append(True)
	elif k==2:
		sub["Novelty_Status"].append(True)
		sub["Inventive_Status"].append(False)
		sub["Applicability_Status"].append(False)
	else:
		sub["Novelty_Status"].append(False)
		sub["Inventive_Status"].append(True)
		sub["Applicability_Status"].append(False)	
data=pd.DataFrame(sub)
data.to_csv("Application_Examination_Criteria.csv",index=False)
