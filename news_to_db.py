import requests
import json
import sqlite3
#_token = 'B426CCEC7B06438CB5DE18579206A6EA'
domain = 'www.xignite.com/xCalendar.json/GetEventsForWeek?'
data_date = '2016-08-01'


s = requests.Session()
url = "https://" + domain
          

params = {'ForDate' : data_date, '_Token' : 'B426CCEC7B06438CB5DE18579206A6EA'}               
req = requests.Request('GET', url, params = params)
pre = req.prepare()
resp = s.send(pre, stream = True, verify = False)

#unicode
x = resp.text
#dict
r = json.loads(x)
#list of ec
y = r["Summaries"]
#one ec (dic)
#ec1 = y[1]
#another ec (dic)
#ec2 = y[2]
#values
#ec1Value = ec1["Values"]

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

for ec in y:
	l = ec["Values"]
	 #l is a list(len can be 0 to 4)
	if len(l) == 1:
	 	Consensus = l[0]["Consensus"]
	 	if l[0]["Actual"] !="":
	 		Actual = l[0]["Actual"]

	if len(l) == 2:
	 	if l[0]["Consensus"] == "":
	 		Consensus = l[1]["Consensus"]
	 		if l[1]["Actual"] !="":
	 			Actual = l[1]["Actual"] 
	 	else:
	 		Consensus = l[0]["Consensus"]
	 		if l[0]["Actual"] !="":	
	 			Actual = l[0]["Actual"] 

	if len(l) == 3:
	 	if l[0]["Consensus"] =="":
	 		if l[1]["Consensus"] == "":
	 			Consensus = l[2]["Consensus"]
	 			if l[2]["Actual"] !="":	
	 				Actual = l[2]["Actual"] 
	 		else:
	 			Consensus = l[1]["Consensus"]
	 			if l[1]["Actual"] !="":	
	 				Actual = l[1]["Actual"]
	 	else:
	 		Consensus = l[0]["Consensus"]
	 		if l[0]["Actual"] !="":	
	 			Actual = l[0]["Actual"] 		 	

	if len(l) == 4:
	 	if l[0]["Consensus"] =="":
	 		if l[1]["Consensus"] == "":
	 			if l[2]["Consensus"]=="":
	 				Consensus = l[3]["Consensus"]
	 				if l[3]["Actual"] !="":	
	 					Actual = l[3]["Actual"] 		 	
	 			else:
	 				Consensus = l[2]["Consensus"]
	 				if l[2]["Actual"] !="":	
	 					Actual = l[2]["Actual"] 		 	
			else:
				Consensus = l[1]["Consensus"]
				if l[1]["Actual"] !="":	
	 				Actual = l[1]["Actual"] 		 	
		else:
			Consensus = l[0]["Consensus"]
			if l[0]["Actual"] !="":	
	 			Actual = l[0]["Actual"]

	if len(l) > 4:
			Consensus = l[0]["Consensus"]
			if l[0]["Actual"] !="":	
	 			Actual = l[0]["Actual"]			 	


	rows = (str(ec["EventID"]),str(ec["Delay"]),str(ec["EventCode"]),str(ec["CountryCode"]),str(ec["ReleasedOn"]),str(ec["EventName"]),str(ec["Values"]),Consensus,Actual,str(ec["Message"]),str(ec["Outcome"]),str(ec["Identity"]))
	c.execute('INSERT INTO EconomicCalendar_economicreleases VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?)', rows)

conn.commit()
conn.close()


