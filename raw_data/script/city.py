#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import os
from tqdm import tqdm
import sys

#root_dir='/Users/zhanghang/bigdata/cs-gy-6513-big-data-project/raw_data/china_air_quality_historical_data'
root_dir=sys.argv[1]
target_dir=sys.argv[2]
data_list=['cities_20150101-20151231',\
        'cities_20160101-20161231',\
        'cities_20170101-20171231',\
        'cities_20180101-20181231',\
        'cities_20190101-20191231',\
        'cities_20200101-20201231',\
        'cities_20210101-20210320']

csv_list=[]
for cur_file in data_list:
    print(cur_file)
    cur_dir=root_dir+'/'+cur_file
    files=os.listdir(cur_dir)
    files=list(filter(lambda x: '.csv' in x and os.path.getsize(cur_dir+'/'+x)!=0 ,files))
    files.sort()
    for cur_file in tqdm(files):
        cur_path=cur_dir+'/'+cur_file
        df=pd.read_csv(cur_path)
        if '<html>' in df.columns:
            continue
        if '.swp' in cur_path:
            continue
            #with open('/Users/zhanghang/Downloads/record.txt','a') as mon:
            #    mon.write(cur_path+'\n')
            continue
        csv_list.append(df)

result = pd.concat(csv_list)
result = pd.DataFrame(result,columns=['date','hour','type','北京','天津','石家庄','大连','上海','南京','杭州','厦门','济南','武汉','广州','深圳'])
result.index = range(len(result))
#result.to_csv('/Users/zhanghang/Downloads/result1.csv')
result.to_csv(target_dir+'/'+'cities_merge_all.csv')





