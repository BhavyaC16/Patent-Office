import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import datetime


sub={"Application_ID":[],"Status":[]}
for i in range(1,450):
	sub["Application_ID"].append(249800+i)
for i in range(1,250):
	sub["Status"].append("Approved")
for i in range(250,350):
	sub["Status"].append("Pending")
for i in range(350,450):
	sub["Status"].append("Rejected")

data=pd.DataFrame(sub)
data.to_csv("Patent_Applications.csv",index=False)
