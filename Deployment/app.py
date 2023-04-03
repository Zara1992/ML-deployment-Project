from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd


# App definition
app = Flask(__name__)

# importing models
with open('..\Pickle_Dump\ModelGS.pkl', 'rb') as f:
   grid = pickle.load (f)



#webpage

@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Loan Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           query_ = pd.DataFrame(json_)
           query_['ApplicantIncome_Log'] = np.log(query_['ApplicantIncome_Log'])
           query_['LoanAmount_Log'] = np.log(query_['LoanAmount_Log'])
           query_['TotalIncome_Log'] = np.log(query_['TotalIncome_Log'])
           prediction = list (grid.best_estimator_.predict(query_))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()


