import xlrd

input_file = 'foundations/excel/sales_2013.xlsx'
workbook = xlrd.open_workbook(input_file)

totalSum = 0
print('시트 개수 : ',workbook.nsheets)
for ws in workbook.sheets() :
    # print("워크시트 이름 :",ws.name,"   \t( 행:",ws.nrows,"열:",ws.ncols,")")
    sheetSum = 0
    for i in range(1,ws.nrows) :
        for j in range(0,ws.ncols) :
            print(ws.cell_value(i,j), end='\t')
            if j == 3 :
                ##연봉 10% 상승
                sheetSum += (ws.cell_value(i,j)*1.1)
        print()
    print('<<',ws.name, ':',sheetSum,'>>')
    totalSum += sheetSum
print('Total Sum :',totalSum)