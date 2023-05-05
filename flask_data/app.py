from flask import Flask, render_template, request,jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
Analyzed_Data = []
@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['data_file']
    df = pd.read_csv(file)

    # perform data analysis
    num_rows, num_cols = df.shape
    # summary_stats = df.describe()
    # summary_stats_json = summary_stats.to_json(orient='index')



    

    # # Get the value of the environment variable
    # my_variable = os.environ.get('MY_VARIABLE')
    data ={'num_rows': num_rows,'num_cols':num_cols}
    Analyzed_Data.append(data)



    return jsonify({'message': 'File added successfully'})


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'Analyzed_Data': Analyzed_Data})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
