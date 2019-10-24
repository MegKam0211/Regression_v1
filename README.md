# Regression
# A simple Machine Learning example using linear regression.
Regression using python's quandl function

following the tutorial of sentdex https://www.youtube.com/watch?v=JcI5Vnw0b2c&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=2

I calculate the relationship values between the High and Low stock percentages.

And then calculate the percentage between the Open and Last stock values to see if any changes occurred.

Predicting future stock movements and prices.
using linear regression algorithm and then fitting the data to svm. 

#firstly 
calculating the relationship between the high and the low percent ie. 'HL_PCT' = HighLow_Percent
and the relationship between Last and Open percent daily percent change ie 'PCT_change'

features that we have set:'Last', 'HL_PCT', 'PCT_change', 'Volume

#secondly 
we will try to predict out 10% of the datafame
compare the forecast price to the Last price

#thirdly 
train, test, predict and run the algorithm
sklearn's preprocessing mwthod is used on the features,where the goal is to be between -1 and 1.
cross vaidation is used to create training and testing samples - to split the data.

Why train and test on separate data:
if you train a classifier to predict based on the same data that you test against, when you do test it, the program will have seen the data already and so knows what the answer is. 

What we see when running the algorithms:
svm gives an accuracy of 0.175 between the test data and the trained data.
Whereas linear regression gives a higher accuracy of 0.243.
To obtain the variance score of the
model, the score() function is used which is te accuracy in my code. 

With the various algorithms, check the documentation to find which one can be threaded.
