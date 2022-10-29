import joblib
clf = joblib.load('wineCheck.dmp')
print('Model Running Success\n',clf)
save = clf.predict([ [7.2,0.23,0.32,8.5,0.058,47,186,3.19,0.4,9.9,6] ])

print('This wind is ')