# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os



# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session



def predictfertilizerss(inp):
	df= pd.read_csv('data\\Fertilizer Prediction new.csv')
	df

	import seaborn as sns
	import matplotlib.pyplot as plt

	y=df['label']
	X=df.drop('label',axis=1)

	from sklearn.model_selection import train_test_split,GridSearchCV# splitting the data for training and testing
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=0)


	from sklearn.ensemble import RandomForestClassifier

	clf=RandomForestClassifier(n_estimators=20,max_depth=5,bootstrap=False,random_state=0)
	clf.fit(X_train,y_train)


	y_pred=clf.predict(X_test)


	# from sklearn import metrics

	# # Model Accuracy
	# print("Accuracy:", metrics.accuracy_score(y_pred, y_test))

	# from sklearn.model_selection import cross_val_score
	# print(cross_val_score(clf,X,y,cv=10).mean())


	# 
	print("ssdfdg",inp)
	checkss=inp

	y_pred=clf.predict(checkss)
	print(y_pred)
	return y_pred[0]




predictfertilizerss([[26,52,38,1,1,37,0,0]])