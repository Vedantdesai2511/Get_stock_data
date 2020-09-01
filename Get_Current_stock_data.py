import requests
from bs4 import BeautifulSoup
import re
import time
import robin_stocks as rh
import pandas as pd
import numpy as np

Dict = {}


class GetCurrentStockData:

    def __init__(self, stock_name=None):
        self.stock_name = stock_name

    def stock_current_price(self):
        """
        This function takes datat from the google and return the current stock value of inputted stock
        :return: stock value (float)
        """

        # Can optimize hte function by using __repr__ function
        # TODO: bug - Cannot read if the stock value is > 1000.

        print(self)

        page1 = requests.get('https://finance.yahoo.com/quote/' + str(self) + '?p=' + str(self) + '&.tsrc=fin-srch')

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
        page1 = requests.get('https://www.google.com/search?q=' + str(self.stock_name).lower() + '+google+stock&rlz'
                                                                                                 '=1C1CHBF_enUS880US880&oq=' + str(self.stock_name).lower() + '+google+stock&aqs=chrome..69i57j0.9427j0j7&sourceid=chrome&ie=UTF-8')

        soup1 = BeautifulSoup(page1.text, 'html.parser')

        try:
            data1 = soup1.find(class_='BNeawe iBp4i AP7Wnd')
        except:
            data1 = soup1.find(class_='IsqQVc NprOob XcVN5d fw-price-dn')

        data1 = str(data1)
        abc1 = re.findall("\d+\.\d+", data1)

        try:
            curr_price = float(abc1[0])
        except:
            abc1 = re.findall("\d+", data1)
            curr_price = float(abc1[0])

        print(f'current price {self.stock_name} : {curr_price}')

        return curr_price


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
            df1.loc[df1.Quote == sym[idx], 'Curr_price'] = curr_price
            print("{} | {}".format(quote['symbol'], quote['ask_price']))

        return df1
