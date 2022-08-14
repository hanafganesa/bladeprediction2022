from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)
svmodel = pickle.load(open('logreg_model.sav', 'rb'))

@app.route("/")
def home():
    return "Blade Prediction Model"

@app.route("/predict", methods=['POST'])
def predict():
    # print(1)
    data = request.get_json(force=True)
    prediction = svmodel.predict([np.array(list(data.values()))])

    # output = prediction[0]
    # return jsonify(output)

    if(prediction[0] == 0):
        return 'The blade is Worn'
    else:
        return 'The blade is New'

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0',debug=True)