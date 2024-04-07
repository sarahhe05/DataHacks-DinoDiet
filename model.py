#importing packages
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc, confusion_matrix, precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
import seaborn as sns

#reading and getting the dataset
df = pd.read_csv("data.csv")

#list all diets
df["diet"].unique()

#number of herbivorous
df[df["diet"] == "herbivorous"].shape[0]

#number of carnivorous
df[df["diet"] == "carnivorous"].shape[0]

#number of omnivorous
df[df["diet"] == "omnivorous"].shape[0]

#data columns
df.columns

df

#change herbivorous/omnivorous to omnivorous
df['diet'] = df['diet'].replace('herbivorous/omnivorous', 'omnivorous')

#check how many omnivorous there are after the change
df[df["diet"] == "omnivorous"].shape[0]

#find all unique values of period column
df["period"].unique()

#find all unique values of lived_in column
df["lived_in"].unique()

#find all unique values of types of dinosaurs
df["type"].unique()

#change the period column into three categories
for i, period in enumerate(df["period"]):
  if "Triassic" in period:
    df["period"][i] = "Triassic"
  if "Jurassic" in period:
    df["period"][i] = "Jurassic"
  if "Cretaceous" in period:
    df["period"][i] = "Cretaceous"

df

#double check period column
df["period"].unique()

#drop all rows with USA in the period column
df = df[df.get("period") != "USA"]
df

#drop all rows with null values
df = df.dropna()
df

#drop all unneccsary columns because there are not useful
clean = df.drop(columns = ['name', 'taxonomy', 'named_by', 'species', 'link'])
clean

#get rid of unknown diet
clean = clean[clean["diet"] != "unknown"]
clean

#explore length column
clean["length"].unique()

#convert length column to floats
len_arr = np.array(clean["length"])
for i, elem in enumerate(len_arr):
  len_arr[i] = float(elem[:-1])
clean["length"] = len_arr
clean

#plotting length column to see the distribution on the histogram
clean.plot(kind = "hist", y = "length")

#find the median length
median = clean["length"].median()
median

#change the length columns into two categories: small and large
category_lst = []
for length in clean["length"]:
  if length < 6.0:
    category_lst.append("short")
  else:
    category_lst.append("tall")
category_arr = np.array(category_lst)
clean["length"] = category_arr

#preparing matrices for modeling
target = clean.iloc[:, [0]]
clean = clean.drop(columns = 'diet')

#train XGB Classifier, check accuracy, and display confusion matrix
X, y = clean, target
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_2 = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X_2, y, test_size=0.2, random_state=42)
classifier = xgb.XGBClassifier(gamma = 1)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
y_pred = label_encoder.inverse_transform(y_pred)
y_test = label_encoder.inverse_transform(y_test)

# conf_matrix = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(6, 6))
# sns.heatmap(conf_matrix, annot=True)
# plt.title('Confusion Matrix')
# plt.xlabel('Predicted')
# plt.ylabel('True')
# plt.show()
#feature importance
# importances = classifier.feature_importances_
# feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importances})
# feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
# print(feature_importance_df)

#method to create prediction on new data
def predict_one(period, location, types, length):
  df = pd.DataFrame({'period': period, 'lived_in': location, 'type' : types, 'length': length}, index = [0])
  X2 = pd.concat([df, X])
  encoded = pd.get_dummies(X2)
  y_pred = classifier.predict(encoded)
  result = label_encoder.inverse_transform(y_pred)
  return result[0]
