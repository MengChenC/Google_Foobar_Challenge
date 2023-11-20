def solution(n):
    '''
    Function takes a positive integer n and returns the 
    number of different staircases that can be built from 
    exactly n bricks.
    Parameters:
        n (int): n>=3, the number of bricks we can use.
    Return:
        total (int): number of possible combinations we 
        have for building the staircases.
    '''
    # For safety and completeness.
    if n < 3:
        return 0
    # Initialize the table.
    memo = [[0 for _ in range(n+2)]
               for _ in range(n+2)]
    # Base case, when bricks = 3 or 4.
    # (Steps must = 2 in both cases.)
    memo[3][2] = memo[4][2] = 1
    # Fill the table from bottom up.
    # i is num of bricks, j is num of steps.
    # Then start from bricks = 5,
    # and steps from at least 2.
    for i in range(5, n+1):
        for j in range(2, i+1):
            # When steps == 2,
            # cumulate from also 2 steps
            # but with 2 fewer bricks.
            if j == 2 :
                memo[i][j] = memo[i-j][j] + 1
            # When steps > 2,
            # cumulate from the bricks - steps
            # with same steps and one step fewer
            # respectively.
            else :
                memo[i][j] = memo[i-j][j] +\
                             memo[i-j][j-1]
    # Count the total possibilities for n.
    total = 0
    for i in range(1, n+1):
        total += memo[n][i] 
    return total
