'''
Designing a deep learning model for classification
11 min
To initialize a Keras Sequential model in TensorFlow, we do the following:

from tensorflow.keras.models import Sequential
my_model = Sequential()

The process is the following:

set the input layer
set the hidden layers
set the output layer.
To add the input layer, we use keras.layers.InputLayer the following way:

from tensorflow.keras.layers import  InputLayer
my_model.add(InputLayer(input_shape=(data_train.shape[1],)))

For now, we will only add one hidden layer using keras.layers.Dense:

from tensorflow.keras.layers import  Dense
my_model.add(Dense(8, activation='relu'))

This layer has eight hidden units and uses a rectified linear unit (relu) as the activation function.

Finally, we need to set the output layer. For regression, we don’t use any activation function in the final layer because we needed to predict a number without any transformations. However, for classification, the desired output is a vector of categorical probabilities.

To have this vector as an output, we need to use the softmax activation function that outputs a vector with elements having values between 0 and 1 and that sum to 1 (just as all the probabilities of all outcomes for a random variable must sum up to 1). In the case of a binary classification problem, a sigmoid activation function can also be used in the output layer but paired with the binary_crossentropy loss.

Since we have 3 classes to predict in our glass production data, the final softmax layer must have 3 units:

my_model.add(Dense(3, activation='softmax')) #the output layer is a softmax with 3 units

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
#initialize the model
model = Sequential()

#add the input layer
model.add(InputLayer(input_shape=(x_train.shape[1],)))

#add a hidden layer
model.add(Dense(10, activation='relu'))

#add an output layer
model.add(Dense(6, activation='softmax'))




