import requests
from bs4 import BeautifulSoup
import re
# from datetime import datetime
import time
import robin_stocks as rh
import pandas as pd
# from pandas import *

# stock_name_list = ["EURUSD", "JPY", "GBPUSD", "AUDUSD", "NZDUSD"]

# stock_name_list = ['ROKU', 'NVDA', 'AAPL', 'FB']
                   # 'FB']  # , 'NFLX', 'OKTA', 'SQ', 'SHOP', 'SPLK', 'ALGN', 'DIN', 'TSLA', 'SSNLF',
#                    'MSFT', 'AMZN', 'GOOGL', 'BQCNF', 'BABA', 'TCEHY', 'V', 'JNJ', 'WMT', 'JPM', 'NSRGY', 'MA', 'NSRGF',
#                    'RHHBY', 'RHHVF']

Dict = {}


# print("Hola")


class GetCurrentStockData:

    def __init__(self, stock_name=None):
        self.stock_name = stock_name

    # def get_current_price(self):
    #     # global Dict
    #
    #     if self in stock_name_list:
    #         Dict[self].append(GetCurrentStockData.stock_current_price(self))
    #     else:
    #         Dict[self] = [GetCurrentStockData.stock_current_price(self)]
    #
    #     print(Dict)
    #     return Dict

    def stock_current_price(self):
        print(self)

        page1 = requests.get('https://finance.yahoo.com/quote/' + str(self) + '?p=' + str(self) + '&.tsrc=fin-srch')

        soup1 = BeautifulSoup(page1.text, 'html.parser')

        data1 = soup1.find(class_='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)')

        data1 = str(data1)
        abc1 = re.findall("\d+\.\d+", data1)
        # print("Hello")

        # curr_price = float(abc1[2])
        try:
            curr_price = float(abc1[2])
        except:
            abc1 = re.findall("\d+", data1)
            curr_price = float(abc1[-1])

        print(f'current price {self} : {curr_price}')
        time.sleep(0.5)
        return curr_price

    def stock_current_price_forex(self):

        page1 = requests.get('https://finance.yahoo.com/quote/' + str(self) + '%3DX?p=' + str(self) + '%3DX')

        soup1 = BeautifulSoup(page1.text, 'html.parser')

        data1 = soup1.find(class_='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)')

        data1 = str(data1)
        abc1 = re.findall("\d+\.\d+", data1)

        try:
            curr_price = float(abc1[2])
        except:
            abc1 = re.findall("\d+", data1)
            curr_price = float(abc1[-1])

        print(f'current price {self} : {curr_price}')
        time.sleep(0.5)
        return curr_price

    def stock_current_price_google_web_scraper(self):
        # company_names = self

        page1 = requests.get('https://www.google.com/search?q=' + str(self.stock_name).lower() + '+google+stock&rlz=1C1CHBF_enUS880US880&oq=' + str(self.stock_name).lower() + '+google+stock&aqs=chrome..69i57j0.9427j0j7&sourceid=chrome&ie=UTF-8')

        soup1 = BeautifulSoup(page1.text, 'html.parser')
        # print(soup1)

        # beutysoup = BeautifulSoup.prettify(soup1)
        # print(beutysoup)

        try:
            data1 = soup1.find(class_='BNeawe iBp4i AP7Wnd')
            # print(data1)
        except:
            data1 = soup1.find(class_='IsqQVc NprOob XcVN5d fw-price-dn')
            # print(data1)

        data1 = str(data1)
        abc1 = re.findall("\d+\.\d+", data1)

        try:
            curr_price = float(abc1[0])
        except:
            abc1 = re.findall("\d+", data1)
            curr_price = float(abc1[0])

        # print(curr_price)
        print(f'current price {self.stock_name} : {curr_price}')

        return curr_price
    #
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     result = [executor.submit(GetCurrentStockData.get_current_price, stock_name) for stock_name in stock_name_list]


class RobinHoodCurrentPrice:
    def __init__(self, symbol):
        self.user = 'vedantdesai07@gmail.com'
        self.password = 'Vbd@25111996'
        self.symbol = symbol

    def get_current_price(self):
        rh.login(self.user, self.password)
        quotes = rh.get_quotes(self.symbol)

        sym = self.symbol
        b = np.zeros(len(sym))

        quotes = rh.get_quotes(self.symbol)

        df1 = pd.DataFrame({'Quote': sym, 'Curr_price': b}, index=np.arange(len(sym)))

        for idx, quote in enumerate(quotes):
            curr_price = quote['ask_price']
            # print(curr_price)

            # print(df1)
            # print(sym[idx])
            df1.loc[df1.Quote == sym[idx], 'Curr_price'] = curr_price

            # print(df1)
            print("{} | {}".format(quote['symbol'], quote['ask_price']))

        return df1

# print(GetCurrentStockData('ROKU').stock_current_price_google_web_scraper())
