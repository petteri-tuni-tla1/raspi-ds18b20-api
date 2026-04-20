from flask import Flask, jsonify
import os

app = Flask(__name__)

# The path to your file containing the integer
FILE_PATH = "data.txt"

@app.route('/get-integer', methods=['GET'])
def get_integer():
    # Check if the file exists to avoid a crash
    if not os.path.exists(FILE_PATH):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(FILE_PATH, 'r') as f:
            content = f.read().strip()
            
            # Convert to integer to validate it's actually a number
            value = int(content)
            
            return jsonify({"integer_value": value}), 200
    except ValueError:
        return jsonify({"error": "File does not contain a valid integer"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create a dummy file if it doesn't exist for testing
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            f.write("42")
            
    app.run(debug=True, port=5000)

