
import pandas as pd
date =  pd.read_excel(r'C:\\Users\\Administrator\\Desktop\\1\\1.xls',converters={"a":str,"b":str,"c":str,"d":str,"e":str})# C:\\Users\\Administrator\\Desktop\\1.xls
print(date)
#print(date.columns)
un = date['村'].unique()
for a in un:
    print(a)
    date_xin = date[date.村 == a]
    date_xin.set_index('序号')

    date_xin["序号"] = range(1, len(date_xin) + 1)
    print(date_xin.head())

    date_xin.to_excel('C:\\Users\\Administrator\\Desktop\\新建文件夹 (6)\\'+a+"_"+str(len(date_xin))+".xlsx", sheet_name='sheet1', index=None, encoding="gbk")




