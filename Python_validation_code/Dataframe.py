import pandas as pd

from pandasql import sqldf

df=pd.read_csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")

print(df.head(2))
print(df.tail(2))
print(df.describe())

source=pd.read_csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
target = pd.read_csv("/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info_t.csv")

def count_val(source, target):
    src_cnt = sqldf("select count(*) count1 from source")
    #src_cnt = source.shape[0]
    #tgt_cnt = target.shape[0]
    tgt_cnt = sqldf("select count(*) count1 from target")
    if list(src_cnt.count1) == list(tgt_cnt.count1):
        print("matching")
    else:
        print("count validation failed", src_cnt-tgt_cnt)

def Column_value_val(source, target):
    Mismatch_S_T = sqldf("select *  from source except select *  from target")
    Mismatch_T_S = sqldf("select *  from target except select *  from source")
    print("Mismatch records between source and target")
    print(Mismatch_S_T)
    print("Mismatch records between target and source")
    print(Mismatch_T_S)
    source

Column_value_val(source, target )

def duplicate(target, key_colum ):
    duplicate = sqldf(f'''select key_column, count(*)  from target"
                       group by key_column having count(*)>1''')
    if duplicate.shape[0]>0:
        print("duplicates")
    else:
        print("no duplicates")
duplicate(target,'identifier')


