from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    nitrogen = request.form['Nitrogen']
    phosphorus = request.form['Phosporus']
    potassium = request.form['Potassium']
    temperature = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['pH']
    rainfall = request.form['Rainfall']

    # Simulate recommendation logic (replace with your ML model logic)
    result = f"Use fertilizer with NPK: {nitrogen}-{phosphorus}-{potassium}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
