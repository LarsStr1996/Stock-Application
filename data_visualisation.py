import pandas as pd
import numpy as np
class DataVisual(object):
       newJob = 'New Job'
       key1 = '--- 1 = Stock Value     '
       key2 = '--- 2 = History         '
       key3 = '--- 3 = Stock List      '
       key4 = '--- 4 = Open Wallet     '
       key5 = '--- 5 = Dividend        '
       key6 = '--- 6 = Create Wallet   '
       key7 = '--- 7 = Forgot Password?'
       key8 = '--- 8 =                 '
       key9 = '--- 9 =                 '
       keyboard = np.array([[key1,key2,key3],[key4,key5,key6],[key7,key8,key9]])
       keyboard = pd.DataFrame(keyboard)
