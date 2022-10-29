import xlrd
import xlwt

input_file = 'foundations/excel/sales_2013.xlsx'
out_file = 'foundations/excel/sales_2013_out.xls'

read_Workbook = xlrd.open_workbook(input_file)
write_Workbook = xlwt.Workbook()
for rWs in read_Workbook.sheets() :
    wWs = write_Workbook.add_sheet(rWs.name)
    for i in range(0,rWs.nrows) :
        for j in range(0,rWs.ncols) :
            wWs.write(i,j,rWs.cell_value(i,j))
            print(rWs.cell_value(i,j), end='\t')
        print()
write_Workbook.save(out_file)