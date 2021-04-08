import win32com.client


def get_sheetpw(xls, filename, password):
    try:
        xlsheet = xls.Workbooks.Open(filename, False, True, None, Password=password)
        print('破解成功!')
        print("文档密码是：{}".format(password))
        xlsheet.Close()
        return True
    except:

        return False


if __name__ == '__main__':
    xls = win32com.client.Dispatch("Excel.Application")
    xls.DisplayAlerts = 0
    p = 0
    print('破解中......')

    while True:

        isdone = get_sheetpw(xls, r'C:\\Users\\Administrator\\Desktop\\23.xlsx', p)
        p = p + 1
        print(p)
        if isdone:
            break