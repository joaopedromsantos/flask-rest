from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

data = {
    'Marca': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Volkswagen', 'Audi', 'Hyundai',
              'Kia', 'Mazda', 'Subaru', 'Lexus', 'Jeep', 'Dodge', 'Ram', 'GMC', 'Cadillac', 'Buick'],
    'Modelo': ['Corolla', 'Civic', 'F-150', 'Silverado', 'Altima', '3 Series', 'C-Class', 'Golf', 'A4', 'Elantra',
               'Soul', 'CX-5', 'Outback', 'RX', 'Wrangler', 'Charger', '1500', 'Sierra', 'Escalade', 'Enclave'],
    'Ano': [2020, 2019, 2018, 2021, 2020, 2019, 2021, 2018, 2020, 2019,
            2021, 2020, 2019, 2018, 2021, 2020, 2019, 2018, 2021, 2020],
    'Preço': [20000, 22000, 25000, 27000, 23000, 35000, 40000, 21000, 37000, 19000,
              18000, 26000, 24000, 45000, 32000, 30000, 28000, 34000, 50000, 31000],
    'Quilometragem': [15000, 12000, 30000, 25000, 20000, 10000, 8000, 22000, 9000, 14000,
                      16000, 18000, 20000, 11000, 13000, 17000, 19000, 21000, 7000, 23000]
}

# Criando o DataFrame
df = pd.DataFrame(data)


@app.route('/sheets', methods=['GET'])
def get_sheets():
    return jsonify(df.to_json(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
