from datetime import datetime

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.engine.saving import model_from_yaml
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from matplotlib import pyplot
import pandas.plotting._matplotlib
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re
import pickle
from keras.callbacks import TensorBoard
from sklearn.preprocessing import LabelEncoder


# load and create model
yaml_file = open('model1.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model1.h5")
print("Loaded model from disk")


loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

new_string = "A lot of good things are happening. We are respected again throughout the world, " \
             "and that's a great thing.@realDonaldTrump"
new_string = [[new_string]]
max_df = pd.DataFrame(new_string, index=range(0, 1, 1), columns=list('t'))

max_df['t'] = max_df['t'].apply(lambda x: x.lower())
max_df['t'] = max_df['t'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))
print(max_df)

max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(max_df['t'].values)
X = tokenizer.texts_to_sequences(max_df['t'].values)
X = pad_sequences(X, maxlen=28)

print(loaded_model.predict(X))
print("====== the input vector")
print(X)
