# The code was made following the tutorial found at this link:
# https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/

# The libraries we will need for the program
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

import time # Used to get the application run time


start_time = time.process_time()

url = 'new_dataset_pool.txt' # Name of the dataset
names = ['color', 'Class'] # The field names for the dataset

dataset = pd.read_csv(url, names=names) # Reads in the dataset

dataset.head()


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Trains the dataset with a test size of 0.25
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Fits our data to ensure it's not overfitted
scaler = StandardScaler()
scaler.fit(X_train)

# Get's training data
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Set's the nearest neighbors to 5
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# Sets our predictions for our test set
y_pred = classifier.predict(X_test)

# prints our results
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Get's the end time of the program's execution
print('--------{0}--------'.format(round(time.process_time() - start_time, 2)))

error = []

# Runs the KNN Algorithm 40 times to get values of i that can produce lower accuracy
# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))


# Graphs Findings
plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()