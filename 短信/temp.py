from openpyxl import load_workbook
import datetime
workbook1 = load_workbook(('C:\\Users\\Administrator\\Desktop\\a - 副本.xlsx'))
sheet = workbook1['Test2']
sheet.title = '2'
workbook1.save('C:\\Users\\Administrator\\Desktop\\a - 副本.xlsx')