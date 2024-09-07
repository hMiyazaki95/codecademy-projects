'''
Preparing the data
16 min
When using categorical cross-entropy — the loss function necessary for multiclass classification problems — in TensorFlow with Keras, one needs to convert all the categorical features and labels into one-hot encoding vectors. Previously, when we had features encoded as strings, we used the pandas.get_dummies() function. This works well for features, but it’s not very usable for labels. The problem is that get_dummies() creates a separate column for each category, and you cannot predict for multiple columns.

A better approach is to convert the label vectors to integers ranging from 0 to the number of classes by using sklearn.preprocessing.LabelEncoder:

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
train_y=le.fit_transform(train_y.astype(str))
test_y=le.transform(test_y.astype(str))

We first fit the transformer to the training data using the LabelEncoder.fit_transform() method, and then fit the trained transformer to the test data using the LabelEncoder.transform() method.

We can print the resulting mappings with:

integer_mapping = {l: i for i, l in enumerate(le.classes_)}
print(integer_mapping)

We get the following output:

{'lamps': 0, 'tableware': 1, 'containers': 2}

Each category is mapped to an integer, from 0 to 2 (because we have three categories).

Now that we have labels as integers, we can use a Keras function called to_categorical() to convert them into one-hot-encodings — the format we need for our cross-entropy loss:

train_y = tensorflow.keras.utils.to_categorical(train_y, dtype = 'int64')
test_y = tensorflow.keras.utils.to_categorical(test_y, dtype = 'int64')


1.
Use the LabelEncoder.fit_transform() method to encode the label vector y_train into integers and assign the result back to the y_train variable.

Stuck? Get extra guidance
Checkpoint 2 Passed
2.
Use the le.transform() method to encode the label vector y_test into integers, where le is the instance of LabelEncoder trained in the previous step, and assign the result back to y_test.

Stuck? Get extra guidance
Checkpoint 3 Passed
3.
Using the tensorflow.keras.utils.to_categorical() function, convert the integer encoded label vector y_train into a one-hot encoding vector and assign the result back into the y_train variable.

Stuck? Get extra guidance
Checkpoint 4 Passed
4.
Using the tensorflow.keras.utils.to_categorical() function, convert the integer encoded label vector y_test into a one-hot encoding vector and assign the result back into the y_test variable.


'''


import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
import tensorflow
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
y_train = le.fit_transform(y_train.astype(str))
y_test = le.transform(y_test.astype(str))

#print the integer mappings
integer_mapping = {l: i for i, l in enumerate(le.classes_)}
print("The integer mapping:\n", integer_mapping)

#integer_mapping = {l: i for i, l in enumerate(le.classes_)}
#print("The integer mapping:\n", integer_mapping)

#convert the integer encoded labels into binary vectors (binary vectors)
y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

# Print the one-hot encoded vectors
print("One-hot encoded y_train:\n", y_train)
print("One-hot encoded y_test:\n", y_test)