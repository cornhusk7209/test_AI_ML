import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import missingno as msno  # Optional: for visualizing missing data
from scipy import stats
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
df_dummy = pd.read_csv('ML_dummy_dataset.csv') #read the dataset from folder

# Display the first few rows of the dataset
print(df_dummy.head())

#Load processing functions
def load_data(df):
    return df

# For numeric data, fill missing values with the mean
def handle_missing_values(df):
    numeric_df = df.select_dtypes(include='number')
    return df.fillna(numeric_df.mean())


def remove_outliers(df):
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    print(df)
    print(z_scores)
    return df[(z_scores < 3).all(axis=1)]# Remove rows with any outliers
    # print(df)
    # feature1 = df['Feature1'].dropna()
    # z_scores_feature1 = stats.zscore(feature1)
    # df.loc[feature1.index, 'Feature1_zscore'] = z_scores_feature1
    # print(df[['Feature1', 'Feature1_zscore']])
    

def scale_data(df):
    scaler = StandardScaler()
    df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(df.select_dtypes(include=[np.number]))
    return df

def encode_categorical(df, categorical_columns):
    return pd.get_dummies(df, columns=categorical_columns)

def save_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
    
#Process the data

# Load the data
df_preprocessed = load_data(df_dummy)
print(df_preprocessed.dtypes)

# Handle missing values
# df_preprocessed = handle_missing_values(df_preprocessed)
print('There are '+ str(df_preprocessed.isnull().sum().sum()) +' missing values')


df_preprocessed = handle_missing_values(df_preprocessed)
print(df_preprocessed.isnull().sum())  # Verify that there are no missing values

## Remove outliers
df_preprocessed = remove_outliers(df_preprocessed)

print(df_preprocessed.tail(3))