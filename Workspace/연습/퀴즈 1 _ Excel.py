import csv

## Excel File 경로 저장
readFile1 = 'foundations/csv/sales_february_2014.csv'
readFile2 = 'foundations/csv/sales_january_2014.csv'
readFile3 = 'foundations/csv/sales_march_2014.csv'
readFilePath = [
                readFile1,
                readFile2,
                readFile3
            ]
writeFilePath = 'foundations/csv/sales_2014_total.csv'

# csvList = []

##  저장판 파일 경로를 통해 Excel파일 불러오기
# with open(readFile1, 'r') as rfp :
#     reader = csv.reader(rfp)
#     headList = next(reader)
#
#     for cList in reader :
#         csvList.append(cList)
#
# with open(readFile2, 'r') as rfp:
#     reader = csv.reader(rfp)
#     headList = next(reader)
#
#     for cList in reader:
#         csvList.append(cList)
#
# with open(readFile3, 'r') as rfp:
#     reader = csv.reader(rfp)
#     headList = next(reader)
#
#     for cList in reader:
#         csvList.append(cList)

for i in range(readFilePath) :
    with open(readFilePath[i], 'r') as rfp :
        reader = csv.reader(rfp)
        headList = next(reader)

    for cList in reader :
        csvList.append(cList)

headList = [ data.upper().strip() for data in headList]
print(headList)
pos = headList.index('SALE AMOUNT')

# for i in range(len(csvList)) :
#     row = csvList[i]
#     saleAmount = row[pos]
#     saleAmount = float(saleAmount[1:].replace(",",""))
#     saleAmount *= 1.15
#     saleAmountStr = "${0:.2f}".format(saleAmount)
#     csvList[i][pos] = saleAmountStr
#
# print(csvList)

with open(writeFilePath, mode='w', newline='') as wfp :
    writer = csv.writer(wfp)
    writer.writerow(tuple(headList))
    for row in csvList :
        writer.writerow(row)
        print(row)