import sqlite3
import oandapy
import csv
import numpy as np

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

oanda = oandapy.API(environment="practice", access_token="bc27a46b1615b33ede78f1de2c0dffe0-e1b6efb42854e92b5c526549993252b5")

currencies = ['EUR_USD', 'GBP_USD', 'AUD_USD','USD_JPY', 'NZD_USD', 'USD_CAD', 'USD_CHF','EUR_GBP', 'EUR_CHF', 'EUR_JPY', 'EUR_CAD', 'EUR_AUD', 'EUR_NZD', 'CHF_JPY', 
			  'GBP_CHF', 'CAD_CHF', 'AUD_CHF', 'NZD_CHF', 'AUD_JPY', 'AUD_CAD', 'AUD_NZD', 'GBP_AUD', 'GBP_JPY', 'CAD_JPY', 'NZD_JPY', 'GBP_CAD', 'GBP_NZD', 'NZD_CAD']
times = ['M1','M5','M15','M30','H1']


for time in times:

	BigDataForTimeEUR_USD = []
	Date=[]
	Time=[]
	BigDataForPriceEUR_USD =[]
	#BigDataForTimeGBP_USD = []
	BigDataForPriceGBP_USD =[]
	#BigDataForTimeAUD_USD = []
	BigDataForPriceAUD_USD =[]
	#BigDataForTimeUSD_JPY = []
	BigDataForPriceUSD_JPY =[]
	#BigDataForTimeNZD_USD = []
	BigDataForPriceNZD_USD =[]
	#BigDataForTimeUSD_CAD = []
	BigDataForPriceUSD_CAD =[]
	#BigDataForTimeUSD_CHF = []
	BigDataForPriceUSD_CHF =[]
	BigDataForPriceEUR_GBP=[] 
	BigDataForPriceEUR_CHF=[] 
	BigDataForPriceEUR_JPY=[] 
	BigDataForPriceEUR_CAD=[] 
	BigDataForPriceEUR_AUD=[]  
	BigDataForPriceEUR_NZD=[]  
	BigDataForPriceCHF_JPY=[] 
	BigDataForPriceGBP_CHF=[]  
	BigDataForPriceCAD_CHF=[]  
	BigDataForPriceAUD_CHF =[] 
	BigDataForPriceNZD_CHF =[] 
	BigDataForPriceAUD_JPY =[] 
	BigDataForPriceAUD_CAD =[] 
	BigDataForPriceAUD_NZD =[] 
	BigDataForPriceGBP_AUD =[] 
	BigDataForPriceGBP_JPY =[] 
	BigDataForPriceCAD_JPY =[] 
	BigDataForPriceNZD_JPY =[] 
	BigDataForPriceGBP_CAD =[] 
	BigDataForPriceGBP_NZD =[] 
	BigDataForPriceNZD_CAD=[] 
	

	print "Collecting %r Data" % (time)

	for currency in currencies:

		print "Collecting %r Data" % (currency)

		res = oanda.get_history(instrument=currency, granularity=time) # currencies
		ccy = res.get("instrument")
		prices = res.get('candles')

			# highAsk, lowAsk, complete, openBid, closeAsk, closeBid, 
			# Volume, openAsk, time, lowBid, highBid


			#------------------------------
			# MAKE SURE DATABASE IS CLEAN
			#------------------------------

		prices_time = ["Time"]
		t=["Time"]
		d=["Date"]
		prices_closeMid = [ccy]
		prices_complete = []
		CCY = []
		BigData = []

			# Get time, close_price,complete status

		for index, value in enumerate(prices):
			# currency name
			# time
			prices_time.append(prices[index].get("time"))
			d.append((str(prices[index].get("time")))[:10])
			t.append((str(prices[index].get("time")))[11:19])
			# price
			prices_closeBid = prices[index].get("closeBid")
			prices_closeAsk = prices[index].get("closeAsk")
			prices_closeMid.append((prices_closeBid+ prices_closeAsk) / 2.0)
			# completed
			# prices_complete.append(prices[index].get("complete"))
		if currency is 'EUR_USD':		
			BigDataForTimeEUR_USD += prices_time
			BigDataForPriceEUR_USD += prices_closeMid
			Date +=d
			Time +=t
		elif currency is 'GBP_USD':
			
			BigDataForPriceGBP_USD += prices_closeMid
		elif currency is 'AUD_USD':
			
			BigDataForPriceAUD_USD += prices_closeMid
		elif currency is 'USD_JPY':
			
			BigDataForPriceUSD_JPY += prices_closeMid
		elif currency is 'NZD_USD':
			
			BigDataForPriceNZD_USD += prices_closeMid
		elif currency is 'USD_CAD':
			
			BigDataForPriceUSD_CAD += prices_closeMid
		elif currency is 'USD_CHF':
			
			BigDataForPriceUSD_CHF += prices_closeMid
		elif currency is "EUR_GBP":	
			BigDataForPriceEUR_GBP += prices_closeMid 
		elif currency is "EUR_CHF":	
			BigDataForPriceEUR_CHF+= prices_closeMid
		elif currency is "EUR_JPY":		
			BigDataForPriceEUR_JPY+= prices_closeMid 
		elif currency is "EUR_CAD":	
			BigDataForPriceEUR_CAD+= prices_closeMid
		elif currency is "EUR_AUD":	
			BigDataForPriceEUR_AUD+= prices_closeMid
		elif currency is "EUR_NZD":	
			BigDataForPriceEUR_NZD+= prices_closeMid
		elif currency is "CHF_JPY":	
			BigDataForPriceCHF_JPY+= prices_closeMid
		elif currency is "GBP_CHF":	
			BigDataForPriceGBP_CHF+= prices_closeMid
		elif currency is "CAD_CHF":	
			BigDataForPriceCAD_CHF+= prices_closeMid
		elif currency is "AUD_CHF":	
			BigDataForPriceAUD_CHF+= prices_closeMid
		elif currency is "NZD_CHF":	
			BigDataForPriceNZD_CHF+= prices_closeMid
		elif currency is "AUD_JPY":	
			BigDataForPriceAUD_JPY += prices_closeMid
		elif currency is "AUD_CAD":	
			BigDataForPriceAUD_CAD += prices_closeMid
		elif currency is "AUD_NZD":	
			BigDataForPriceAUD_NZD += prices_closeMid
		elif currency is "GBP_AUD":	
			BigDataForPriceGBP_AUD += prices_closeMid
		elif currency is "GBP_JPY":		
			BigDataForPriceGBP_JPY += prices_closeMid
		elif currency is "CAD_JPY":		
			BigDataForPriceCAD_JPY += prices_closeMid
		elif currency is "NZD_JPY":		
			BigDataForPriceNZD_JPY += prices_closeMid 
		elif currency is "GBP_CAD":		
			BigDataForPriceGBP_CAD += prices_closeMid 
		elif currency is "GBP_NZD":		
			BigDataForPriceGBP_NZD += prices_closeMid 
		elif currency is "NZD_CAD":		
			BigDataForPriceNZD_CAD+= prices_closeMid 		
		#print CCY	
		#print prices_time	
		#print prices_closeMid
		#print prices_complete
	if time is 'M1':
		
		rows = zip(BigDataForTimeEUR_USD,Date,Time,BigDataForPriceEUR_USD,BigDataForPriceGBP_USD,BigDataForPriceAUD_USD,BigDataForPriceUSD_JPY,BigDataForPriceNZD_USD,BigDataForPriceUSD_CAD,BigDataForPriceUSD_CHF,BigDataForPriceEUR_GBP,BigDataForPriceEUR_CHF,BigDataForPriceEUR_JPY,BigDataForPriceEUR_CAD ,BigDataForPriceEUR_AUD  ,BigDataForPriceEUR_NZD  ,BigDataForPriceCHF_JPY,BigDataForPriceGBP_CHF,BigDataForPriceCAD_CHF ,BigDataForPriceAUD_CHF ,BigDataForPriceNZD_CHF ,BigDataForPriceAUD_JPY  ,BigDataForPriceAUD_CAD  ,BigDataForPriceAUD_NZD ,BigDataForPriceGBP_AUD ,BigDataForPriceGBP_JPY ,BigDataForPriceCAD_JPY ,BigDataForPriceNZD_JPY ,BigDataForPriceGBP_CAD ,BigDataForPriceGBP_NZD ,BigDataForPriceNZD_CAD)
		#for row in rows:	
		c.executemany("INSERT INTO prices_price_m1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
		#conn.commit()
	elif time is 'M5':
		
		rows = zip(BigDataForTimeEUR_USD,Date,Time,BigDataForPriceEUR_USD,BigDataForPriceGBP_USD,BigDataForPriceAUD_USD,BigDataForPriceUSD_JPY,BigDataForPriceNZD_USD,BigDataForPriceUSD_CAD,BigDataForPriceUSD_CHF,BigDataForPriceEUR_GBP,BigDataForPriceEUR_CHF,BigDataForPriceEUR_JPY,BigDataForPriceEUR_CAD ,BigDataForPriceEUR_AUD  ,BigDataForPriceEUR_NZD  ,BigDataForPriceCHF_JPY,BigDataForPriceGBP_CHF,BigDataForPriceCAD_CHF ,BigDataForPriceAUD_CHF ,BigDataForPriceNZD_CHF ,BigDataForPriceAUD_JPY  ,BigDataForPriceAUD_CAD  ,BigDataForPriceAUD_NZD ,BigDataForPriceGBP_AUD ,BigDataForPriceGBP_JPY ,BigDataForPriceCAD_JPY ,BigDataForPriceNZD_JPY ,BigDataForPriceGBP_CAD ,BigDataForPriceGBP_NZD ,BigDataForPriceNZD_CAD)
		#for row in rows:	
		c.executemany("INSERT INTO prices_price_m5 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
		#conn.commit()
	elif time is 'M15':
		
		rows = zip(BigDataForTimeEUR_USD,Date,Time,BigDataForPriceEUR_USD,BigDataForPriceGBP_USD,BigDataForPriceAUD_USD,BigDataForPriceUSD_JPY,BigDataForPriceNZD_USD,BigDataForPriceUSD_CAD,BigDataForPriceUSD_CHF,BigDataForPriceEUR_GBP,BigDataForPriceEUR_CHF,BigDataForPriceEUR_JPY,BigDataForPriceEUR_CAD ,BigDataForPriceEUR_AUD  ,BigDataForPriceEUR_NZD  ,BigDataForPriceCHF_JPY,BigDataForPriceGBP_CHF,BigDataForPriceCAD_CHF ,BigDataForPriceAUD_CHF ,BigDataForPriceNZD_CHF ,BigDataForPriceAUD_JPY  ,BigDataForPriceAUD_CAD  ,BigDataForPriceAUD_NZD ,BigDataForPriceGBP_AUD ,BigDataForPriceGBP_JPY ,BigDataForPriceCAD_JPY ,BigDataForPriceNZD_JPY ,BigDataForPriceGBP_CAD ,BigDataForPriceGBP_NZD ,BigDataForPriceNZD_CAD)
		#for row in rows:
		c.executemany("INSERT INTO prices_price_m15 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
		#conn.commit()
	elif time is 'M30':
		
		rows = zip(BigDataForTimeEUR_USD,Date,Time,BigDataForPriceEUR_USD,BigDataForPriceGBP_USD,BigDataForPriceAUD_USD,BigDataForPriceUSD_JPY,BigDataForPriceNZD_USD,BigDataForPriceUSD_CAD,BigDataForPriceUSD_CHF,BigDataForPriceEUR_GBP,BigDataForPriceEUR_CHF,BigDataForPriceEUR_JPY,BigDataForPriceEUR_CAD ,BigDataForPriceEUR_AUD  ,BigDataForPriceEUR_NZD  ,BigDataForPriceCHF_JPY,BigDataForPriceGBP_CHF,BigDataForPriceCAD_CHF ,BigDataForPriceAUD_CHF ,BigDataForPriceNZD_CHF ,BigDataForPriceAUD_JPY  ,BigDataForPriceAUD_CAD  ,BigDataForPriceAUD_NZD ,BigDataForPriceGBP_AUD ,BigDataForPriceGBP_JPY ,BigDataForPriceCAD_JPY ,BigDataForPriceNZD_JPY ,BigDataForPriceGBP_CAD ,BigDataForPriceGBP_NZD ,BigDataForPriceNZD_CAD)
		#for row in rows:
		c.executemany("INSERT INTO prices_price_m30 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
		#conn.commit()
	elif time is 'H1':
		
		rows = zip(BigDataForTimeEUR_USD,Date,Time,BigDataForPriceEUR_USD,BigDataForPriceGBP_USD,BigDataForPriceAUD_USD,BigDataForPriceUSD_JPY,BigDataForPriceNZD_USD,BigDataForPriceUSD_CAD,BigDataForPriceUSD_CHF,BigDataForPriceEUR_GBP,BigDataForPriceEUR_CHF,BigDataForPriceEUR_JPY,BigDataForPriceEUR_CAD ,BigDataForPriceEUR_AUD  ,BigDataForPriceEUR_NZD  ,BigDataForPriceCHF_JPY,BigDataForPriceGBP_CHF,BigDataForPriceCAD_CHF ,BigDataForPriceAUD_CHF ,BigDataForPriceNZD_CHF ,BigDataForPriceAUD_JPY  ,BigDataForPriceAUD_CAD  ,BigDataForPriceAUD_NZD ,BigDataForPriceGBP_AUD ,BigDataForPriceGBP_JPY ,BigDataForPriceCAD_JPY ,BigDataForPriceNZD_JPY ,BigDataForPriceGBP_CAD ,BigDataForPriceGBP_NZD ,BigDataForPriceNZD_CAD)
		#for row in rows:
		c.executemany("INSERT INTO prices_price_H1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rows)
		
conn.commit()
conn.close()
print "done"