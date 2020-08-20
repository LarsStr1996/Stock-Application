import pandas as pd
import os
import numpy as np
class Stock(object):
       def __init__(self):
              self.name = input('CompanyName: ')
       def company_char(self):
              name = self.name 
       
       def stock_value(self):
              live_stock = si.get_live_price(self.name)
              return live_stock
                     
       def dividend(self):
              dividend = si.get_quote_table(self.name,dict_result=False)
              dividend = pd.DataFrame(dividend)
              return dividend
       
       def show_ticker_list():
              tickers = tickers_other()
              return tickers


                     

       





       
