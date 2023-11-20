def solution(x, y):
    '''
    Function to get the minimum cycles of replication
    needed for the target amount of bombs.
    Parameters:
        x, y (str): The target number of Mach and Facula 
            bombs respectively.
    Returns:
        cycles (str): The minimum cycles, or 'impossible'
            if the target is infeasible.
    '''
    x, y = int(x), int(y)
    # Record the cycles.
    cycles = 0
    # We go backward, always use the larger number to 
    # subtract the smaller one.
    while True:
        # Until there is a solution when x==y==1.
        if x==1 and y==1:
            return str(cycles)
        # Otherwise there is no solution when x==y!=1,
        # or x or y==0 but their counterpart !=1.
        if x==0 or y==0 or x==y:
            return 'impossible'
        # We have to use division to quickly calculate the 
        # cycles, and use modular division to update x and y.
        # Also need to tackle special case when either x or y==1 
        # since we set one stopping point at x==y==1.
        if x>y:
            if y == 1:
                cycles += x//y - 1
                x = 1
            else:
                cycles += x//y
                x %= y
        else:
            if x == 1:
                cycles += y//x - 1
                y = 1
            else:
                cycles += y//x
                y %= x
