import kiteconnect
from kiteconnect import KiteConnect,KiteTicker,ticker
import logging
import pandas as pd
import json
import csv
from time import time,sleep
import pygame
from datetime import datetime
try:
    api_key = "" ## input yout api key
    api_secret ="" ## input your api secreat

    ## get request_key at https://kite.trade/connect/login?api_key= ## api key

    # kite = KiteConnect(api_key=api_key)
    # data = kite.generate_session(request_key,api_secret)
    access_token = ''# or data['access_token'] ## input your token

    logging.basicConfig(level=logging.DEBUG)   ###13430274-niftymay,13430018-BANKNIFTY20MAYFUT

    tokens = [14956546,13014274,12084738,
	      14956290,13014018,12084482,
              1510401,1270529,1346049,340481,81153,
              690691,780803,
	      507395,490755,289539,
              507907,690435,780547,
              447491,278019,288771]

    # Initialise
    kws = KiteTicker('api_key', access_token)
    def on_ticks(ws, ticks):
    # Callback to receive ticks.
        logging.debug("Ticks: {}".format(ticks))
        #tokens = [55634439]#,55653383] #[1510401,1270529,1346049,340481,81153]
        #po.append(ticks)
        #symbol = ['NIFTY20MAYFUT','NIFTY20JUNFUT','NIFTY20JULFUT','BANKNIFTY20MAYFUT','BANKNIFTY20JUNFUT',
        #          'BANKNIFTY20JULFUT','axis','icicibank','indusindbk','hdfc','bajaj-fin','USDINR20JULFUT','GBPINR20JUNFUT','JPYINR20JUNFUT']

        for i in range(len(tokens)):
            try:
                a = (datetime.now(),ticks[i]['instrument_token'],ticks[i]['last_price'],
                ticks[i]['last_quantity'],ticks[i]['average_price'],
                ticks[i]['volume'],ticks[i]['buy_quantity'],ticks[i]['sell_quantity'],
                ticks[i]['ohlc']['open'],ticks[i]['ohlc']['high'],ticks[i]['ohlc']['low'],ticks[i]['ohlc']['close'],
                ticks[i]['change'],ticks[i]['last_trade_time'],ticks[i]['oi'],
                ticks[i]['oi_day_high'],ticks[i]['oi_day_low'],
                ticks[i]['depth']['buy'][0]['quantity'],ticks[i]['depth']['buy'][0]['price'],
                ticks[i]['depth']['buy'][1]['quantity'],ticks[i]['depth']['buy'][1]['price'],
                ticks[i]['depth']['buy'][2]['quantity'],ticks[i]['depth']['buy'][2]['price'],
                ticks[i]['depth']['buy'][3]['quantity'],ticks[i]['depth']['buy'][3]['price'],
                ticks[i]['depth']['sell'][0]['quantity'],ticks[i]['depth']['sell'][0]['price'],
                ticks[i]['depth']['sell'][1]['quantity'],ticks[i]['depth']['sell'][1]['price'],
                ticks[i]['depth']['sell'][2]['quantity'],ticks[i]['depth']['sell'][2]['price'],
                ticks[i]['depth']['sell'][3]['quantity'],ticks[i]['depth']['sell'][3]['price'])
                with open('portfolio_full_mode_data_1sept.csv', 'a+',newline='') as f:   ## name your file here
                    #son.dump(ticks, filehandle)
                    writer = csv.writer(f)
                    writer.writerow(a)
            except:
                print('tick-skip-error')



    def on_connect(ws, response):
        # Callback on successful connect.
        ws.subscribe(tokens)
        #axis 1510401, icicibank 1270529,indusindbk 1346049,,hdfc 340481, bajaj fin 81153

        ws.set_mode(ws.MODE_FULL, tokens)
        #54996743,55953159
    def on_close(ws, code, reason):
    #     # On connection close stop the main loop
    #     # Reconnection will not happen after executing `ws.stop()`
        pygame.init()                                     ## Alarm in case of any error which stops the program
        morty = pygame.mixer.Sound('evil_morty_wav.wav')
        morty.play()
        ws.stop()


    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close
    kws.connect(threaded=True,disable_ssl_verification=False)

    count = 0
    while True:
        count+=1
        if (count%2 == 0):
            if kws.is_connected():
                kws.set_mode(kws.MODE_FULL,tokens)
            else:
                if kws.is_connected():
                    kws.set_mode(kws.MODE_FULL,tokens)
            sleep(2)## cause kws.connect will give errors
except:
    pygame.init()
    morty = pygame.mixer.Sound('evil_morty_wav.wav')
    morty.play()
    print('major-error')
    #pass
