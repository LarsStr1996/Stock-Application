from create_wallet import Create_wallet
from data_visualisation import DataVisual
from personal_wallet import Personal_wallet
from stock import Stock
from tkinter import *
from yahoo_fin.stock_info import *
from yahoo_fin import stock_info as si
import time
from live_plot import plots

class Runner(object):
       
       def ticker_list():
              tickers = Stock.show_ticker_list()
              print(tickers)
       def dividend():
              dividend = Stock().dividend()
              dividend = dividend.iloc[10,1]
              print(dividend)
       def run_create_wallet():
              Create_wallet.wallet(wallet_name_x)
       def run_stock_value():
              comp = company_name.get()
              plots.live_plot_stocks(comp)  
       def run_historical_stock():
              comp = company_name.get()
              inte = interval.get()
              start = start_date.get()
              end = end_date.get()
              plots.historical_stock(inte,start,end,comp)
       def run_personal_wallet():
              wallet_na = wallet_name.get()
              wallet,message = Personal_wallet().open_wallet(wallet_na)
              if message == False:
                     Label(screen10,text="Wallet Doesn't Exist").pack()
                     Label(screen10,text="").pack()
                     Label(screen10,text="Do you want a new wallet?").pack()
                     Button(screen10,text='Yes',width = 10,height = 1,command = Welcome.create_wallet()).pack()
                     delBut = Button(screen10,text='No',width=10,height=1,command=Welcome.delete_10)
                     delBut.pack()
              elif message == True:
                     plots.wallet_plot(wallet_na)
       
class Screens(object):
       def __init__(self,screen):
              self.screen = screen
       def stock(self):
              self.screen7 = Toplevel(self.screen)
              self.screen7.title("Live Stock Value")
              self.screen7.geometry("300x300")
              Label(self.screen7,text="Stock Value: ").pack()
              global company_name
              company_name = StringVar()
              self.company_name_entry = Entry(self.screen7,textvariable = company_name)
              self.company_name_entry.pack()
              Button(self.screen7, text="Find Stock",width = 10,height = 1,command = Runner.run_stock_value).pack()
              
       def historical_stock(self):
              self.screen8 = Toplevel(self.screen)
              self.screen8.title("Live Stock Value")
              self.screen8.geometry("300x300")
              Label(self.screen8,text="Stock Name: ").pack()
              global start_date
              global end_date
              global interval
              global company_name
              company_name = StringVar()
              company_name_entry = Entry(self.screen8,textvariable = self.company_name)
              company_name_entry.pack()
              start_date = StringVar()
              end_date = StringVar()
              interval = StringVar()
              Label(self.screen8,text="Start Date (m/d/y): ").pack()
              start_date_entry = Entry(self.screen8,textvariable = start_date)
              start_date_entry.pack()
              Label(self.screen8,text="End Date (m/d/y): ").pack()
              end_date_entry = Entry(self.screen8,textvariable = end_date)
              end_date_entry.pack()
              Label(self.screen8,text="Interval (month,week,day): ").pack()
              interval_entry = Entry(self.screen8,textvariable = interval)
              interval_entry.pack()
              Button(self.screen8, text="Find Stock",width = 10,height = 1,command = Runner.run_historical_stock).pack()
              return self.company_name
              
       def personal_wallet(self):
              global screen10
              screen10 = Toplevel(self.screen)
              screen10.title("Personal Wallet")
              screen10.geometry("300x300")
              global wallet_name
              Label(screen10,text="Wallet Name: ").pack()
              wallet_name = StringVar()
              wallet_name_entry = Entry(screen10,textvariable = wallet_name)
              wallet_name_entry.pack()
              find_wallet_button = Button(screen10, text="Find Wallet",width = 10,height = 1,command = Runner.run_personal_wallet)  
              find_wallet_button.pack()
       def company_list(self):
              global screen9
              screen9 = Toplevel(self.screen)
              screen9.title("Company List")
              screen9.geometry("500x500")
              listbox= Listbox(screen9)
              listbox.insert(comp)
       def create_wallet(self):
              global screen11
              screen11 = Toplevel(self.screen)
              screen11.title("Wallet Builder")
              screen11.geometry("300x300")
              Label(screen11,text="Wallet Name: ").pack()
              global wallet_name_x
              wallet_name_x = StringVar()
              wallet_name_x_entry = Entry(screen11,textvariable = wallet_name_x)
              wallet_name_x_entry.pack()
              Button(screen11,text='Yes',width = 10,height = 1,command = Runner.run_create_wallet).pack()
              
       
class Buttons(object):
       def button_access_system(screen):
              h = 1
              w = 20
              b1 = Button(screen,text='Live Stock Value',height=h,width=w, command = Screens(screen).stock).pack(expand=True)
              b2 = Button(screen,text='Historical Stock',height=h,width=w, command = Screens(screen).historical_stock).pack(expand=True)
              b3 = Button(screen,text='Company List',height=h,width=w, command = Screens(screen).company_list).pack(expand=True)
              b4 = Button(screen,text='Personal Wallet',height=h,width=w, command = Screens(screen).personal_wallet).pack(expand=True)
              b5 = Button(screen,text='Dividend',height=h,width=w, command = Runner.dividend).pack(expand=True)
              b6 = Button(screen,text='Create Wallet',height=h,width=w, command = Screens(screen).create_wallet).pack(expand=True)
              b7 = Button(screen,text='7',height=h,width=w).pack(expand=True)
              b8 = Button(screen,text='8',height=h,width=w).pack(expand=True)
              b9 = Button(screen,text='Settings',height=h,width=w).pack(expand=True)
              b0 = Button(screen,text='Return to Login',height=h,width=w, command = screen.destroy).pack(expand=True)

       
       
              
       
       
