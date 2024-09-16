'''
Setting the optimizer
4 min
Now that we’ve had a brief introduction to cross-entropy, we’ll see how to use it with our model.

First, to specify the use of cross-entropy when optimizing the model, we need to set the loss parameter to categorical_crossentropy of the Model.compile() method.

Second, we also need to decide which metrics to use to evaluate our model. For classification, we usually use accuracy. Accuracy calculates how often predictions equal labels and is expressed in percentages. We will use this metric for our problem.

Finally, we will use Adam as our optimizer because it’s effective here and is commonly used.

To compile the model with all the specifications mentioned above we do the following:

my_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

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

print(x_train.head())
print(y_train)



'''
Output


Output-only Terminal
Output:
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
    PM2.5    PM10     NO    NO2    NOx  ...     O3  Benzene  Toluene  Xylene    AQI
0  206.14  334.21  61.02  63.70  89.54  ...  35.84     5.45    42.52    0.71  342.0
1   53.71   60.15  11.02  13.43  20.48  ...  22.08     0.91     3.45    0.69  226.0
2  187.82  300.92  28.91  60.61  57.94  ...  83.99     1.56     6.80    0.08  362.0
3   50.64  132.94   9.56  37.51  11.09  ...  50.11     0.22     2.27    0.26  161.0
4   27.98   79.71   2.79  18.31  12.10  ...  34.54     0.19     1.79    0.13   79.0

[5 rows x 13 columns]
[[0 0 0 0 0 1]
 [0 0 1 0 0 0]
 [0 0 0 0 0 1]
 ...
 [0 0 0 0 0 1]
 [0 0 0 0 0 1]
 [0 0 0 0 0 1]]


'''