import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import missingno as msno  # Optional: for visualizing missing data
from scipy import stats

# Load your dataset into a pandas DataFrame
df_dummy = pd.read_csv('ML_dummy_dataset.csv') #read the dataset from folder

# Display the first few rows of the dataset
print(df_dummy.head())

#Load processing functions
def load_data(df):
    return df

def handle_missing_values(df):
    return df.fillna(df.mean())  # For numeric data, fill missing values with the mean

def remove_outliers(df):
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    return df[(z_scores < 3).all(axis=1)]  # Remove rows with any outliers

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
#df_preprocessed = handle_missing_values(df_preprocessed)