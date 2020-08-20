import pandas as pd
import os
from tkinter import *
class Create_wallet(object):                
       def wallet(wallet_name):
              wallet_name = str(wallet_name)
              data = {'Company': [],\
                     'Initial Value': [],\
                     'Stock Amount': [],\
                     'Most recent Dividend': [],\
                     'Total Dividend': [],
                     'yield':[]}
              x = pd.DataFrame(data)
              x.columns = ['Name','Initial Value','Stock Amount',\
                           'Most recent Dividend','Total Dividend','Yield']
              if os.path.isfile('wallets/'+wallet_name+'.pkl'):
                     question = input('Do you want to overwrite? (y/n) ')
                     if question == 'y':
                            x.to_pickle('wallets/'+wallet_name+'.pkl')
                            return
                     elif question == 'n':
                            return
              else:
                     x.to_pickle('wallets/'+wallet_name+'.pkl')
                     
                     
