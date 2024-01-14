from flask import Flask, request, jsonify
import pandas as pd
import json
from b_Excel_By_Input import input_to_Excel
from c_Graph_and_Html import Excel_to_Graph

app = Flask(__name__)

@app.route('/bc_app', methods=['POST'])
def submit_user_data():
    try:
        user_data = request.json
        Pb = input_to_Excel(user_data)
        img1, img2 = Excel_to_Graph(Pb)
        return jsonify({'message': 'Data received successfully', 'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
