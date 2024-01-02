
import pandas as pd
import logging

logging.basicConfig(filename="new.txt",level=logging.INFO,
                   format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='a')

#logger = logging.getLogger()


logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error")
logging.critical("this is critical")

def file_read(path,file_type):
    try:
        if file_type.upper()=='CSV':
            df= pd.read_csv(path)
            logging.info(f"file {path} read successfully")
        elif file_type.upper() =='JSON':
            df = pd.read_excel(path)
            logging.info(f"file {path} read successfully")
        else:
            print("enter correct file format")
        return df
    except:
        print("The provide file is not present in the location")
    finally:
        print("log out from fs")

source = file_read(path='/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info2.csv', file_type='csv')
target = file_read(path='/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info_t.csv', file_type='csv')
print(source)
print(target)









# import cx_Oracle
# try:
#     con=cx_Oracle.connect('scott/tiger@host.docker.internal')
#     cursor=con.cursor()
#     cursor.execute("create table employees(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))")
#     print("Table created successfully")
# except :
#     print("There is a problem with sql")
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()