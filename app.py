from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")
  
@app.route('/userlogin')
def userlogin():
    return render_template("userlogin.html")

@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html")   

@app.route('/register')
def register():
    return render_template("register.html")        

@app.route('/Heart')
def cancer():
    return render_template("checkup.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load(r'C:\Users\lenovo\OneDrive\Desktop\Heart Disease TP\heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        return(render_template("safe1.html", prediction_text=prediction))  
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("safe.html", prediction_text=prediction))       

if __name__ == "__main__":
    app.run(debug=True)
