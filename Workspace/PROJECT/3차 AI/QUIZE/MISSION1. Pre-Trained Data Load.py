'''
제목 : [머신러닝] Iris, Pre-Rained 데이터
(1)Pre-Trained 데이터 생성하기
-자신의 데이터 셋 찾기 :Ex) Iris, MNIST 제외...
- *.cvs 설명
    --데이터 셋의 개요 : 봄꽃의 종류를 예측하기
    --각 열의 의미
        1~4열(데이터)   : 꽃잎폭, 꽃잎두께
        5열(레이블)     : 3개(세토라, 버지니카, 버지니아)
    --epdlxj godtn : 150행
- 훈련시킨 알고리즘 : knn, SVM.. --> 여러개 테스트
- 모델의 정확도(신뢰도) :96.33%
- 모델을 덤프한 파일 : *.dmp
- 예측해본 정답이 없는 데이터 : [4.1,3.3,1.5,0.2]
==>카페에 업로드: 뒤 정보 + 데이터파일(*.cvs) + 프리트랜드인덤프(*.dmp)

(2) 심화 : 다른사람의 Pre-Trained데이터로 머신러닝 확인해 보기기
'''
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC, SVR, NuSVC, NuSVR
# from sklearn import utils, metrics, svm
# from sklearn.utils import shuffle
# import pandas as pd

# # 1. 데이터 파일 불러오기
# dataFile = pd.read_csv('../DATA/winequalityN4.csv',encoding="UTF-8")
# dataFile.fillna(0)
#
# # 2. 데이터 파일의 데이터 총 갯수[0번째 인덱스의 갯수]
# dataLine = dataFile.shape[0]
#
# # 3. 학습용 데이터 : 테스트 데이터 = 8:2 라인 갯수 구하기
#     #학습용 데이터
# study_DataLine = int(dataLine*0.8)
#     #테스트용 데이터
# test_DataLine = dataLine-study_DataLine
# print('총 데이터:',dataLine,' 훈련용 :',study_DataLine,' 테스트용:',test_DataLine)
#
# # 4. 학습용 데이터 와 테스트용 데이터를 구한 싸이즈만큼 분리
#     #(1) 데이터가 같은이름으로 뭉쳐있는 부분이 있어 섞어주었다.
#     # *tip : import를 random으로 받으면 Error 발생함으로 주의
# dataFile = shuffle(dataFile)
#
#     #(2) -1 기존 데이터에서 80%의 데이터를 학습용으로 저장
# study_data = dataFile.iloc[0:study_DataLine, 0:-1]
#     #(2) -2 학습용 데이터의 마지막 행 부분을 라벨로 지정
# study_lable= dataFile.iloc[0:study_DataLine, [-1]]
#
#     #(3) -1 기존 데이터에서 나버지 20%의 데이터를 학습용으로 저장
# test_data = dataFile.iloc[test_DataLine:, 0:-1]
#     #(4) -2 학습용 데이터의 마지막 행 부분을 라벨로 지정
# test_lable= dataFile.iloc[test_DataLine:, [-1]]
# print('study_data\n',study_data,'\n study_lable\n',study_lable)
#
# # 5. 머신러닝 알고리즘을 통해 학습용 데이터를 학습시킨다.
# # 머신러닝 = KNeighborsClassifier(n_neighbors=3).fit(study_data,study_lable)
# 머신러닝 = svm.SVC(gamma='auto').fit(study_data,study_lable)
#
# # 6. 테스트 데이터를 통해 정확도를 확인한다.
# testResult = 머신러닝.predict(test_data)
#
#
# # print(testResult)
#
# findLable = metrics.accuracy_score(testResult,test_lable)
# print('테스트 데이터와 비교했을 때 정확도: %5.2f %%' % (findLable*100))
#
# # 7. 정답을 모르는 데이터로 예측 해 보기 : 최종 목표
# #9.7,0.53,0.6,2,0.039,5,19,3.3,0.86,12.4,6,red
# tempData = 머신러닝.predict([ [8,0.1,0.1,2,1,1,19,4,1,10.5,7] ])
# print('이 와인은',tempData,'입니다. 단',findLable,'%의 확률입니다.')
#
# # 8. 모델 덤프
# import joblib
# joblib.dump(dataFile, 'wineCheck.dmp')
# print('save')

# 9. 덤프모델 로딩
import joblib
clf = joblib.load('../wineCheck.dmp')
print('Model Running Success')

# 10. 정답을 모르는 데이터로 예측
answer = clf.predict([[8,0.1,0.1,2,1,1,19,4,1,10.5,7]])


print('이 글은', answer, ' 입니다.')
