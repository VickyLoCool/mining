import xlrd
import jieba.posseg as pseg
import re
import numpy as np

def is_chinese(word):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    if pattern.search(word):
        return False
    return True


xlrd.Book.encoding='utf-8'
df=xlrd.open_workbook('data.xlsx')
table=df.sheets()[4]
print(table.nrows)
diag=[]
dict1={}
hospital=set()
for i in range(1,table.nrows):
    hos=str(table.cell(i,7))
    if hos in hospital:
        continue
    hospital.add(hos)
    dict1[hos]=str(table.cell(i,0))
np.save('hospital.npy',dict1)
