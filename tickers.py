import pandas as pd
import numpy as np
from yahoo_fin.stock_info import *
from yahoo_fin import stock_info as si


class search_tickers():
       def __init__(self):
              pass
       
       def load_ticker_file(file_loc,sheet_name):
              dfs = pd.read_excel(file_loc, sheet_name=sheet_name)
              return dfs
       
       def query(dataframe):
              search_number = 0
              again = 'y'
              from_ticker = False
              from_name = False
              from_category = False
              from_country = False
              while True:
                     type_of_search = input('What kind of search? ')
                     
                     if type_of_search == 'Ticker':
                            from_ticker = True
                     elif type_of_search == 'Name':
                            from_name = True
                     elif type_of_search == 'Category':
                            from_category = True
                     elif type_of_search == 'Country':
                            from_country = True
                     else:
                            print('Search type is invalid')
                     
                     Name = input('Name: ')
                     df = dataframe
                     if from_ticker == True:
                            df = df.loc[lambda df: df['Ticker']==Name]
                            
                     elif from_name == True:
                            #df = df.loc[lambda df: df['Name']==Name]
                            df['Name_found'] = df['Name'].str.contains(Name)
                            df = df.loc[lambda df: df['Name_found']==True]
                     elif from_category == True:
                            df = df.loc[lambda df: df['Category Name']==Name]
                     elif from_country == True:
                            df = df.loc[lambda df: df['Country']==Name]
                     else:
                            print('your input is invalid')
                     again = input('Is this what you were looking for? (y/n) ')
                     if again == 'n':
                            continue
                     elif again == 'y':
                            return df
                     
                     search_number += 1

file_loc      = r"C:\Python37\personal_scripts\stock\tickers.xlsx"
sheet_name    = 'Stock'

dfs = search_tickers.load_ticker_file(file_loc,sheet_name)                     
search_tickers.query(dfs)

