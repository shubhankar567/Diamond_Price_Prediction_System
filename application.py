from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeine

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])  # type: ignore
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')

    else: 
        data = CustomData(
            carat=float(request.form.get('carat')), # type: ignore 
            depth = float(request.form.get('depth')), # type: ignore
            table = float(request.form.get('table')), # type: ignore
            x = float(request.form.get('x')), # type: ignore
            y = float(request.form.get('y')), # type: ignore
            z = float(request.form.get('z')), # type: ignore
            cut = request.form.get('cut'), # type: ignore
            color= request.form.get('color'), # type: ignore
            clarity = request.form.get('clarity') # type: ignore
        )
        
        # Cnverting the random input data into a dataframe
        input_dataset = data.data_to_dataframe() # type: ignore

        # Predicting
        predict_obj = PredictPipeine()
        output = predict_obj.prediction(input_dataset)

        # Rounding off the result 
        results = round(output[0],2)

        return render_template('form.html', final_result = results)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

