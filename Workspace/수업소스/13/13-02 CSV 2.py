## 연봉을 10% 인상시켜 저장

import csv


# filename = '/foundations/csv/supplier_data.csv'
rFname = 'foundations/csv/supplier_data.csv'
wFname = 'foundations/csv/supplier_data2.csv'

csvList = []
with open(rFname,'r') as rfp :
    reader = csv.reader(rfp)
    headerList = next(reader)
    print(headerList)

    sum = 0
    count = 0
    for cList in reader :
        csvList.append(cList)

## 월급의 열 이름 : COST
# COST가 몇번째 열인지 찾기
            #data를 대문자로.공백삭제
headerList = [ data.upper().strip() for data in headerList]
print(headerList)

#COST가 몇번째 열인지 반환
strIndex = headerList.index('COST')
print(strIndex)
for i in range(len(csvList)) :
    row = csvList[i]
    cose = row[strIndex]
    cose = float(cose[1:])
    cose *= 15
    coseStr = "${0:.2f}".format(cose)
    csvList[i][strIndex] = coseStr

print(csvList,'\n')

## Save Result
with open(wFname, mode='w', newline='') as wfp :
    writer = csv.writer(wfp)
    writer.writerow(tuple(headerList))
    print(row)
    for row in csvList :
        writer.writerow(row)
        print(row)
