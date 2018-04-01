from flask import Flask
from flask import make_response, jsonify

import random
import cups
import glob

app = Flask(__name__)

#app.config['PRINTER_NAME'] = "Brother_HL_L2305_series"
app.config['PRINTER_NAME'] = ""

cups_conn = cups.Connection()
IPPError = cups.IPPError()
files = glob.glob("print-files/*.txt")

PRINTER_NAME = app.config['PRINTER_NAME']
IPP_ERROR = "ipp error"

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/print_test', methods=['POST'])
def print_test():
    try:
        cups_conn.printTestPage(PRINTER_NAME)
    except IPPError:
        printer_error(IPP_ERROR)
    else:
        return make_response(jsonify({'status': 'OK'}), 200)



@app.route('/print_file', methods=['POST'])
def print_file():
    filename =  random.choice(files)
    try:
        cups_conn.printFile(PRINTER_NAME, filename, "job", {})
    except IPPError:
        printer_error(IPP_ERROR)
    else:
        return make_response(jsonify({'status': 'OK'}), 200)


@app.errorhandler(500)
def five_hundred(error):
    return make_response(jsonify({'error': 'Server Error'}), 500)


def printer_error(error_message):
    print(error_message)
    return make_response(
        jsonify({
            'status': 'ERROR',
            'error': error_message
        }), 200)
