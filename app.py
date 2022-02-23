#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)
from flask import request, render_template
import joblib
import pandas as pd
from scipy import stats
import numpy as np

@app.route("/",methods = ["GET","POST"])

def getDefault(i):
    return "default" if 1 else "no default"

def index():
    
    if request.method == "POST":
        df = pd.read_csv("Credit Card Default II (balance).csv")
        dfnew = df[df["age"]>0]
        x_column = ['income', 'age', 'loan']
        age = request.form.get("age")
        loan = request.form.get("loan")
        income = request.form.get("income")
        dfnew = dfnew[['income', 'age', 'loan']]
        df2 = {'income': income, 'age': age, 'loan': loan}
        dfnew = dfnew.append(df2, ignore_index=True)
        model1 = joblib.load("LogisticRegression")
        model2 = joblib.load("DecisionTree")
        model3 = joblib.load("RandomForest")
        model4 = joblib.load("XGBoost")
        model5 = joblib.load("MLP")
        normalised_df = dfnew.copy()
        for i in x_column:
            normalised_df[i] = stats.zscore(normalised_df[i].astype(np.float))
        lastrow = normalised_df.iloc[-1]
        pred = model1.predict([[float(lastrow[0]),float(lastrow[1]),float(lastrow[2])]])
        pred2 = model2.predict([[float(income),float(age),float(loan)]])
        pred3 = model3.predict([[float(lastrow[0]),float(lastrow[1]),float(lastrow[2])]])
        pred4 = model4.predict([[float(lastrow[0]),float(lastrow[1]),float(lastrow[2])]])
        pred5 = model5.predict([[float(lastrow[0]),float(lastrow[1]),float(lastrow[2])]])
        res = "Logistic Regression: " + str(getDefault(pred[0])) + "." + 
        "Decision Tree: " + str(getDefault(pred[0])) + "." +
        "Logistic Regression: " + str(getDefault(pred[0])) + "." + 
        "Logistic Regression: " + str(getDefault(pred[0])) + "." + 
        "Logistic Regression: " + str(getDefault(pred[0])) + "." +
        return (render_template("index.html",result=pred))
    else:
        return (render_template("index.html",result="2"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




