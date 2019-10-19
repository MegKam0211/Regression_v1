import pandas as pd
import quandl

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

print(df.head)

