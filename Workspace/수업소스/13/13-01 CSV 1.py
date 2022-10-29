#2020-10-19 빅데이터 플랫폼

#IMPORT
import csv

##우리회사 평균 연봉은?
# filename = '/foundations/csv/supplier_data.csv'
filename = 'foundations/csv/supplier_data.csv'
with open(filename,'r') as rfp :
    reader = csv.reader(rfp)
    headerList = next(reader)
    print(headerList)

    sum = 0
    count = 0
    for cList in reader :
        sum += int(float(cList[3][1:]))
        count +=1
    avg = sum // count
    print('평균 연봉 : ',avg)