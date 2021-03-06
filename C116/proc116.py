# -*- coding: utf-8 -*-
"""ProC116.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dd_1Yk9rUG9ChKCKaAO6tC_dB-RPmoTc
"""

from google.colab import files
data_to_upload = files.upload()

import pandas as pd
import plotly.express as px

df = pd.read_csv('Admission_Predict.csv')
#Serial No.	GRE Score	TOEFL Score	University Rating	SOP	LOR	CGPA	Chance of admit

#  TOEFL score as X and Chance of admit as  result as Y

toefl_score = df['TOEFL Score'].tolist()
results = df['Chance of admit'].tolist()

fig = px.scatter(x=toefl_score,y=results)
fig.show()

import plotly.graph_objects as go

toefl_score = df['TOEFL Score'].tolist()
results = df['Chance of admit'].tolist()
colors = []

for data in results:
  if data == 1:
    colors.append("green")
  else:
    colors.append("red")

fig = go.Figure(data = go.Scatter(
    x = results,
    y = toefl_score,
    mode = 'markers',
    marker = dict(color = colors)
))
fig.show()

scores = df[["TOEFL Score"]]
results = df['Chance of admit']

from sklearn.model_selection import train_test_split

score_train, score_test, results_train, results_test = train_test_split(scores,results,test_size=0.25,random_state = 0)
print(score_train)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(score_train,results_train)

results_pred = classifier.predict(score_test)
from sklearn.metrics import accuracy_score

print("accuracy: ",accuracy_score(results_test,results_pred))

