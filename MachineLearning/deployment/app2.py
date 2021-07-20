from flask import Flask, request, render_template
import json
import joblib

app = Flask(__name__)
model = joblib.load("ccpp_model.pkl")


@app.route("/",methods=["GET","POST"])
def main():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def main2():
    data = request.form
    #data['prediction'] = model.predict(data['values']).tolist()
    print(data,type(data))
    return json.dumps(data)

if __name__=="__main__":
    app.run(port=5000)