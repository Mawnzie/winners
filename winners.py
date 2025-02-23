from flask import Flask, request, jsonify
from json import dumps
from funktioner import read_csv,parse_csv
app = Flask(__name__)


@app.route('/winners', methods=['GET'])
def winners():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file format. Only CSV allowed"}), 400

    try:
       
        df = read_csv(file)

        dfResult = parse_csv(df)
        
        result = dfResult.to_dict(orient='records')
        

        out = {"winners":result}
        return dumps(out, indent=10)

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
