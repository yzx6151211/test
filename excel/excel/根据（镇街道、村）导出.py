
import pandas as pd
import os
# converter = {}
# column_number = ""
# while True:
#     x = input("请输入您要导出为文本的列（第一行标题,多列）名称，结束请输入“结束”：")
#     column_number=column_number+x+"、"
#     print("要转出为文本的列为"+column_number)
#     if x !="结束":
#         converter[x] = str
#     else:
#         break
#
# date =  pd.read_excel(r'temp.xlsx',converters=converter)

date =  pd.read_excel(r'temp.xlsx',converters={'社会保障号':str,'银行账号':str,'行号':str,'行号':str,'人员编码':str})# C:\\Users\\Administrator\\Desktop\\1.xls
print(date)
print(date.columns)
unzhen = date['镇街道'].unique() # 列表，所有镇街道的名称
for i in unzhen: # 先按镇街道筛选

    os.mkdir(i)
    date_zhen = date[date.镇街道 == i]
    un = date_zhen['村'].unique() # 列表，所有村名称

    for a in un: #再按村筛选
        print(a)


        date_xin = date_zhen[date.村 == a]
        print(date.镇街道)
        date_xin.set_index('序号')

        date_xin["序号"] = range(1, len(date_xin) + 1)
        print(date_xin.head())

        date_xin.to_excel(i+'\\'+a+"_"+str(len(date_xin))+".xlsx", sheet_name='sheet1', index=None, encoding="gbk")




