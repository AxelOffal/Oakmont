# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 00:01:55 2023

@author: willi
"""
#https://www.abs.gov.au/about/data-services/application-programming-interfaces-apis/data-api-user-guide
#https://stackoverflow.com/questions/59979833/how-to-get-data-from-australia-bureau-of-statistics-using-pandasmdx
import pandas as pd
from pandasdmx import Request
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# disable_warnings(InsecureRequestWarning)


# abs = Request('ABS')

# data_response = abs.data(resource_id='CPI')

# cpi_data = data_response.write(pd.DataFrame)

# print(cpi_data.head())

# # Step 6: Save the Data (if needed)
# cpi_data.to_csv('cpi_data.csv', index=False)

Agency_Code = 'ABS'
Dataset_Id = 'ATSI_BIRTHS_SUMM'
ABS = Request(Agency_Code)
data_response = ABS.data(resource_id='ATSI_BIRTHS_SUMM', params={'startPeriod': '2016'})

#This will result into a stacked DataFrame
df = data_response.write(data_response.data.series, parse_time=False)

#A flat DataFrame
data_response.write().unstack().reset_index()