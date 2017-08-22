import xlwings as xw



def excelToWeb ():
    wb = xw.Book('a.xlsx')
    sht = wb.sheets['Sheet1']
    numA = sht.range('B2').value
    numB = sht.range('C2').value
    return [numA, numB]


def webToExcel (number_1, number_2):
    wb = xw.Book('a.xlsx')
    sht = wb.sheets['Sheet1']
    sht.range('B5').value = number_1
    sht.range('C5').value = number_2


