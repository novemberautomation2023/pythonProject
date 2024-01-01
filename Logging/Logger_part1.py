'''This file created to practice functions
Author - Sreeni added date:26/Dec/2023 '''

#Levels of logging
#
# 1. Notset ( Level code - 0 )
# 2. Debug ( Level code - 10 )
# 3. info ( Level code - 20 )
# 4. warning ( Level code - 30 )
# 5. error ( Level code - 40 )
# 6. critical ( Level code - 50 )

import logging

import pandas as pd
logging.basicConfig(filename='logger_part1.txt',level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s')
# Default level set is Warning( 30 )
# logging.debug("This is debug logger")
# logging.info("This is info logger")
# logging.warning("This is warning logger")
# logging.error("This is error logger")
# logging.critical("This is critical logger")
# logging.info("This is info2 logger")
# logging.error("This is error2 logger")

#print("This is debug logger")
# #print("This is info logger")
# print("This is warning logger")
# #print("This is error logger")
# print("This is critical logger")

def read_file(path, file_type):
    try:
        if file_type == 'csv':
            df = pd.read_csv(path)
            rows = df.shape[0]
            print("CSV file read successfully", path)
            logging.info(f"CSV file read successfully {path} and rows read is {rows}")
        elif file_type == 'excel':
            df = pd.read_excel(path)
            print(" excel file read successfully", path)
            logging.info(f"excel file read successfully +{path}")
        elif file_type == 'json':
            df = pd.read_json(path)
            print(" json file read successfully", path)
            logging.info(f"json file read successfully +{path}")
        else:
            pass
        return df
    except:
        error_files = []
        error_files.append(path)
        print(error_files)
        logging.critical("File is not present")
        #df =  df = pd.read_csv(path)

df = read_file("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv","csv")
print(df.head(2))

df2 = read_file("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info_t.csv","csv")
print(df2.head(2))



