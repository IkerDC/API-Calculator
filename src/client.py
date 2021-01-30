import requests

#URL
BASE = "http://127.0.0.1:7000/"

def call_API(operation):
    '''
    Function that will call the api

    :param operation: String containing the operation to be computed.
    :return: Response from the API
    '''
    #First replace every possible divide sign by | if there are so it does not mess up with our call.
    operation = operation.replace('/','|')

    #Do the call
    response = requests.get(BASE + 'calculate/' + operation).json()
    return response



print('This calculator will read an input operation and computed, for instance:\n'
      '25*123, or 123+784, ... The operations allowed are +,-,*,/,%,^.\n')

#Menu and call
comp = True
while comp:
    print('Introduce the full operation:')
    x = input()
    print(call_API(x))
    print('[0]: Exit \n'
          '[1]: Compute another operation')
    cont = input()
    if cont != '1':
        comp = False
