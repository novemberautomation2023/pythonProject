import pandas as pd
import cx_Oracle
from pandasql import sqldf
import os
import numpy as np
from datetime import datetime

#Source columns
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='freepdb1') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
conn = cx_Oracle.connect(user=r'scott', password='tiger', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
curs = conn.cursor()
query='''select table_name, column_name, data_type, data_length,nullable from all_tab_cols '''
curs.execute(query)
columns=[desc[0] for desc in curs.description]
data=curs.fetchall()
df_cvp_schema=pd.DataFrame(list(data),columns=columns)
conn.close()


#target schem
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='U4FEDX') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
conn = cx_Oracle.connect(user=r'scott', password='tiger', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
curs = conn.cursor()
query='''select table_name, column_name, data_type, data_length,nullable from all_tab_cols where owner='LSP'
and  column_name not like 'SYS%' and  table_name not in ('MBR_FED_ENTRY_OFFERS_TMP','RPT_PERIOD_VW')
 order by 1,2,3,4'''
curs.execute(query)
columns=[desc[0] for desc in curs.description]
data=curs.fetchall()
df_AWS_schema=pd.DataFrame(list(data),columns=columns)
conn.close()

#Validation

df_comparison=pd.DataFrame()
df_comparison['TABLE_NAME']=np.where(df_AWS_schema['TABLE_NAME']==df_cvp_schema['TABLE_NAME'],True, False)
df_comparison['COLUMN_NAME']=np.where(df_AWS_schema['COLUMN_NAME']==df_cvp_schema['COLUMN_NAME'],True, False)
df_comparison['DATA_TYPE']=np.where(df_AWS_schema['DATA_TYPE']==df_cvp_schema['DATA_TYPE'],True, False)
df_comparison['DATA_LENGTH']=np.where(df_AWS_schema['DATA_LENGTH']>=df_cvp_schema['DATA_LENGTH'],True, False)
df_comparison['NULLABLE']=np.where(df_AWS_schema['NULLABLE']>=df_cvp_schema['NULLABLE'],True, False)


