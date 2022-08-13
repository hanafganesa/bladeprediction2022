from flask import Flask
from pydantic import BaseModel
import pickle
import json

app = Flask("__name__")

class model_input(BaseModel):
    pcut_position : int
    psvol_position : int

# load saved model
svmodel = pickle.load(open('logreg_model.sav', 'rb'))

@app.route("/")
def hello():
    return "Blade Prediction Model"

@app.route("/blade_predict")
def blade_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    pcpos = input_dictionary['pcut_position']
    pspos = input_dictionary['psvol_position']

    input_list = [pcpos, pspos]

    prediction = svmodel.predict([input_list])

    if(prediction[0] == 0):
        return 'The blade is Worn'
    else:
        return 'The blade is New'

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0',debug=True)