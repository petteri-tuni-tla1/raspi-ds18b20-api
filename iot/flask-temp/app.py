from flask import Flask, jsonify
import os
import glob
import time

# The path to your file containing the integer
FILE_PATH = "/opt/iot/data/temp1.txt"
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        with open(FILE_PATH, 'w') as f:
            f.write(str(temp_c))

app = Flask(__name__)


@app.route('/get-temp', methods=['GET'])
def read_temp_value():
    # Check if the file exists to avoid a crash
    if not os.path.exists(FILE_PATH):
        return jsonify({"error": "File not found"}), 404

    try:
        read_temp()
        with open(FILE_PATH, 'r') as f:
            content = f.read().strip()
            
            # Convert to integer to validate it's actually a number
            # value = int(content)
            
            return jsonify({"value": content}), 200

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

