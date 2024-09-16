'''
1.
Using the # symbol for comments, comment out the following lines of code (Line 36 and Line 37):

y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

Checkpoint 2 Passed
2.
Modify the existing code on the right by changing the model.compile() method to use sparse_categorical_crossentropy as loss. Run the code.

Note: Running this in the LE will take almost a full minute!

Classification loss alternative: sparse crossentropy
6 min
As we saw before, categorical cross-entropy requires that we first integer-encode our categorical labels and then convert them to one-hot encodings using to_categorical(). There is another type of loss – sparse categorical cross-entropy – which is a computationally modified categorical cross-entropy loss that allows you to leave the integer labels as they are and skip the entire procedure of encoding.

Sparse categorical cross-entropy is mathematically identical to categorical cross-entropy but introduces some computational shortcuts that save time in memory as well as computation because it uses a single integer for a class, rather than a whole vector. This is especially useful when we have data with many classes to predict.

We can specify the use of the sparse categorical crossentropy in the .compile() method:

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

Note the following changes: we make sure that our labels are just integer encoded using the LabelEncoder() but not converted into one-hot-encodings using .to_categorical(). Hence, we comment out the code that uses .to_categorical().
'''



import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  InputLayer
from tensorflow.keras.layers import  Dense
from sklearn.metrics import classification_report
import numpy as np
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
#we comment it here because we need only integer labels for
#sparse cross-entropy
# y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
# y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

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
model.fit(x_train, y_train, epochs = 20, batch_size = 16, verbose = 0)

#get additional statistics
y_estimate = model.predict(x_test, verbose=0)
y_estimate = np.argmax(y_estimate, axis=1)
print(classification_report(y_test, y_estimate))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])






'''
Output

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7782 entries, 0 to 7781
Data columns (total 14 columns):
PM2.5          7782 non-null float64
PM10           7782 non-null float64
NO             7782 non-null float64
NO2            7782 non-null float64
NOx            7782 non-null float64
NH3            7782 non-null float64
CO             7782 non-null float64
SO2            7782 non-null float64
O3             7782 non-null float64
Benzene        7782 non-null float64
Toluene        7782 non-null float64
Xylene         7782 non-null float64
AQI            7782 non-null float64
Air_Quality    7782 non-null object
dtypes: float64(13), object(1)
memory usage: 851.3+ KB
None
Counter({'Very Poor': 1297, 'Poor': 1297, 'Moderate': 1297, 'Satisfactory': 1297, 'Severe': 1297, 'Good': 1297})
              precision    recall  f1-score   support

           0       0.58      0.95      0.72       100
           1       0.89      0.27      0.41       508
           2       0.36      0.81      0.49       172
           3       0.68      0.80      0.73       452
           4       0.36      0.81      0.50        37
           5       0.58      0.34      0.43       125

    accuracy                           0.58      1394
   macro avg       0.57      0.66      0.55      1394
weighted avg       0.69      0.58      0.55      1394







<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7782 entries, 0 to 7781
Data columns (total 14 columns):
PM2.5          7782 non-null float64
PM10           7782 non-null float64
NO             7782 non-null float64
NO2            7782 non-null float64
NOx            7782 non-null float64
NH3            7782 non-null float64
CO             7782 non-null float64
SO2            7782 non-null float64
O3             7782 non-null float64
Benzene        7782 non-null float64
Toluene        7782 non-null float64
Xylene         7782 non-null float64
AQI            7782 non-null float64
Air_Quality    7782 non-null object
dtypes: float64(13), object(1)
memory usage: 851.3+ KB
None
Counter({'Very Poor': 1297, 'Poor': 1297, 'Moderate': 1297, 'Satisfactory': 1297, 'Severe': 1297, 'Good': 1297})
              precision    recall  f1-score   support

           0       0.64      0.96      0.77       100
           1       0.85      0.87      0.86       508
           2       0.62      0.74      0.68       172
           3       0.94      0.76      0.84       452
           4       0.45      0.84      0.58        37
           5       0.73      0.50      0.59       125

    accuracy                           0.79      1394
   macro avg       0.71      0.78      0.72      1394
weighted avg       0.82      0.79      0.79      1394



Key Changes
Accuracy: Increased from 0.58 to 0.79.
Precision, Recall, F1-score: Improved for most classes, indicating better performance.
Macro avg and Weighted avg: Improved, showing overall better model performance.
The model has learned better with more epochs, leading to improved metrics.

'''