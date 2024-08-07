import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load climate data
data = pd.read_csv('../data/historical_climate_data.csv')
X = data[['temperature', 'humidity', 'pressure']]
y = data['future_temperature']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train AI model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print(predictions)

