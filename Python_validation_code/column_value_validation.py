import pandas as pd
import cx_Oracle
from pandasql import sqldf
import os
import numpy as np
from datetime import datetime

#Reading tables

dsn_tns_cvp = cx_Oracle.makedsn(Cvp_Host_name, Cvp_Port, service_name=Cvp_Service_name) #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
conn_cvp = cx_Oracle.connect(user=Cvp_User_name, password=Cvp_Password, dsn=dsn_tns_cvp) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
curs_cvp = conn_cvp.cursor()
query=r'''select distinct table_name from all_tab_cols where  owner='FEDX_LSP' and  column_name not like 'SYS%'
and table_name  in ('TRN_SUSPENSE','TRN_DETAIL')'''
curs_cvp.execute(query)
columns=[desc[0] for desc in curs_cvp.description]
data=curs_cvp.fetchall()
Tables=pd.DataFrame(list(data),columns=columns)

def table_data_validation():
    Table_error = []
    for i in Tables['TABLE_NAME'].head(100):
        try:
            dsn_tns_cvp = cx_Oracle.makedsn(Cvp_Host_name, Cvp_Port,
                                            service_name=Cvp_Service_name)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'.
            conn_cvp = cx_Oracle.connect(user=Cvp_User_name, password=Cvp_Password,
                                         dsn=dsn_tns_cvp)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
            curs_cvp = conn_cvp.cursor()
            query = r'select * from FEDX_LSP.' + i + ' where rownum<100000 order by 1,2,3'
            print(query)
            curs_cvp.execute(query)
            columns = [desc[0] for desc in curs_cvp.description]
            data = curs_cvp.fetchall()
            df_cvp_schema = pd.DataFrame(list(data), columns=columns)
            conn_cvp.close()
            dsn_tns_aws = cx_Oracle.makedsn(Aws_Host_name, Aws_Port,
                                            service_name=Aws_Service_name)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'.
            conn_aws = cx_Oracle.connect(user=Aws_User_name, password=Aws_Password,
                                         dsn=dsn_tns_aws)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
            curs_aws = conn_aws.cursor()
            query = r'select * from LSP.' + i + ' where rownum<100000 order by 1,2,3'
            curs_aws.execute(query)
            columns = [desc[0] for desc in curs_aws.description]
            data = curs_aws.fetchall()
            df_AWS_schema = pd.DataFrame(list(data), columns=columns)
            conn_aws.close()
            df_AWS_schema.fillna(0, inplace=True)
            df_cvp_schema.fillna(0, inplace=True)
            dict = {}
            for k in df_AWS_schema.columns:
                for l in df_cvp_schema.columns:
                    if k == l:
                        dict[k] = np.where(df_AWS_schema[k] == df_cvp_schema[l], True, False)
                        # print(dict)
            table_comapre = pd.DataFrame(dict)
            file_name = "tables" + "_" + i + ".xlsx"
            print(file_name)
            os.chdir(r"C:\Users\ksreenivasulu\Canada Migration Automation\Table_validation")
            writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
            df_AWS_schema.to_excel(writer, sheet_name='df_AWS_schema')
            df_cvp_schema.to_excel(writer, sheet_name='df_cvp_schema')
            table_comapre.to_excel(writer, sheet_name=i)
            writer.save()
        except:
            ls.append(i)
    df = pd.DataFrame(Table_error)
    os.chdir(r"C:\Users\ksreenivasulu\Canada Migration Automation\Table_validation")
    df.to_csv('error.csv')


