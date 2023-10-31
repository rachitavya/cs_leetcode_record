from flask import Flask,request, render_template
import pandas as pd

data=pd.read_csv("Contact Information (Responses) - Form Responses 1.csv")
data=data.drop(columns=['Timestamp'],axis=1)

students_data = data.to_dict(orient='records')

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',students=students_data)

if __name__=='__main__':
     app.run(debug=True)