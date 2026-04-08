# importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# read the file
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\healthcare_dataset.csv\healthcare_dataset.csv")
#print(df.columns)

#EDA
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.shape)

# data cleaning
# print(df.isnull().sum())

#visualization
print(df.columns)
numric_cols = [[ 'Age','Blood Type', 'Medical Condition',
       'Billing Amount']]
