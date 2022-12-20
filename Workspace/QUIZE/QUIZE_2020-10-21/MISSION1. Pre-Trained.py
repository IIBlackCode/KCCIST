from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, svm
from sklearn.utils import shuffle
import pandas as pd

#0. 데이터를 준비 : 학습용, 테스트용 --> 지도학습 (데이터 들, 레이블(구분))
df = pd.read_csv('../winequality-red.csv') #csv파일 --> Dataframe
print(df) ##등급의 열이름, 데이터 행 수 :1599 / 데이터 열 수 : 12 확인
print(pd.np.unique(df['quality'])) ##등급의 개수를 확인 : 3~8까지 6개등급
df = shuffle(df) #데이터 프레임을 섞어준다 (학습용 테스트용으로 섞는다.)
# #0-1. 학습용과 테스트용으로 분리 (8:2)
datalen=df.shape[0] #데이터의 길이를 확인 : 1599
studySize = int(datalen*0.8) #학습용 데이터의 길이를 설정 0.8배수
testSize = datalen - studySize #테스트용 데이터의 길이를 설정 0.2배수

study_data = df.iloc[0:studySize, 0:-1] #답이 없는 데이터만
study_label = df.iloc[0:studySize,[-1]] #답만 따로 빼주기
test_data = df.iloc[studySize:, 0:-1] #답이 없는 데이터만
test_label = df.iloc[studySize:,[-1]] #답만 따로 빼주기

#1. 머신러닝 알고리즘 선택 (KNN / SVM / 의사결정트리 등 + 딥러닝도 가능)
# clf = KNeighborsClassifier(n_neighbors=3) ##KNN 알고리즘
clf = RandomForestClassifier(random_state=0) ##RandomForest 알고리즘

#2. 학습데이터(80%)로 훈련시키기 --> 오래걸리는 작업 (좋은 컴퓨터, GPU필요)
#   훈련 완료 --> 모델 완성!
clf.fit(study_data,study_label) ##Study_data를 label을 정답으로 학습시키기

#3.모델 정답률(신뢰도) 검증 (테스트용(20%) 데이터 사용)
answers = clf.predict(test_data)#answers라는 변수에 예측한 답을 넣고
score = metrics.accuracy_score(answers, test_label)*100 #정답률을 구하기 (%처리를 위해 100을 곱함)
print("정답률 : %5.2f %%" % (score))
#
#4. 정답을 모르는 데이터로 예측해 보기 : 최종 목표
# 꽐라가 된 상태로 길을 걷다가 누군가 나를 불러들어간 편의점
# 나를 부른 이는 바로 와인이었다. 나도 모르는 사이에 와인을 집어들고 나와
# 벌컥벌컥 마시다 가격을 보니 10만원이었다. 충격을 먹은 채 그대로 필름이 끊겨버렸다.
# 다음날 일어나 술이 깬 채로 어제의 나를 자책하며
# 나는 과연 합리적인 소비를 한 것인지 의문이 들어 와인의 등급을 알아보고 싶어졌다.
# 내가 마신 와인의 산도와 당도, 이산화황의 함유, 밀도와 알콜 도수는 다행히 나의 엄청난 혀로 판단이 가능했다
# 남은 와인을 탈탈 털어넣고 혀에 모든 감각을 집중하여 다음의 값을 구하였다.
# 1.fixed acid, 2.volitile acid, 3.citric acid, 4.residual sugar,
# 5.chlorides, 6.free sulfer dioxide, 7.total sulfer dioxide, 8.density, 9.pH, 10.sulphates, 11.alcohol
# 10.0 , 0.58, 0.03, 2.0, 0.075, 20, 30, 0.0997, 3.25, 0.58, 10.2
# 위와 같은 데이터가 나왔는데 내가 어제 10만원을 주고 산 와인은 과연 몇등급일까...
answer = clf.predict([ [10.0 , 0.58, 0.03, 2.0, 0.075, 20, 30, 0.0997, 3.25, 0.58, 10.2] ])
print("내가 마신 와인은",answer,"입니다. 단, ","%5.2f %%의 확률입니다." % (score))