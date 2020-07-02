import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.preprocessing import StandardScaler


# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = pd.read_csv("BresC.csv")
X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values

from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)



X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size= .25, random_state= 0)

my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=30, activation='relu'))  # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
