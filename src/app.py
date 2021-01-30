from flask import Flask, send_file
import calculator as calc
import json
import os

app = Flask(__name__)
@app.route('/calculate/<string:string_operation>', methods = ['GET'])
def calculate(string_operation):

    #First replace the character for the division
    string_operation = string_operation.replace('|','/')

    #Do the computation
    correct, operator = calc.is_op_correct(string_operation)
    #return string_operation + operator
    if(correct):
        n1, op, n2 = calc.getnums_and_op(string_operation, operator)
        result = calc.calculate(n1, op, n2)
        return json.dumps('The result is: ' + str(result))

    else:
        return json.dumps('The operation introduced is not correct.')

if __name__ == '__main__':
    app.run(debug=True, port=7000)


