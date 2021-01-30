import operator

def is_op_correct(calcul):
    '''
    This function will look for the operation that teh user wants to performed. The ones available are
    +, -, /, *, %,^.

    :param calc: The operation introduced by the user
    :return: The operation required to be performed
    '''

    #Find the operation on the 'equation'
    ops = ['+','-','/','*','%','^']

    #Count how many operators we have and store the operator found/s
    occrs = 0
    op = ''
    not_alpha = False
    #Check if the character is a number and if we only have one operator. Plus if the operator is not at the start nor end
    for a in calcul:
        if (a.isdigit() or (a in ops and (a != calcul[0] and a != calcul[len(calcul)-1]))):
            if (a in ops):
                occrs += 1
                op = a
        else:
            not_alpha = True
    #Have we found only a sign, and all the rest are numbers?
    if((occrs != 1) or not_alpha):
        return False, op
    else:
        return True, op

def getnums_and_op(calcul, op):
    '''
    Return the operations separated by numbers and operator.
    :param calc: Full string with the operation.
    :param op: Operator found if is_op_correct is true
    :return:
    '''
    #Find where the operator is and return the number
    op_pos = calcul.find(op)
    return calcul[0:op_pos], op, calcul[op_pos+1:]

def calculate(n1, op, n2):
    '''
    Calculate the operation
    :param n1: First number
    :param op: Operator
    :param n2: Second number
    :return: Result
    '''
    #Lookup table
    operate = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul, "%": operator.mod, "^": operator.pow}
    if (op == '/' and n2 == '0'):
        calcul = 'Good try! But when you divide by 0 some really bad things happen. So, do not do it.'
    else:
        calcul = operate[op](int(n1),int(n2))
    return calcul


