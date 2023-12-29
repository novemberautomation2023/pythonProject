import pandas as pd

from Functions.functions_patt1 import factorial2,result2
source = pd.read_csv(r'/Users/harish/Desktop/ETL Automation/Contact_info.csv')
target = pd.read_csv(r'/Users/harish/Desktop/ETL Automation/Contact_info_t.csv')

print(source.head(2))
print(source.columns)
print(source.shape[0])
print(source.shape[1])

print(target.columns)
print(target.shape[0])
print(target.shape[1])
#
def count_val(sourcedf,targetdf):
    source_cnt = source.shape[0]
    target_cnt =  target.shape[0]
    if source_cnt == target_cnt:
        print("Count is matching")
    else:
        print("Count is not matching and difference is", source_cnt-target_cnt)
    return source_cnt,target_cnt

src_cnt,tgt_cnt = count_val(sourcedf= source, targetdf = target)
print("#"*30)
print(src_cnt)
print(tgt_cnt)


print("#"*30)
def data_val(sourcedf, targetdf):
    print(sourcedf.compare(targetdf))

data_val(source, target)
#
#




