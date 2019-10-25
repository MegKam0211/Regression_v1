import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import linear_model
from sklearn.linear_model import LinearRegression 

#getting the dataset
df = quandl.get("CHRIS/MGEX_MW1")
#print the head just to get a look at what we are working with
#print(df.head())

#grab certain features in the dataset
#create a list of all the columns to use in the dataset.
df = df[['Open', 'High', 'Low', 'Last', 'Volume']]
#print(df)
#define what features need to be used and get rid of redundant ones.

#firstly doing the high minus the low percent
#define a new column --> 'HL_PCT' = HighLow_Percent
df['HL_PCT'] = (df['High'] - df['Last']) / df['Last'] * 100

#calculate the daily percent change
df['PCT_change'] = (df['Last'] - df['Open']) / df['Open'] * 100

#define a new dataframe with adjusted values
#define only the columns that are needed.
df = df[['Last', 'HL_PCT', 'PCT_change', 'Volume']] #volume refers to the number of trades that were made that day
#print(df.head)

#features that we have set:'Last', 'HL_PCT', 'PCT_change', 'Volume'
#to define a label, create a new column
forecast_col = 'Last'
df.fillna(-99999, inplace=True)#fill in missing data

#regression alogorithm: 
#define forecast out as being equal to the int() value
#this will predict the number of days out 
forecast_out = int(math.ceil(0.1*len(df))) #ceil() returns the ceiling value of x. math.ceil will round up to the nearest whole
#number of dayas shifted is 1%
print(forecast_out) #result is 615 days in advanc3

#we will try to predict out 10% of the datafame
#create labels now that we have forecast_out
df ['label'] = df[forecast_col].shift(-forecast_out) #shifting the columns negatively
#each row, which is the label column ie. 'Last' price for each row amount of x days into the future.
#so the features may cause the 'Last' price in x days to change or 1% 

#print(df.head())
df.dropna(inplace=True)
#print(df.tail())

#defined features are X, labels will be y
#X is equal to numpy array 
X = np.array(df.drop(['label'], 1)) #drop the label column, therefore the features will be everything but the label column
#dropping 'label' returns a new dataframe
#it can be converted to an array.
y = np.array(df['label'])

#scale X before feeding it through the classifier.
#so that it is normalized with the other data points
#to scale it, its included in the training data 
X = preprocessing.scale(X)

#define y
y = np.array(df['label'])

#print(len(X), len(y))
#pass through the x's, the y's and how big of a test size you want
#this is going to take all the features of the labels
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.15)
#We use x_train & y_train to fit our classifier
#use LinearRegression() to define a classifier.
#can now sample a training set while holding out 15% of the data for testing (evaluating) our classifier.

#test using linear regression algorithm
clf = LinearRegression()
#test using svm algorithm
#clf = svm.SVR()

clf.fit(X_train, y_train) #fit is synonomous with train
accuracy = clf.score(X_test, y_test) #score is synonomous with test

print(accuracy)
