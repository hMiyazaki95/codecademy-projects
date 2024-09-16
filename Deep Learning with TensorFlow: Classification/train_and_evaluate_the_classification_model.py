'''

model
5 min
To train a model instance my_model on the training data my_data and training labels my_labels we do the following:

my_model.fit(my_data, my_labels, epochs=10, batch_size=1, verbose=1)

With the command above, we set the number of epochs to 10 and the batch size to 1. To see the progress of the training we set verbose to true (1).

After the model is trained, we can evaluate it using the unseen test data my_test and test labels test_labels:

loss, acc = my_model.evaluate(my_test, test_labels, verbose=0)

We take two outputs out of the .evaluate() function:

the value of the loss (categorical_crossentropy)
accuracy (as set in the metrics parameter of .compile()).


my_data: This represents the input features of your training dataset. These are the variables used to make predictions.

my_labels (goal): These are the target values or labels corresponding to the input features in my_data. They are what the model aims to predict.

epochs=10: This means the model will go through the entire training dataset 10 times. Each complete pass through the dataset is called an epoch.

batch_size=1: This specifies the number of training examples used in one iteration before updating the model’s weights. A batch size of 1 means the model updates its weights after each training example.

verbose=1: This controls the verbosity of the training process. A value of 1 means progress messages will be displayed during training, showing the progress of each epoch.
'''


import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  InputLayer
from tensorflow.keras.layers import  Dense
#your code here

train_data = pd.read_csv("air_quality_train.csv")
test_data = pd.read_csv("air_quality_test.csv")

#print columns and their respective types
print(train_data.info())
#print the class distribution
print(Counter(train_data["Air_Quality"]))
#extract the features from the training data
x_train = train_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]
#extract the label column from the training data
y_train = train_data["Air_Quality"]
#extract the features from the test data
x_test = test_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]
#extract the label column from the test data
y_test = test_data["Air_Quality"]

#encode the labels into integers
le = LabelEncoder()
#convert the integer encoded labels into binary vectors
y_train=le.fit_transform(y_train.astype(str))
y_test=le.transform(y_test.astype(str))
#convert the integer encoded labels into binary vectors
y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

#design the model
model = Sequential()
#add the input layer
model.add(InputLayer(input_shape=(x_train.shape[1],)))
#add a hidden layer
model.add(Dense(10, activation='relu'))
#add an output layer
model.add(Dense(6, activation='softmax'))

#compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#train and evaluate the model
model.fit(x_train, y_train, epochs=20, batch_size=4, verbose=1)
