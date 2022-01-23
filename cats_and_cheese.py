from collections import deque

# Challenge 1
def balanced_symbols(input_string: str="")->bool:
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
def cost_prorating(cost: int, weights : list)->list:
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


# Challenge 3
def water_jugs(target:float, capacities: list) -> str:
    """
    Given a set of jugs' capacities and a target volume, this function returns a minimal sequence
    of pouring operations to reach a state where at least one jug has the target volume of water in it.
    If no sequence exists, it returns None.

    BFS algorithm is used for this implementation of N-water jugs.

    Parameters
    ----------
    target: float
        Target volume of water.
    capacities: list
        Set of jugs' capacities.
    
    Returns
    -------
    str
        The minimum steps in format source -> destination : states.
        Where:
            source: the jug to pour from, or -1 to fill from the faucet
            destination: the jug to pour into, or -1 to empty into the sink
            states: the state of each jug, i.e. its volume of water, after the pouring operation

    Examples
    --------
    >>> water_jugs(target=4, capacities=[3, 5])
    -1 -> 1 : (0, 5)
    1 -> 0 : (3, 2)
    0 -> -1 : (0, 2)
    1 -> 0 : (2, 0)
    -1 -> 1 : (2, 5)
    1 -> 0 : (3, 4)
    >>> water_jugs(target=15, capacities=[1, 2, 10, 20])
    -1 -> 3 : (0, 0, 0, 20)
    3 -> 0 : (1, 0, 0, 19)
    3 -> 1 : (1, 2, 0, 17)
    1 -> -1 : (1, 0, 0, 17)
    3 -> 1 : (1, 2, 0, 15)
    """
    if type(target) != int and type(target) != float:
        raise TypeError("The parameter 'target' should be a float.")
    
    if target <= 0:
        raise ValueError("The 'target' should be greater than zero.")
    
    if type(capacities) != list:
        raise TypeError("The parameter 'capacities' should be a list of integers.")
    
    if len(capacities) == 0:
        raise ValueError("The 'capacities' list should not be empty.")
    
    for capacity in capacities:
        if type(capacity) != int and type(capacity) != float:
            raise TypeError("Each of the jugs' capacities should be float or int.")
        if capacity <= 0:
            raise ValueError("Each of the weights should be greater than 0.")
        
    def fill_a_jug(state, capacities):
        possible_states, prev_states, pouring_ops = [], [], []
        for i in range(len(capacities)):
            temp = list(state)
            temp[i] = capacities[i]
            possible_states.append(temp)
            prev_states.append(state)
            pouring_ops.append([-1, i])

        return possible_states, prev_states, pouring_ops

    def empty_a_jug(state):
        possible_states, prev_states, pouring_ops = [], [], []
        for i in range(len(state)):
            temp = list(state)
            temp[i] = 0
            possible_states.append(temp)
            prev_states.append(state)
            pouring_ops.append([i, -1])
        
        return possible_states, prev_states, pouring_ops

    def pour_a_jug_into_another(state, capacities):
        possible_states, prev_states, pouring_ops = [], [], []
        for i in range(len(state)):
            for e in range(len(state)):
                temp = list(state)
                if e == i: continue
                diff = min(state[i], capacities[e] - temp[e])
                temp[i] = temp[i] - diff
                temp[e] = temp[e] + diff
                possible_states.append(temp)
                prev_states.append(state)
                pouring_ops.append([i, e])
                
        return possible_states, prev_states, pouring_ops
    
    states_queue = deque()
    ops_queue = deque()
    prevs_queue = deque()
    path = []
    ops = []
    prevs = []
    searched = []
    solution = ""

    states_queue.append([0 for i in range(len(capacities))])
    ops_queue.append([0 for i in range(len(capacities))])
    prevs_queue.append([0, 0])

    while len(states_queue) > 0:
        state = states_queue.popleft()
        op = ops_queue.popleft()
        prev = prevs_queue.popleft()

        if state in searched:
            continue
        
        path.append(state)
        ops.append(op)
        prevs.append(prev)
        searched.append(state)

        for s in state:
            if s == target:
                i = len(path) - 1
                while i != 0:
                    state_tuple = tuple(path[i])
                    solution = "{} -> {} : {}\n".format(ops[i][0], ops[i][1], state_tuple) + solution
                    i = path.index(prevs[i])
                return solution

        # fill a jug from the faucet
        possible_states, prev_states, pouring_ops = fill_a_jug(state, capacities)
        for possible_state, prev_state, pouring_op in zip(possible_states, prev_states, pouring_ops):
            states_queue.append(possible_state)
            prevs_queue.append(prev_state)
            ops_queue.append(pouring_op)

        # empty a jug in the sink
        possible_states, prev_states, pouring_ops = empty_a_jug(state)
        for possible_state, prev_state, pouring_op in zip(possible_states, prev_states, pouring_ops):
            states_queue.append(possible_state)
            prevs_queue.append(prev_state)
            ops_queue.append(pouring_op)

        # pour a jug into another jug
        possible_states, prev_states, pouring_ops = pour_a_jug_into_another(state, capacities)
        for possible_state, prev_state, pouring_op in zip(possible_states, prev_states, pouring_ops):
            states_queue.append(possible_state)
            prevs_queue.append(prev_state)
            ops_queue.append(pouring_op)
                


