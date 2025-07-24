import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Step 1: Load the dataset
df = pd.read_csv("your_dataset.csv")  # Replace with your CSV file path
print("Original Data:\n", df.head())

# Step 2: Handle missing values
imputer = SimpleImputer(strategy="mean")  # For numerical columns
df[df.select_dtypes(include=['float64', 'int64']).columns] = imputer.fit_transform(
    df.select_dtypes(include=['float64', 'int64'])
)

# Step 3: Encode categorical variables
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le  # Save the encoder for inverse transform if needed

# Step 4: Feature scaling
scaler = StandardScaler()
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Step 5: Split the data
X = df.drop(columns=["target"])  # Replace "target" with your target column
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Preprocessing complete.")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
