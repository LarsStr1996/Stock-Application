import pandas as pd
class Personal_wallet(object):
       def __init__(self):
              pass
       def update_wallet():
              pass
                     
       def add_data():
              pass
       def yield_(self):
              wallet_yield = (costs/walletValue)*100
              return wallet_yield
       def costs(self):
              pass
       def dividend(self):
              pass
       def wallet_value(self):
              wallet_value = self.costs+self.dividend+self.costs
              return wallet_value
       
       def initial_value():
              price = float(input('Price at moment of buying: '))
              return price
       
       def stock_amount():
              amount = float(input('Number of stocks you bought: '))
              return amount
       
       def open_wallet(self,wallet_name):
              try:
                     wallet = pd.read_pickle('wallets/'+wallet_name+'.pkl')
                     message = True
                     return wallet,message
              except:
                     error_message = False
                     wallet = 'Empty'
                     return wallet,error_message
              
       
