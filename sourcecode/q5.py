from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pandas as pd

#Reading dataset from the input file
dataset = pd.read_csv('./glass.csv')

#Handling null values and filling them with mean values of specific column
dataset = dataset.apply(lambda x: x.fillna(x.mean()),axis=0)

print(dataset.isnull().sum())

#Selecting the features
X_train = dataset.drop("Type",axis=1)
Y_train = dataset["Type"]

#Using train_test_split function for test data
X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.33, random_state=42)

#Gaussian
gaussian= GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred =gaussian.predict(X_test)
score = round(gaussian.score(X_test, y_test) * 100, 2)
print("GNB Accuracy",score)

#KNN
k1 = KNeighborsClassifier()
k1.fit(X_train, Y_train)
predicted = k1.predict(X_train)
print("KNN Accuracy:",round(k1.score(X_test, y_test) * 100, 2))

#SVM
s1 = SVC()
s1.fit(X_train, Y_train)
predicted = s1.predict(X_train)
print("SVM Accuracy:", round(s1.score(X_test, y_test) * 100, 2))
