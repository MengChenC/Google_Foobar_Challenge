def simplify_xor(n):
    '''
    Helper function to simplify the XOR calculation
    utilizing patterns in finding XOR in range(0, n),
    (all n is inclusive hereafter):
    result = n if n%4==0
    result = 1 if n%4==1
    result = n+1 if n%4==2
    result = 0 if n%4==3
    Parameters:
        n(int): The length to be performed XOR from 0.
    Returns:
        result(int): XOR result for all elements from
            0 to n.
    '''
    results = [n, 1, n+1, 0]
    return results[n%4]

def solution(start, length):
    '''
    Function covers for the missing security checkpoint
    by outputting the same checksum the trainers would 
    normally submit before lunch.
    Parameters:
        start(int): The ID of the first worker to be checked.
        length(int): The length of the line.
    Returns:
        result(int): Checksum based on XOR(^).
    '''
    # Record the result.
    result = 0
    # Reverse the order, so every line gets to skip one element.
    for i in range(length, 0, -1):
        # Update result when looping over each line.
        # Since reduce(operator.XOR, range(start, start+i), result)
        # is not fast enough for the test data, we have to leverage
        # the associate nature of XOR (both a,b inclusive):
        # XOR(a to b) = XOR(0 to b) ^ XOR(0 to a-1).
        result ^= (simplify_xor(start+i-1)) ^ (simplify_xor(start-1))
        # The difference among each element between current line 
        # and next line is the value of length.
        start += length
    return result
