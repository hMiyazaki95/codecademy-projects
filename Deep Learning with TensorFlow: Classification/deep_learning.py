from sklearn.metrics import log_loss

#the first class is set to probability 1, all others are 0; this example belongs to class #1
ex_1_true = [1, 0, 0] 
#the second class is set to probability 1, all others are 0;this example belongs to class #2
ex_2_true = [0, 1, 0] 
#the third class is set to probability 1, all others are 0;this example belongs to class #3
ex_3_true = [0, 0, 1] 

#the highest probability is given to class #1
ex_1_predicted = [0.7, 0.2, 0.1] 
#the highest probability is given to class #2
ex_2_predicted = [0.1, 0.8, 0.1] 
#the highest probability is given to class #3
ex_3_predicted = [0.2, 0.2, 0.6] 

#the highest probability given to class #3, true labels is class #1
ex_1_predicted_bad = [0.1, 0.1, 0.7]
#the highest probability given to class #1, true labels is class #2
ex_2_predicted_bad = [0.8, 0.1, 0.1] 
#the highest probability given to class #1, true labels is class #3
ex_3_predicted_bad = [0.6, 0.2, 0.2] 

true_labels = [ex_1_true, ex_2_true, ex_3_true]
predicted_labels = [ex_1_predicted, ex_2_predicted, ex_3_predicted]
predicted_labels_bad = [ex_1_predicted_bad, ex_2_predicted_bad, ex_3_predicted_bad]

ll = log_loss(true_labels, predicted_labels)
print('Average Log Loss (good prediction): %.3f' % ll)

ll = log_loss(true_labels, predicted_labels_bad)
print('Average Log Loss (bad prediction): %.3f' % ll)

#your code here
ll = log_loss(true_labels, true_labels)
print('(TODO)Average Log Loss (true prediction): %.3f' % ll)


'''
Classification
Cross-entropy
8 min
Before we continue loading the data and designing the model, we need to talk about cross-entropy, an important concept for evaluating classification model training. Cross-entropy is a score that summarizes the average difference between the actual and predicted probability distributions for all classes. The goal is to minimize the score, with a perfect cross-entropy value is 0.

For example, consider a problem with three classes, each having three examples in the data classified in class 1, class 2, and class 3, respectively. They are represented with one-hot encoding.

Let the true distribution for each example be:

#the first class is set to probability 1, all others are 0; this example belongs to class #1
ex_1_true = [1, 0, 0] 
#the second class is set to probability 1, all others are 0;this example belongs to class #2
ex_2_true = [0, 1, 0] 
#the third class is set to probability 1, all others are 0;this example belongs to class #3
ex_3_true = [0, 0, 1] 

Now imagine a predictive model that gave us the following predictions:

#the highest probability is given to class #1
ex_1_predicted = [0.7, 0.2, 0.1] 
#the highest probability is given to class #2
ex_2_predicted = [0.1, 0.8, 0.1] 
#the highest probability is given to class #3
ex_3_predicted = [0.2, 0.2, 0.6] 

If we compare the true and predicted distributions above, they seem to be rather different numbers, but there is a good pattern here: each example’s predicted distribution gives the highest probability to the label the example actually belongs to. This means the distributions are similar and the cross-entropy should be small. When we calculate cross-entropy for the example above, we get 0.364, which is rather good and close to 0.

Now, consider a bad predictive model that gives the highest probability to a wrong label every time:

#the highest probability given to class #3, true labels is class #1
ex_1_predicted_bad = [0.1, 0.1, 0.7]
#the highest probability given to class #1, true labels is class #2
ex_2_predicted_bad = [0.8, 0.1, 0.1] 
#the highest probability given to class #1, true labels is class #3
ex_3_predicted_bad = [0.6, 0.2, 0.2] 

When we calculate the cross-entropy for these examples, we get 2.036, which is rather bad.

If we take cross-entropy between two identical true distributions, we get perfect probabilities and cross-entropy equal to 0.

Run the code on the right to see this in practice. To calculate cross-entropy between two distributions we are using the log_loss() function in scikit-learn, which is equivalent to calculating cross-entropy.

Instructions
Checkpoint 1 Passed
1.
Use the log_loss() function to calculate cross-entropy between true_labels and true_labels.

'''