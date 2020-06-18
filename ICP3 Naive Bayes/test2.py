import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC

train_df = pd.read_csv('./glass.csv')
test_df = pd.read_csv('./glass.csv')
X_train = train_df.drop("Type", axis=1)
Y_train = train_df["Type"]
X_test = test_df.drop("Type", axis=1).copy()
print(train_df[train_df.isnull().any(axis=1)])

X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.4, random_state=0)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# Implement linear SVM method using scikit library
svm = LinearSVC()
svm.fit(X_train, y_train)
print('Accuracy of Naive Bayes Linear SVM on training set: {:.2f}'.format(svm.score(X_train, y_train)))
# Evaluate the model on testing part
print('Accuracy of Naive Bayes Linear SVM on test set: {:.2f}'.format(svm.score(X_test, y_test)))

