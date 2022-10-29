import xlrd

input_file = 'foundations/excel/sales_2013.xlsx'
workbook = xlrd.open_workbook(input_file)

totalSum = 0
print('시트 개수 : ',workbook.nsheets)
for ws in workbook.sheets() :
    print("워크시트 이름 :",ws.name,"   \t( 행:",ws.nrows,"열:",ws.ncols,")")