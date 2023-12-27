import pandas as pd

from Functions.functions_patt1 import factorial2,result2
source = pd.read_csv(r'/Users/harish/Desktop/ETL Automation/Contact_info.csv')
target = pd.read_csv(r'/Users/harish/Desktop/ETL Automation/Contact_info_t.csv')

print(source.columns)
print(source.shape[0])
print(source.shape[0])

def count_val(sourcedf, targetdf):
    source_cnt = source.shape[0]
    target_cnt =  target.shape[0]
    if source_cnt == target_cnt:
        print("Count is matching")
    else:
        print("Count is not matching and difference is", abs(source_cnt-target_cnt))

count_val(source, target)

def data_val(sourcedf, targetdf):
    print(sourcedf.compare(targetdf))

data_val(source, target)






