# Heart Disease Data Processing Script

#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load Dataset
file_path = 'Heart.csv'
df = pd.read_csv(file_path)

# Step 2: Inspect Data 
print('Data Info:')
print(df.info())
print('\nData Stats:')
print(df.describe())
print('\nFirst 5 rows:')
print(df.head())

# Step 3: Save Data in Various Formats
df.to_excel('dataset.xlsx', index=False)
df.to_json('dataset.json', orient='records', indent=2)
from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:")
df.to_sql('dataset', con=engine, index=False, if_exists='replace')

# Step 4: Reload Data to Verify 
df_excel = pd.read_excel('dataset.xlsx')
df_json = pd.read_json('dataset.json')
df_sql = pd.read_sql('dataset', con=engine)

# Step 5: Clean and Prepare Data
# Handle Missing Values
df.fillna(method='ffill', inplace=True)
# Remove Duplicates
df.drop_duplicates(inplace=True)
# Normalize Numerical Data 
scaler = MinMaxScaler()
numerical_cols = df.select_dtypes(include=['number']).columns
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
# Encode Categorical Data
df = pd.get_dummies(df, drop_first=True)
# Final Dataset
print('Cleaned Data:')
print(df.head())
# Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
