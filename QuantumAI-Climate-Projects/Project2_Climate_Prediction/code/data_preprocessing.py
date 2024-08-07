import pandas as pd

# Load and preprocess climate data
data = pd.read_csv('../data/raw_climate_data.csv')

# Example preprocessing steps
data['future_temperature'] = data['temperature'].shift(-1)
data = data.dropna()

# Save preprocessed data
data.to_csv('../data/historical_climate_data.csv', index=False)

