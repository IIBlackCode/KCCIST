'''
    퀴즈1. CSV 폴더의 sales_????_2014.csv 파일 3개를
    sales_2014_total.csv에 합쳐서 저장한다.
    단, Sales Amount는 가격을 15% 인상시킨다.
'''

import csv
import xlrd

fileName1 = '/foundations/csv/sales_february_2014.csv'
fileName2 = '/foundations/csv/sales_january_2014.csv'
fileName3 = '/foundations/csv/sales_march_2014.csv'
sales_2014_total = 'foundations/csv/sales_2014_total.csv'

read1_workbook = xlrd.open_workbook(fileName1)
read2_workbook = xlrd.open_workbook(fileName2)
read3_workbook = xlrd.open_workbook(fileName3)

totalSum = 0
print('시트 개수 : ',read1_workbook.nsheets)
# for ws in workbook.sheets() :
#     # print("워크시트 이름 :",ws.name,"   \t( 행:",ws.nrows,"열:",ws.ncols,")")
#     sheetSum = 0
#     for i in range(1,ws.nrows) :
#         for j in range(0,ws.ncols) :
#             print(ws.cell_value(i,j), end='\t')
#             if j == 3 :
#                 ##연봉 10% 상승
#                 sheetSum += (ws.cell_value(i,j)*1.1)
#         print()
#     print('<<',ws.name, ':',sheetSum,'>>')
#     totalSum += sheetSum
# print('Total Sum :',totalSum)