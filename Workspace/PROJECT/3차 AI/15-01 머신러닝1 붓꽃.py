# 붓꽃 구별하기. 머신러닝 프로젝트1 --> Iris

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.utils import shuffle
import pandas as pd

'''
    준비
    0. 데이터 준비   : 학습용, 테스트용 => 지도학습(데이터 들, 레이블)
        훈련용, 학습용으로 분리 (8:2)

    1. 머신러닝 알고리즘 선택(Knn, SVM, 의사결정트리... + 딥러닝 가능)

    2. 학습데이터(80%)로 훈련시키기 => 오래 걸리는 작업 (좋은 컴퓨터 + GPU)
        ==> 모델이 완성됨  
    3. <모의고사>모델의 정답률(신뢰도) : 테스트용 데이터(20%) ==> 몇%가 일치한지 여부

    4. 정답을 모르는 데이터로 예측 해 보기 : 최종 목표
    
'''
df = pd.read_csv('iris.csv')
# df = utils.shuffle(df)
df = shuffle(df)

#훈련용, 학습용으로 분리
dataLen = df.shape[0]   # 데이터 프레임(엑셀 표)의 행 개수
print(dataLen)
studySize = int(dataLen * 0.8)
testSize = dataLen - studySize

study_data = df.iloc[0:studySize, 0:-1]
study_lable= df.iloc[0:studySize, [-1]]
print('study_data\n',study_data,'\n study_lable\n',study_lable)
test_data = df.iloc[studySize:, 0:-1]
test_lable= df.iloc[studySize:, [-1]]
# 1. 머신러닝 알고리즘 선택(Knn, SVM, 의사결정트리... + 딥러닝 가능)
clf = KNeighborsClassifier(n_neighbors=3)

# 2. 학습데이터(80%)로 훈련시키기 => 오래 걸리는 작업 (좋은 컴퓨터 + GPU)
#         ==> 모델이 완성됨
clf.fit(study_data, study_lable)

# 3. <모의고사>모델의 정답률(신뢰도) : 테스트용 데이터(20%) ==> 몇%가 일치한지 여부
# answers = 정답을 모르는 데이터로 예측 해 보기 : This is Fical goal
answers = clf.predict(test_data)
score = metrics.accuracy_score(answers, test_lable)*100
print('정답률 : %5.2f %%' % (score))

# 4. 정답을 모르는 데이터로 예측 해 보기 : 최종 목표
# 길을 걷다가 우연히 꽃을 하나 발견했다. 영롱한 빛이 나의 눈에 들어왔다.
# 줄자로 ㄲㅊ잎 두께, 꽃잎 길이, 줄기, 두께를 재봤다.
# 4.1, 3.3, 1.5, 0.2, 였다. 이게 무슨 붓꽃이지?
answers = clf.predict([[4.1, 3.3, 1.5, 0.2] ])
print('이 꽃은',answers,'입니다. 단',score,'%의 확률입니다.')