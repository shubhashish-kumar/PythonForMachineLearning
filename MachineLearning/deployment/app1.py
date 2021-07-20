## execute 'python app1.py' command on terminal with this file's location

from flask import Flask, request
import json
import joblib

app = Flask(__name__)
model = joblib.load("ccpp_model.pkl")


@app.route("/",methods=["GET","POST"])
def main():
    return "Hello world from Flask"

@app.route("/predict",methods=["GET","POST"])
def main2():
    data = request.data
    data = data.decode()
    data = json.loads(data)
    data['prediction'] = model.predict(data['values']).tolist()
    print(data,type(data))
    return json.dumps(data)

if __name__=="__main__":
    app.run(port=5000)