import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# loading the diabetes dataset to a pandas DataFrame
df = pd.read_csv("trimmed_blade.csv")

print(df.head())

# select lists of features and target names
X = df.drop("label", axis=1)
y = df["label"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# instantiate model
classifier = LogisticRegression(C=100, penalty="l2", solver="lbfgs")

# fit the model
classifier.fit(X_train, y_train)

# pickle
pickle.dump(classifier, open("model.pkl", "wb"))
