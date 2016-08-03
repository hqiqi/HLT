import os
import sqlite3
import numpy as np
import talib as ta
from talib import EMA

conn = sqlite3.connect('db.sqlite3')

def scrub(table_name):
	 return '',join(chr for chr in table_name if chr.isalmum())

M1 = {}
M5 = {}
M15 = {}
M30 = {}
H1 = {}

MapTable = {"prices_price_m1": M1, "prices_price_m5": M5, "prices_price_m15": M15, "prices_price_m30": M30, "prices_price_H1": H1}

c = conn.cursor()

for table in MapTable:

	c.execute("SELECT * FROM {}".format(table))

	a = c.fetchall()
	for index, value in enumerate(a[0]):
		MapTable[table][value] = [temp[index] for temp in a[-200:]]

conn.close()

dash_data = {}
All_TF = {"M1": M1, "M5": M5, "M15": M15, "M30": M30, "H1": H1}
db_TF = ["M1", "M5", "M15", "M30", "H1"]
kUSD = ['EUR_USD', 'GBP_USD', 'AUD_USD', 'USD_JPY', 'NZD_USD', 'USD_CAD', 'USD_CHF']
kEUR = ['EUR_USD', 'EUR_GBP', 'EUR_CHF', 'EUR_JPY', 'EUR_CAD', 'EUR_AUD', 'EUR_NZD']
kGBP = ['GBP_USD', 'EUR_GBP', 'GBP_CHF', 'GBP_AUD', 'GBP_JPY', 'GBP_CAD', 'GBP_NZD']
kJPY = ['USD_JPY', 'EUR_JPY', 'CHF_JPY', 'AUD_JPY', 'GBP_JPY', 'CAD_JPY', 'NZD_JPY']
kNZD = ['NZD_USD', 'EUR_NZD', 'NZD_CHF', 'AUD_NZD', 'NZD_JPY', 'GBP_NZD', 'NZD_CAD']
kAUD = ['AUD_USD', 'EUR_AUD', 'AUD_CHF', 'AUD_JPY', 'AUD_CAD', 'AUD_NZD', 'GBP_AUD']
kCHF = ['USD_CHF', 'EUR_CHF', 'CHF_JPY', 'GBP_CHF', 'CAD_CHF', 'AUD_CHF', 'NZD_CHF']
kCAD = ['USD_CAD', 'EUR_CAD', 'CAD_CHF', 'AUD_CAD', 'CAD_JPY', 'GBP_CAD', 'NZD_CAD']
kKeys = [kUSD, kEUR, kGBP, kJPY, kNZD, kAUD, kCHF, kCAD]
pos = ("USD", "EUR", "GBP", "JPY", "NZD", "AUD", "CHF", "CAD")
madTable = ("indicators_usd_maddash","indicators_eur_maddash","indicators_gbp_maddash", "indicators_jpy_maddash", 
			"indicators_nzd_maddash","indicators_aud_maddash","indicators_chf_maddash","indicators_cad_maddash")
currencies = ['EUR_USD', 'GBP_USD', 'AUD_USD','USD_JPY', 'NZD_USD', 'USD_CAD', 'USD_CHF','EUR_GBP', 'EUR_CHF', 'EUR_JPY', 'EUR_CAD', 'EUR_AUD', 'EUR_NZD', 'CHF_JPY', 
		  	  'GBP_CHF', 'CAD_CHF', 'AUD_CHF', 'NZD_CHF', 'AUD_JPY', 'AUD_CAD', 'AUD_NZD', 'GBP_AUD', 'GBP_JPY', 'CAD_JPY', 'NZD_JPY', 'GBP_CAD', 'GBP_NZD', 'NZD_CAD']

for tf in All_TF:
	dash_data[tf] = {}
	print '-' * 20
	print tf
	print '-' * 20

	for ccy in currencies: 
		temp = [float(i) for i in All_TF[tf][ccy][:]]
		mad = float(M1[ccy][-1]) - ta.EMA(np.array(temp), timeperiod=37)
		dash_data[tf].update({ccy:mad[-1]})
		print ccy, mad[-1]
	
conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

for index, prikey in enumerate(kKeys):

	c.execute("DELETE FROM {}".format(madTable[index]))

	for key in prikey: 
		
		if key[-3:] == pos[index]:
			sgn = -1
		else:
			sgn = 1

		if "JPY" in key:
			pip = 100
		else:
			pip = 10000

		queryinput = (key,)

		for tf in db_TF:
			queryinput += (round(pip * sgn * dash_data[tf][key]),)

		c.execute("INSERT INTO {} VALUES (null,?,?,?,?,?,?)".format(madTable[index]), queryinput) #Edit here

	conn.commit()
conn.close()
print "Done"