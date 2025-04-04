import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions
import pickle

# Loading data
df = pd.read_csv('placement.csv')

# selecting relevant columns
df = df.iloc[:,1:]

# scattering plot
plt.scatter(df['cgpa'],df['iq'],c = df['placement'])
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("Scatter Plot of CGPA vs IQ")
plt.show()

# data spiliting
x = df.iloc[:,:2]
y = df.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)


# feature scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Model training
clf  = LogisticRegression()
clf.fit(x_train,y_train)

# prediction and accuracy
y_pre = clf.predict(x_test)
accuracy_scoree = accuracy_score(y_test,y_pre)
print(f"Model Accuracy: {accuracy_scoree:.2f}")

# dicision boundary
plt.figure(figsize=(8, 6))
plot_decision_region = plot_decision_regions(x_train,y_train.values,clf=clf,legend=2)
plt.title("Decision Boundary")
plt.show()

pickle.dump(clf,open('model.pkl','wb'))