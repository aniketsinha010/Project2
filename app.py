from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application = Flask(__name__)
app = application


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        data = CustomData(  ## object of CustomData class...
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score'),
        )
        data_df = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()  ## object of PredictPipeline class..
        results = predict_pipeline.predict(data_df)  ## calling the predict method from PredictPipeleine class...

        return render_template("home.html",results=results[0])


if __name__ == "__main__":
    app.run(debug=True,port=5000)