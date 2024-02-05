import numpy as np
import xlrd
import jieba.posseg as pseg
import re
import numpy as np

def is_chinese(word):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    if pattern.search(word):
        return False
    return True

f=open('1.txt','r')
words=f.readlines()
words=[w.replace('\n','') for w in words]
load_dict=np.load('hospital.npy',allow_pickle=True).item()
xlrd.Book.encoding='utf-8'
df=xlrd.open_workbook('result.xlsx')
table=df.sheets()[0]
print(table.nrows)
diag=[]
dict1={}
s=set()
for i in range(2,table.nrows):
    hospital=str(table.cell(i,4))
    if not hospital in load_dict.keys():
        continue
    district=load_dict[hospital]
    if not district in dict1.keys():
        dict1[district]={}
    judge=str(table.cell(i,37))
    for w in words:
        if w in judge:
            if w in dict1[district].keys():
                dict1[district][w]+=1
            else:
                dict1[district][w]=1
np.save('hospi.npy',dict1)