def is_prime(n):
    '''
    Helper function to decide if n is a prime.
        Parameters:
            n (int): The number to be checked.
        Returns:
            (boolean): True if a prime, False otherwise.
    '''
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def prime_generator():
    '''
    Generator for lazy implementation of getting prime sequence.
        Yields:
            n (int): A prime number.
    '''
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def solution(i):
    '''
    Function takes in a starting index i and returns the next 
    five digits in a string of all primes.
        Parameters:
            i (int): The starting index.
        Returns:
            result[:5] (str): A slice of string of five digits 
            from the starting index in the prime string.
    '''
    # Create the generator object
    primes = prime_generator()
    result = ''
    # Loop till result contains more than five digits
    while len(result) < 5:
        prime_str = str(next(primes))
        prime_len = len(prime_str)
        # Each round we subtract prime_len from target index i.
        # And when i falls shorter than a prime_len, we start 
        # to record the digits of the prime from current index i
        # to the next five.
        if i <= prime_len:
            result += prime_str[i:i+5]
        # When i == 0, we still need to loop till result has 
        # more than five digits, hence we take max(0, _) here.
        i = max(0, i-prime_len)
    return result[:5]
