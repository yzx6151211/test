import xlrd as xr
import xlwt as xw
from xlutils.copy import copy
data= xr.open_workbook('C:\\Users\\Administrator\\Desktop\\1.xls')

# table = data.sheets()[0]
# table = data.sheet_by_index(0)
table = data.sheet_by_name("sheet1")


cell = table.cell(1,1)
cell3 = cell.ctype
cell2 =table.cell_type(1,1)


workbook =copy(data)
worksheet = workbook.get_sheet('sheet1')

worksheet.write(1, 1, "memeda")
style = xw.XFStyle()


al = xw.Alignment()
al.horz = 0x02
al.vert = 0x01
style.alignment = al
worksheet.write_merge(0, 3, 0, 3, 'Second Merge',style)
workbook.save('C:\\Users\\Administrator\\Desktop\\2.xls')
