import hashlib
import base64
import requests
import xlrd
book = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\副本a (2).xls')
sheet = book.sheet_by_name('Sheet1')
for i in range(sheet.nrows):
    row_values = sheet.row_values(i)
    mobiles = row_values[0]
    content = row_values[1]
    print(i)
    print(content)