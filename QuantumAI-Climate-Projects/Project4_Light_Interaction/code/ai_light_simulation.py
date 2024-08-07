import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load cloud data
data = pd.read_csv('../data/cloud_data.csv')
X = data[['light_intensity', 'water_droplet_density']]
y = data['scattered_light_intensity']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train AI model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print(predictions)

