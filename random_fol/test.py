import pandas as pd

source = pd.read_csv(r'/Users/harish/Downloads/archive (7)/portfolio.csv')
target = pd.read_csv(r'/Users/harish/Downloads/archive (7)/portfolio.csv')

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

source.grou



