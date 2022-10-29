#파일 열기 --> 파일 읽기/쓰기 --> 파일 닫기

#파일 열기
rfp = open('c:/windows/win.ini','r');   #1
#파일 쓰기
wfp = open('win2.txt','w');

line = rfp.readline();
print(line,end='');
line = rfp.readline();
print(line,end='');
line = rfp.readline();
print(line,end='');

while True :
    line = rfp.readline();
    if (line is None or line == '') :
        break;
    print(line, end='');
    wfp.writelines(line);

#파일 닫기
rfp.close()                             #3
#파일을 먼저 열어주고 닫는다.
wfp.close()                             #