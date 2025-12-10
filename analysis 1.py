
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("claims_data.csv")

df['claim_status_binary'] = df['claim_status'].map({'Approved':1, 'Rejected':0})

X = df[['patient_age','claim_amount','days_to_process','risk_score']]
y = df['claim_status_binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
