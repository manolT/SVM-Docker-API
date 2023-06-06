import pickle

from joblib import load

from sklearn import datasets, svm

SVM = svm.SVC()
X, y = datasets.load_iris(return_X_y=True)
SVM.fit(X, y)
print(SVM.predict([[20, 1, 0, 2000]]))
s = pickle.dumps(SVM)

text_file = open("svm.ml", "wb")
n = text_file.write(s)
text_file.close()

SVM = load('svm.ml')
print(SVM.predict([[2, 0, 0, 1]]))