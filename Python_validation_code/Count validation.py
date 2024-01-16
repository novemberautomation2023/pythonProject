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

#Count validation script

def count_validation():
    dict_AWS = {}
    dict_CVP = {}
    error = ['']
    for i in Tables['TABLE_NAME']:
        try:
            dsn_tns_cvp = cx_Oracle.makedsn(Cvp_Host_name, Cvp_Port,
                                            service_name=Cvp_Service_name)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'.
            conn_cvp = cx_Oracle.connect(user=Cvp_User_name, password=Cvp_Password,
                                         dsn=dsn_tns_cvp)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
            curs_cvp = conn_cvp.cursor()
            query = r'select count(1) from FEDX_LSP.' + i
            curs_cvp.execute(query)
            for row in curs_cvp:
                # print("Number of records in CVP "+ " " +i,row)
                dict_CVP[i] = row
            cvp_data = pd.DataFrame(dict_CVP)
            conn_cvp.close()
            dsn_tns_aws = cx_Oracle.makedsn(Aws_Host_name, Aws_Port,
                                            service_name=Aws_Service_name)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'.
            conn_aws = cx_Oracle.connect(user=Aws_User_name, password=Aws_Password,
                                         dsn=dsn_tns_aws)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
            curs_aws = conn_aws.cursor()
            query = r'select count(1) from LSP.' + i
            curs_aws.execute(query)
            for row in curs_aws:
                # print("Number of records in AWS "+ " " +i,row)
                dict_AWS[i] = row
            aws_data = pd.DataFrame(dict_AWS)
            conn_aws.close()

        except:
            error.append(i)

    final_data = sqldf('select * from cvp_data union all select * from aws_data').T
    final_data = pd.DataFrame(final_data)
    final_data.reset_index(inplace=True)
    final_data.columns = ['Table_name', 'CVP_count', 'AWS_count']
    final_data.to_csv('final_data.csv', index=False)
    df = pd.read_csv('final_data.csv')
    data_compare = np.where(df['CVP_count'] == df['AWS_count'], 'Pass', 'Fail')
    final_data['Count_validation'] = data_compare
    file_name = "Count_Validation_Result" + "_" + str(np.random.randint(100, 1000)) + ".xlsx"
    path = str(os.getcwd())
    print('Pls check file under this path ' + path + ': ' + file_name)
    final_data.to_excel(file_name, index=False)

    error_tables = pd.DataFrame(error)
    os.chdir(r"C:\Users\ksreenivasulu\Canada Migration Automation\Table_validation")
    Error_file_name = "error" + "_" + file_name
    print('Pls check error cfile under this path ' + path + ': ' + Error_file_name)
    error_tables.to_excel(Error_file_name, index=False)
    print('Count validation is complete')
    # print('Table data validation will start')