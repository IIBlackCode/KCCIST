'''
    퀴즈1. 와인의 품질 고르기.
    
    1. 캐글 데이터셋 : https://www.kaggle.com/datasets
    학습, 훈련용 %를 조절...
    알고리즘을 변경
    clf = KNeighborsClassifier(n_neighbors=3) # 숫자를 변경해보자(단, 홀수로)
    clf = svm.SVC(gamma='auto')

    2. 서울 열린 데이터 광장
    데이터셋을 공개

    정답률 구해보기
    
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, svm
from sklearn.utils import shuffle
import pandas as pd

df = pd.read_csv('DATA/winequality-red.csv')
df = shuffle(df)

#훈련용, 학습용으로 분리
dataLen = df.shape[0]   # 데이터 프레임(엑셀 표)의 행 개수 : 1599
studySize = int(dataLen * 0.12)     #1408
testSize = dataLen - studySize      #191
print('dataLen : ',dataLen,' testSize:',testSize, ' studySize:',studySize)


study_data = df.iloc[0:studySize, 0:-1]
study_lable= df.iloc[0:studySize, [-1]]
print('study_data\n',study_data,'\n study_lable\n',study_lable)

test_data = df.iloc[studySize:, 0:-1]
test_lable= df.iloc[studySize:, [-1]]
print('test_data\n',test_data,'\n test_lable\n',test_lable)
# 1. 머신러닝 알고리즘 선택(Knn, SVM, 의사결정트리... + 딥러닝 가능)
# clf = KNeighborsClassifier(n_neighbors=3)
# print(clf)
clf = svm.SVC(gamma='auto')
print(clf)

# 2. 학습데이터(80%)로 훈련시키기 => 오래 걸리는 작업 (좋은 컴퓨터 + GPU)
#         ==> 모델이 완성됨
print("데이터 학습")
clf.fit(study_data, study_lable)

# 3. <모의고사>모델의 정답률(신뢰도) : 테스트용 데이터(20%) ==> 몇%가 일치한지 여부
# answers = 정답을 모르는 데이터로 예측 해 보기 : This is Fical goal
answers = clf.predict(test_data)
print('answers:',answers)
score = metrics.accuracy_score(answers, test_lable)
print('score:',score)
print('정답률 : %5.2f %%' % (score*100))

# 4. 정답을 모르는 데이터로 예측 해 보기 : 최종 목표
# 길을 걷다가 우연히 꽃을 하나 발견했다. 영롱한 빛이 나의 눈에 들어왔다.
# 줄자로 꽃잎 두께, 꽃잎 길이, 줄기, 두께를 재봤다.
# 4.1, 3.3, 1.5, 0.2, 였다. 이게 무슨 붓꽃이지?
# answers = clf.predict([[4.1, 3.3, 1.5, 0.2] ])
answer = clf.predict([ [10.0 , 0.58, 0.03, 2.0, 0.075, 20, 30, 0.0997, 3.25, 0.58, 10.2] ])
print('이 꽃은',answers,'입니다. 단',score,'%의 확률입니다.')