from yahoo_fin.stock_info import *
from yahoo_fin import stock_info as si
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
plt.style.use('seaborn-white')
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.dates as md
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from bokeh.plotting import figure, gridplot, output_file, show
from bokeh.models.widgets import CheckboxGroup
from bokeh.models.widgets import Dropdown
#from bokeh.io import output_file, show, vform
from bokeh.models.widgets import TextInput

from celluloid import Camera

import dash
from dash.dependencies import Output
#from dash.dependencies import Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

class plots(object):
       def live_plot_stocks(name):
              sns.set()
              i = 0
              live_stock_total = []
              ix = []
              t = 3
              fig,ax1 = plt.subplots()
              fig.suptitle('Live Stock Value '+name)
              color = [] 
              time_x = []
              time = datetime.now()
              print(time)
              while True:
                     
                     time += timedelta(seconds = t)
                     time_x.append(time)
                     live_stock = si.get_live_price(name)
                     live_stock_total.append(live_stock)
                     stock_difference = live_stock_total[i]-live_stock_total[i-1]
                     ix.append(i)
                     ax1.clear()
                     if live_stock_total[i] - live_stock_total[i-1] > 0.0:
                            color.append('green')
                            ax1.bar(time_x,live_stock_total,color='green')
                     elif live_stock_total[i] - live_stock_total[i-1] < 0.0:
                            ax1.bar(time_x,live_stock_total,color='red')
                            color.append('red')
                     else:
                            ax1.bar(time_x,live_stock_total,color='black')
                            color.append('black')
                     print(color)
                     if i > 50:
                            plt.xlim(time-timedelta(seconds=t*50))
                            
                     if i > 0:
                            #xfmt = md.DateFormatter('%H:%M:%S')
                            #ax1.xaxis.set_major_formatter(xfmt)
                            plt.tick_params(axis='x',which='both',bottom=True,top=False,labelbottom=True)
                            fig.autofmt_xdate()
                     elif i == 0:
                            plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
                        
                     #plt.ylim(min(live_stock_total),max(live_stock_total))
                     if i > 0:
                            plt.pause(t)
                     i += 1
              return

       def historical_stock(interval,start,end,name):
              
              sns.set()
              
              interval = interval
              if interval == 'Month' or interval == 'month':
                     interval = '1mo'
              elif interval == 'Day' or interval == 'day':
                     interval = '1d'
              elif interval == 'Week' or interval == 'week':
                     interval = '1wk'
              elif interval == '':
                     interval = '1d'
                   
              start_date    = start
              if start_date == '':
                     start_date = '01-01-2000'
                     interval = '1mo'
                     
              end_date      = end
              if end_date == '':
                     end_date = datetime.now()
                     interval = '1mo'
              
              from1999 = get_data(name, start_date = start_date,\
                                  end_date=end_date,interval=interval)
              from1999 = from1999.reset_index()
              plt.figure(figsize=(9, 6))
              ax = plt.subplot(111)  
              ax.spines["top"].set_visible(False)  
              ax.spines["right"].set_visible(False)
              ax.get_xaxis().tick_bottom()  
              ax.get_yaxis().tick_left()
              plt.xticks(rotation=45)
              plt.title("Historical Stock Value: "+name, fontsize=22)
              plt.ylim(min(from1999['close'])-2,max(from1999['close'])+2)
              plt.plot(from1999['index'],from1999['close'])
              plt.show()
              return

       def wallet_plot(name):
              sns.set()
              plt.figure(figsize=(9, 6))
              ax = plt.subplot(111)  
              ax.spines["top"].set_visible(False)  
              ax.spines["right"].set_visible(False)
              ax.get_xaxis().tick_bottom()  
              ax.get_yaxis().tick_left()
              plt.xticks(rotation=45)
              plt.title("Historical Stock Value: "+name, fontsize=22)
              #plt.ylim(min(from1999['close'])-2,max(from1999['close'])+2)
              plt.plot(from1999['index'],from1999['close'])
              plt.show()

              
class test(object):
       def live_plots():
              plots.live_plot_stocks('RDSA.AS')
       def historical_stock():
              interval = 'Day'
              start = '01-01-2000'
              end = '08-06-2020'
              name = 'RDS-A'
              plots.historical_stock(interval,start,end,name)
       def wallet():
              name='RDSA.AS'
              plots.wallet_plot(name)
              
test_live_plots = True
test_historical_stock = False
test_wallet = False       
if test_live_plots == True:
       test.live_plots()
elif test_historical_stock == True:
       test.historical_stock()
elif test_wallet == True:
       test.wallet()

              
       



       
       
