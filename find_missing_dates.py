# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:54:22 2020

@author: verma
"""

import datetime
import pandas as pd


def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timetsamp is empty for now
    dates =  pd.DataFrame(columns=['Record_timestamp'],
        index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'

#    print(dir(dates))
#    print(dir(dates.index))
    days_names = {
        i: name
        for i, name
        in enumerate(['Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday', 
                      'Sunday'])
    }

    dates['WeekDayInt'] = dates.index.dayofweek
    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Week'] = dates.index.week
    dates['Month'] = dates.index.month
    dates['Quarter'] = dates.index.quarter
    dates['Year_half'] = dates.index.month.map(lambda mth: 1 if mth <7 else 2)
    dates['Year'] = dates.index.year
    dates['DateInt'] = dates.index.year * 10000 + dates.index.month * 100 + dates.index.day
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates


dates = create_date_table('2020-01-01','2020-01-31')
print(dates.head(1))
print(len(dates))
dates_filtered = dates[dates.WeekDayInt < 5]
print(len(dates_filtered))
# print(dates_filtered.DateInt)




