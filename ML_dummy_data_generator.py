import pandas as pd
import numpy as np

# Create a dummy dataset
np.random.seed(0)
dummy_data = {
    'Feature1': np.random.normal(100, 10, 100).tolist() + [np.nan, 700],  # Normally distributed with an outlier
    'Feature2': np.random.randint(0, 100, 102).tolist(),  # Random integers
    'Category': ['A', 'B', 'C', 'D'] * 25 + [np.nan, 'A'],  # Categorical with some missing values
    'Target': np.random.choice([0, 1], 102).tolist()  # Binary target variable
}

# Convert the dictionary to a pandas DataFrame
df_dummy = pd.DataFrame(dummy_data)

#Insert 5 additional missing values in 'Category'
nan_indices = np.random.choice(df_dummy.index, size=5, replace=False)
df_dummy.loc[nan_indices, 'Category'] = np.nan


# Display the first few rows of the dummy dataset
print(df_dummy.head())

df_dummy.to_csv('ML_dummy_dataset.csv', index=False)


