from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load medicine data from JSON
with open('medicines.json', 'r', encoding='utf-8') as file:
    medicines_data = json.load(file)['medicines']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_medicines', methods=['POST'])
def get_medicine():
    medicine_name = request.form['medicine-name']

    for medicine in medicines_data:
        if medicine['name'].lower() == medicine_name.lower():
            return jsonify(medicine)

    return jsonify({'error': 'Medicine not found'})

if __name__ == '__main__':
    app.run(debug=True)




