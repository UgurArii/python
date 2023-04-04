import pandas as pd
import numpy as np

train = pd.read_csv('/root/Desktop/pythonTest/train.csv')
test = pd.read_csv('/root/Desktop/pythonTest/test.csv')

print(train[:4])
print(train.isnull().sum())
print(test.isnull().sum())
impute_value = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_value)
test['Age'] = test['Age'].fillna(impute_value)

train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)

predictors = ['Pclass','IsFemale','Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values
print(X_train[:5])
print(y_train[:5])

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
model = LogisticRegression()
print(model.fit(X_train, y_train))

y_predict = model.predict(X_test)
print(y_predict[:10])


#model_cv = LogisticRegressionCV(10)
#print(model_cv.fit(X_train, y_train))

from sklearn.model_selection import cross_val_score
model = LogisticRegression(C=10)
scores = cross_val_score(model, X_train, y_train, cv=4)
print(scores)
