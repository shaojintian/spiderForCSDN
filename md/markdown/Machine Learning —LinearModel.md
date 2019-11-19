

## Machine Learning —LinearModel

Supervised Learning:
Basic topics are Classification and Regression.

Classification:

About linear model, it includes LinearSVC , LogisticRegression(a classifier not a regressor)， GaussianNaiveBayesClassifier (GuNBC), BernoulliNBC, MultinomialNBC , Decision Trees,Random Forests

First model LinearSVC:

parameters includes :

Regularization class: L1 or L2 .
L1 norm can decrease the coefficients to zero .But L2 can't do that. L2 norm only can try to decrease the coefficients to close to zero.

So L1 norm can select the numbers of features , but L2 can't.

Then,L1 style can increase the interpretability of this model,but lose some important features.

L2 maybe be pollued by meaningless features.



2.C:(learning rate)

C is about restrictive ability. If C is small , coefficients and intercept is be restricted to close to zero (whether it can be explicitly zero depends on L1 or L2)

else if C is high, restrictive ability is low.





Second model: LinearRegression

parameters :

1:Regularization class: L1 or L2 .

This is the same as above the first line.

2:alpha(learning rate)

alpha is opposite to C .If alpha is high , coefficients and intercept is be restricted to close to zero (whether it can be explicitly zero depends on L1 or L2)

else if alpha is low, restrictive ability is low.





Third model : Gussian Naive Bayes Classifier

paramerter:

1:alpha





Fourth model : Bernoulli Naive Bayes Classifier

paramerter:

1:alpha (controls the complexity of model)

ability:

Increase the smoothing performance of model via adding virtual many data points to datasets . Virtual data points contains all positive features .

When increase the alpha , the model will be smoother. So it will decrease the complexity of model . When decrease it , the model will be more complex.











Fourth model : Bernoulli Naive Bayes Classifier

paramerter:

1:alpha (controls the complexity of model) (It is the same as BernoulliNBC)

ability:

Increase the smoothing performance of model via adding virtual many data points to datasets . Virtual data points contains all positive features .

When increase the alpha , the model will be smoother. So it will decrease the complexity of model . When decrease it , the model will be more complex.





Fifth model: Decision Trees

parameters:



Advantages:

1: Easily Visualize .

Generate visualized decision trees to help non-experts to understand this model.

2:less influence about data or features types

Due to every feature is been processed separately , so whatever the data type is binary or continuous .



Disadvantages :

1:poor generalization ability

Easy to overfit ,even it has used pre-pruning. Because of it ,we usually to use ensembles of decision trees to decrease this influence based on decision trees(such as Random Forests and Gradient Boosted Decision Trees)



Sixth model :Random Forests:

Parameters:

1:n_estimator

decide the numbers of decision trees .

2:max_features

decide the max numbers of features .

Preprocessing:

For dataset:

Bootstrap Sample(自动采样）：

To explain it , if we have 100 data nodes ,we select randomly 100 times from this dataset to generate a new dataset which is as big as original dataset , after every time selection ,we don't reduce the data node from original dataset .Clear?
