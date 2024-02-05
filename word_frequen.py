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
df=xlrd.open_workbook('result.xlsx')
table=df.sheets()[0]
print(table.nrows)
diag=[]
s=set()
for i in range(1,table.nrows):
    diag.append(table.cell(i,37).value.replace('\n','').replace('\r','').replace('\t',''))
    print(table.cell(i,37).value)
print('---')
print(diag)
print('---')
for d in diag:
    words=pseg.lcut(d)
    for w in words:
        if len(w.word)==1:
            continue
        if not w.word.isnumeric() and is_chinese(w.word) and w.flag=='n':
            s.add(w.word)
answ=list(s)
print(s)
f=open('1.txt','w')
for one in answ:
    f.write(one+'\n')
f.close()
