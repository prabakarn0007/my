import pandas as pd
import numpy as np
import pickle


### Loading the dataset
df = pd.read_csv('COVID-19 Symptoms.csv')


# --- Data Preprocessing ---
# Arrange columns in below order
df = df[['Corona result', 'age', 'Gender', 'body temperature', 'Dry_Cough', 'sour_throat', 'weakness', 'breathing_problem', 'pain in chest',
         'in contact to infected people', 'diabetes', 'heart_disease', 'lung_disease', 'high blood pressue', 'kidney_disease']]

# Renaming pain in chest as PIC , in contact to infected people as ICTIP and high blood pressue as HBP
df = df.rename(columns={'pain in chest':'PIC', 'in contact to infected people':'ICTIP', 'high blood pressue':'HBP'})

# Converting categorical features using OneHotEncoding method
df = pd.get_dummies(df,drop_first=True)

# independent and dependent features
X = df.iloc[:,1:]
y = df.iloc[:,0]

# Splitting the data into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=0)

# --- Model Building ---
# Random Forest Classifier Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

# Creating a pickle file for the classifier
filename = 'novel-corona-virus-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))
