'''
Loading and analyzing the data
14 min
Let’s walk through an example of how to load, analyze, and split the data.

Assume we have a dataset, stored in the train_glass.csv (training data) and test_glass.csv (test data) files, about various products made of glass. Using the train_glass.csv file, we want to learn a model that can predict which glass item can be constructed given the proportion of various elements such as Aluminium (Al), Magnesium (Mg), and Iron (Fe). We then want to evaluate the model on the test data.

To load the training data into a pandas DataFrame, we do the following:

import pandas as pd
data_train = pd.read_csv("train_glass.csv")

The following command lists all features with accompanying types about the columns:

print(data_train.info())

The output looks something like this:

#   Column    Non-Null Count   Dtype  
---  ------   --------------   -----  
 0   Al       300 non-null     float64
 1   Mg       300 non-null     float64 
 3   Fe       300 non-null     float64
 4   item     300 non-null     object

We see that Al, Mg, and Fe are numeric columns, and item is an object column containing strings. We would like to predict the item column.

The following commands show us which categories we have in the item column and what their distribution is:

from collections import Counter
print('Classes and number of values in the dataset:',Counter(data_train[“item”]))

which gives us the following output:

Classes and number of values in the dataset:
Counter({'lamps': 75, 'tableware': 125, 'containers': 100}

This tells us that we have three categories to predict: “lamps”, “tableware”, and “containers”, and how many samples we have in our training data for each.

Lastly, we need to split the features in our data into the label (y-variable we are trying to predict) and the x-variables (predictor variables) by doing the following:

train_y = data_train["item"]
train_x = data_train[['Al', 'Mg', 'Fe']]

For this exercise (and the remainder of this lesson), you will be working with the air_quality_train.csv and air_quality_test.csv data sets. You will create a classification model that will predict the air quality dependent on the different element compounds found in the air (e.g. Carbon monoxide, Benzene). The label column or y-variable is Air_Quality and has the following scale from worst to best air quality, ['Severe', 'Very Poor', 'Poor', 'Moderate', 'Satisfactory', 'Good'].


1.
Using pd.read_csv(), load and save the air_quality_train.csv data set to an object named train_data. Then load and save air_quality_test.csv as test_data.

Stuck? Get extra guidance
Checkpoint 2 Passed
2.
Let’s take a look at the column features of the training data set. Use .info() to print the non-null count (the observations that are not null) and the data type of each column in train_data.

Stuck? Get extra guidance
Checkpoint 3 Passed
3.
Next, use Counter() to print the class distribution for Air_Quality from the training set.

Checkpoint 4 Passed
4.
Save all the predictor variables to the object x_train. The predictor variables are all the variables except Air_Quality.

Stuck? Get extra guidance
Checkpoint 5 Passed
5.
Then save the label (y-variable) to the object y_train.

In the next exercise, we will split the testing data and continue with our classification model.
'''


import pandas as pd
from collections import Counter

# 1- read in and save the training and testing data

train_data = pd.read_csv("air_quality_train.csv")

test_data = pd.read_csv("air_quality_test.csv")

# 2- print columns and their respective types of train_data

print(train_data.info())


# 3- pint the class distribution
print(Counter(train_data["Air_Quality"]))


# 4- extract the predictor features from the training data

x_train = train_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]

# 5- extract the label column (y-variable) from the training data
y_train = train_data["Air_Quality"]
