import pickle
import pandas as pd
from flask import Flask, request, jsonify

# create flask app
app = Flask(__name__)

# load pickle model
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return "Blade Prediction Model"


@app.route("/predict", methods=["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = model.predict(query_df)

    json_response = []
    for index, row in query_df.iterrows():
        if prediction[index] == 1:
            condition = "The blade is New"
        else:
            condition = "The blade is Worn"
        json_response.append({"pcut_position": int(row['pcut_position']),
                              "psvol_position": int(row['psvol_position']),
                              "prediction": int(prediction[index]),
                              "condition": condition
                              })

    return jsonify(json_response)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(debug=True)
