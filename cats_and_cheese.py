# Challenge 1
def balanced_symbols(input_string: str=""):
    """
    Checks whether an input string is properly balanced with respect to '(' and ')', 
    '[' and ']' and '{' and '}'. The function ignores the symbols within comments, a comment starts 
    with a '/*' and end with '*/'.

    Parameters
    ----------
    input_string: str
        Input string to evaluate.

    Returns
    -------
    bool
        True if the 'input_string' is balanced, False otherwise.

    Examples
    --------
    >>> balanced_symbols("({[()[]]})")
    True
    >>> balanced_symbols("/* abcd /* efgh */ ijkl */")
    False
    >>> balanced_symbols("/*")
    False
    """
    if type(input_string) != str:
        raise TypeError("The parameter 'input_string' should be a string.")

    opening = set('([{')
    closing = set(')]}')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    i = 0
    inside_comment = False

    while i < len(input_string):
        if(input_string[i] == "/") and ((i+1) < len(input_string)) and not inside_comment:
            if input_string[i+1] == "*":
                inside_comment = True
                i += 1

        elif(input_string[i] == "*") and ((i+1) < len(input_string)) and inside_comment:
            if input_string[i+1] == "/":
                inside_comment = False
                i +=1

        elif(input_string[i] == "*") and ((i+1) < len(input_string)) and not inside_comment:
            return False
        
        elif(input_string[i] in opening) and not inside_comment:
            stack.append(input_string[i])

        elif(input_string[i] in closing) and not inside_comment:
            if len(stack) == 0:
                return False
            elif (stack[-1], input_string[i]) in matches:
                stack.pop()
            else:
                return False
        i += 1
    
    if len(stack) == 0 and not inside_comment:
        return True
    else:
        return False

# Challenge 2
def cost_prorating(cost: int, weights : list):
    """
    Returns the distribution of a cost proportionally to a set of  weights, maintaining the order 
    of the input weights. The total amount of the distribution is the input cost.

    Parameters
    ----------
    cost: int
        Cost to distribute.
    weights: list
        Set of weigths.

    Returns
    -------
    list
        Cost distribution as a list of integers.

    Examples
    --------
    >>> cost_prorating(10, [2, 5])
    [3, 7]
    >>> cost_prorating(10, [1, 0])
    [10, 0]
    >>> cost_prorating(123, [1, 2, 3, 4, 5, 6])
    [6, 12, 18, 23, 29, 35]
    """
    if type(cost) != int:
        raise TypeError("The parameter 'cost' should be an int.")
    
    if cost < 0:
        raise ValueError("The cost should be greater or equal to zero.")

    if type(weights) != list:
        raise TypeError("The parameter 'weights' should be a list of integers.")
    
    if len(weights) == 0:
        raise ValueError("The 'weights' list should not be empty.")
    
    all_zero = True
    for weight in weights:
        if type(weight) != int:
            raise TypeError("Each of the weights should be integers.")
        if weight < 0:
            raise ValueError("Each of the weights should be greater or equal to 0.")
        if weight != 0:
            all_zero = False
    
    if all_zero:
        raise ValueError("There should be at least one non-zero weight.")
        

    rounded_cost_distribution, relative_rounding_errors = [], []
    weights_sum = sum(weights)

    for weight in weights:
        rounded_cost_distribution.append(round(cost/weights_sum*weight))
        if weight == 0: 
            relative_rounding_errors.append(0)
        else:
            relative_rounding_errors.append((cost/weights_sum*weight-round(cost/weights_sum*weight))/weight)
    
    diff = sum(rounded_cost_distribution) - cost

    while diff != 0:
        min_error, max_error = 1, -1
        idx = 0
        if diff > 0:
            for i in range(len(relative_rounding_errors)):
                if min_error > relative_rounding_errors[i]:
                    min_error = relative_rounding_errors[i]
                    idx = i

            rounded_cost_distribution[idx] -= 1
            relative_rounding_errors[idx] = 0

        else:
            for i in range(len(relative_rounding_errors)):
                if max_error < relative_rounding_errors[i]:
                    max_error = relative_rounding_errors[i]
                    idx = i

            rounded_cost_distribution[idx] += 1
            relative_rounding_errors[idx] = 0

        diff = sum(rounded_cost_distribution) - cost

    return rounded_cost_distribution
