from collections import deque

def solution(x, y):
    '''
    Based on Breadth First Search to get the smallest number of 
    moves it will take for you to travel from the source square 
    to the destination square using a chess knight's moves
    BFS:
    1. Enqueue src_x, src_y, and the number of moves as root.
    2. Dequeue a node and compare.
    3. If dest_x, dest_y found, quit search and 
       return the number of moves for the node.
    4. Otherwise enqueue direct child nodes whose x and y 
       coordinates are both within the valid boundaries, 
       as well as the number of moves to reach them.
    5. If queue not empty, repeat from step 2.
    Parameters:
        x, y (int): The integers represent the source square 
            and the destination square respectively.
    Returns:
        moves (int): The minimum moves to travel from the 
            source square to the destination square.
    '''
    # Set the boundary.
    N = 8
    # Transform the provided square into x, y coordinates.
    src_y, src_x = divmod(x, N)
    dest_y, dest_x = divmod(y, N)
    # Valid directions.
    knight_moves = ((1,2),(1,-2),(-1,2),(-1,-2),
                    (2,1),(2,-1),(-2,1),(-2,-1))
    # Record if the node has been visited.
    visited = set()
    # Record the number of moves.
    moves = 0
    # Step 1.
    Q = deque([(src_x, src_y, moves)]) 
    while Q:
        # Step 2.
        curr_x, curr_y, moves = Q.popleft()
        # Step 3.
        if (curr_x, curr_y) == (dest_x, dest_y):
            return moves
        # Step 4.
        for dx, dy in knight_moves:
            new_x, new_y = curr_x+dx, curr_y+dy
            if (0<=new_x<=N) and (0<=new_y<=N)\
              and ((new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                Q.append((new_x, new_y, moves+1))
    return -1
