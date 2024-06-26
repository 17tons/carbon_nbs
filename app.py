import flask
from flask import Flask, request, jsonify, send_from_directory, abort, make_response
import pickle
import numpy as np
import json
import uuid
import os
from threading import Thread
import boto3
from botocore.exceptions import NoCredentialsError


app = Flask(__name__)
ec2_client = boto3.client('ec2', region_name='us-west-2')
output_folder = 'output_files'
os.makedirs(output_folder, exist_ok=True)


with open('rf.pkl', 'rb') as f:
     
     model = pickle.load(f)
 
@app.route('/predict', methods=['POST'])
def predict():
     
     data = request.get_json()
     prediction = model.predict(np.array(data['features']).reshape(1, -1))
     return jsonify({'prediction': prediction.tolist()})
 
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
