from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import sqlite3
import oandapy
import csv
import numpy as np
import datetime
import talib as ta
from talib import EMA
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trydjango19.settings')
app = Celery('prices')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@periodic_task(run_every=crontab(), name="Price_To_DB", ignore_result=True)
def Price_To_DB():
	UpdatePrice()

@app.task()
def MAD_To_DB():
	CalculateMaddash()



def UpdatePrice():
	LastUpdate = None
	current = int(str(datetime.datetime.now())[14:16]) 
	updated = True

	if LastUpdate is None:
		LastUpdate = current
		updated = False

	if LastUpdate is not current:
		updated = False

	while updated is False:

		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()

		oanda = oandapy.API(environment="practice", access_token="bc27a46b1615b33ede78f1de2c0dffe0-e1b6efb42854e92b5c526549993252b5")

		currencies = ['EUR_USD', 'GBP_USD', 'AUD_USD','USD_JPY', 'NZD_USD', 'USD_CAD', 'USD_CHF','EUR_GBP', 'EUR_CHF', 'EUR_JPY', 'EUR_CAD', 'EUR_AUD', 'EUR_NZD', 'CHF_JPY', 
			  		  'GBP_CHF', 'CAD_CHF', 'AUD_CHF', 'NZD_CHF', 'AUD_JPY', 'AUD_CAD', 'AUD_NZD', 'GBP_AUD', 'GBP_JPY', 'CAD_JPY', 'NZD_JPY', 'GBP_CAD', 'GBP_NZD', 'NZD_CAD']

		times = {"M1": "prices_price_m1"}			
		 
		if int(str(datetime.datetime.now())[14:16])%5 is 0:
			times["M5"] = 'prices_price_m5'
		if int(str(datetime.datetime.now())[14:16])%15 is 0:
			times["M15"] = 'prices_price_m15'
		if int(str(datetime.datetime.now())[14:16])%30 is 0:
			times["M30"] = 'prices_price_m30' 
		if int(str(datetime.datetime.now())[14:16]) is 00:			
			times["H1"] = 'prices_price_H1' 

		for time in times:

			obj = {}
			for currency in currencies:
				obj['BigDataForPrice'+str(currency)] = []

			BigDataForTimeEUR_USD =[]
			

			Date = []
			Time = []

			print "Collecting %r Data" % (time)

			for currency in currencies:

				print "Collecting %r Data" % (currency)

				res = oanda.get_history(instrument=currency, granularity=time, count="1") # currencies
				ccy = res.get("instrument")
				prices = res.get('candles')

				t = []
				d = []
				prices_time = []
				prices_closeMid = []
				prices_complete = []
				prices_time.append(str(prices[0].get("time")))
				d.append((str(prices[0].get("time")))[:10])
				t.append((str(prices[0].get("time")))[11:19])
				prices_closeBid = prices[0].get("closeBid")
				prices_closeAsk = prices[0].get("closeAsk")
				prices_closeMid.append((prices_closeBid+ prices_closeAsk) / 2.0)
					
				if currency is 'EUR_USD':		
					
					BigDataForTimeEUR_USD += prices_time
					obj["BigDataForPriceEUR_USD"] += prices_closeMid
					Date += d
					Time += t
					
				elif currency is 'GBP_USD':
					obj["BigDataForPriceGBP_USD"] += prices_closeMid
				elif currency is 'AUD_USD':
					obj["BigDataForPriceAUD_USD"] += prices_closeMid
				elif currency is 'USD_JPY':
					obj["BigDataForPriceUSD_JPY"] += prices_closeMid
				elif currency is 'NZD_USD':
					obj["BigDataForPriceNZD_USD"] += prices_closeMid
				elif currency is 'USD_CAD':
					obj["BigDataForPriceUSD_CAD"] += prices_closeMid
				elif currency is 'USD_CHF':
					obj["BigDataForPriceUSD_CHF"] += prices_closeMid
				elif currency is "EUR_GBP":	
					obj["BigDataForPriceEUR_GBP"]+= prices_closeMid 
				elif currency is "EUR_CHF":	
					obj["BigDataForPriceEUR_CHF"]+= prices_closeMid
				elif currency is "EUR_JPY":		
					obj["BigDataForPriceEUR_JPY"]+= prices_closeMid 
				elif currency is "EUR_CAD":	
					obj["BigDataForPriceEUR_CAD"]+= prices_closeMid
				elif currency is "EUR_AUD":	
					obj["BigDataForPriceEUR_AUD"]+= prices_closeMid
				elif currency is "EUR_NZD":	
					obj["BigDataForPriceEUR_NZD"]+= prices_closeMid
				elif currency is "CHF_JPY":	
					obj["BigDataForPriceCHF_JPY"]+= prices_closeMid
				elif currency is "GBP_CHF":	
					obj["BigDataForPriceGBP_CHF"]+= prices_closeMid
				elif currency is "CAD_CHF":	
					obj["BigDataForPriceCAD_CHF"]+= prices_closeMid
				elif currency is "AUD_CHF":	
					obj["BigDataForPriceAUD_CHF"]+= prices_closeMid
				elif currency is "NZD_CHF":	
					obj["BigDataForPriceNZD_CHF"]+= prices_closeMid
				elif currency is "AUD_JPY":	
					obj["BigDataForPriceAUD_JPY"] += prices_closeMid
				elif currency is "AUD_CAD":	
					obj["BigDataForPriceAUD_CAD"]+= prices_closeMid
				elif currency is "AUD_NZD":	
					obj["BigDataForPriceAUD_NZD"]+= prices_closeMid
				elif currency is "GBP_AUD":	
					obj["BigDataForPriceGBP_AUD"] += prices_closeMid
				elif currency is "GBP_JPY":		
					obj["BigDataForPriceGBP_JPY"]+= prices_closeMid
				elif currency is "CAD_JPY":		
					obj["BigDataForPriceCAD_JPY"]+= prices_closeMid
				elif currency is "NZD_JPY":		
					obj["BigDataForPriceNZD_JPY"]+= prices_closeMid 
				elif currency is "GBP_CAD":		
					obj["BigDataForPriceGBP_CAD"] += prices_closeMid 
				elif currency is "GBP_NZD":		
					obj["BigDataForPriceGBP_NZD"] += prices_closeMid 
				elif currency is "NZD_CAD":		
					obj["BigDataForPriceNZD_CAD"]+= prices_closeMid		
				
				fresh = False
				while fresh is False:
					c.execute("SELECT * FROM "+times[time])
					a=c.fetchall()
					d=a[-1:]
					e=d[0][0]
					Total_Previous_Price = d[0][3]+d[0][4]+d[0][5]+d[0][6]+d[0][7]+d[0][8]+d[0][9]+d[0][10]+d[0][11]+d[0][12]+d[0][13]+d[0][14]+d[0][15]+d[0][16]+d[0][17]+d[0][18]+d[0][19]+d[0][20]+d[0][21]+d[0][22]+d[0][23]+d[0][24]+d[0][25]+d[0][26]+d[0][27]+d[0][28]+d[0][29]+d[0][30]
					Total_Current_Price = obj['BigDataForPriceEUR_USD']+obj['BigDataForPriceGBP_USD']+obj['BigDataForPriceAUD_USD']+obj['BigDataForPriceUSD_JPY']+obj['BigDataForPriceNZD_USD']+obj['BigDataForPriceUSD_CAD']+obj['BigDataForPriceUSD_CHF']+obj["BigDataForPriceEUR_GBP"]+obj["BigDataForPriceEUR_CHF"]+obj["BigDataForPriceEUR_JPY"]+obj["BigDataForPriceEUR_CAD"]+obj["BigDataForPriceEUR_AUD"]+obj["BigDataForPriceEUR_NZD"]+obj["BigDataForPriceCHF_JPY"]+obj["BigDataForPriceGBP_CHF"]+obj["BigDataForPriceCAD_CHF"]+obj["BigDataForPriceAUD_CHF"]+obj["BigDataForPriceNZD_CHF"]+obj["BigDataForPriceAUD_JPY"]+obj["BigDataForPriceAUD_CAD"]+obj["BigDataForPriceAUD_NZD"]+obj["BigDataForPriceGBP_AUD"]+obj["BigDataForPriceGBP_JPY"]+obj["BigDataForPriceCAD_JPY"]+obj["BigDataForPriceNZD_JPY"]+obj["BigDataForPriceGBP_CAD"]+obj["BigDataForPriceGBP_NZD"]+obj["BigDataForPriceNZD_CAD"]
					f=str(e)
					if f != BigDataForTimeEUR_USD and Total_Previous_Price != Total_Current_Price:
						rows = zip(BigDataForTimeEUR_USD,Date,Time,obj['BigDataForPriceEUR_USD'],obj['BigDataForPriceGBP_USD'],obj['BigDataForPriceAUD_USD'],obj['BigDataForPriceUSD_JPY'],obj['BigDataForPriceNZD_USD'],obj['BigDataForPriceUSD_CAD'],obj['BigDataForPriceUSD_CHF'],obj["BigDataForPriceEUR_GBP"],obj["BigDataForPriceEUR_CHF"],obj["BigDataForPriceEUR_JPY"],obj["BigDataForPriceEUR_CAD"],obj["BigDataForPriceEUR_AUD"],obj["BigDataForPriceEUR_NZD"],obj["BigDataForPriceCHF_JPY"],obj["BigDataForPriceGBP_CHF"],obj["BigDataForPriceCAD_CHF"],obj["BigDataForPriceAUD_CHF"],obj["BigDataForPriceNZD_CHF"],obj["BigDataForPriceAUD_JPY"],obj["BigDataForPriceAUD_CAD"],obj["BigDataForPriceAUD_NZD"],obj["BigDataForPriceGBP_AUD"],obj["BigDataForPriceGBP_JPY"],obj["BigDataForPriceCAD_JPY"],obj["BigDataForPriceNZD_JPY"],obj["BigDataForPriceGBP_CAD"],obj["BigDataForPriceGBP_NZD"],obj["BigDataForPriceNZD_CAD"])
						c.executemany("INSERT INTO " + times[time] + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
						fresh = True
						print time, currency
					
		conn.commit()
		conn.close()
		#print "done"	
		updated = True
		MAD_To_DB.delay()

def CalculateMaddash():
	conn = sqlite3.connect('db.sqlite3')
	#print "Opened database successfully"

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
	#print "Connection close"

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
	#print "Opened database successfully"
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