from jugaad_data.nse import bhavcopy_save
import pandas as pd
from jugaad_data.holidays import holidays

date_range = pd.bdate_range(start='02/01/2022', end='03/31/2022', freq='C', holidays=holidays(2022))

# for i in date_range[-31:-1]:
#     bhavcopy_save(i, "datafile")
# cf = pd.read_csv('https://archives.nseindia.com/content/equities/EQUITY_L.csv')
# li = []
# for i in cf.columns:
#     if i[0] == ' ':
#         i = i[1:]
#     i = i.replace(' ', '_')
#     li += [i]
# cf.columns = li

# cf.to_csv('datafile/Securities.csv', index=False)
