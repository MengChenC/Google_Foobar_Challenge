def floyd_warshall(times):
    '''
    Function transforms the given matrix into the result 
    of "all pairs shortest paths" via Floyd-Warshall algorithm.
    1. Update the current path if the new path through a middle 
       node is shorter.
    2. Repeat n times (n = num_nodes) to ensure the path length 
       reductions are traversed through.
    3. Repeat 2 again, if a path through a middle node turns out 
       still shorter, there is a negative cycle. Represent that 
       path with negative infinity.
    '''
    n_nodes = range(len(times))
    for stage in [1, 2]:
        for k in n_nodes:
            for i in n_nodes:
                for j in n_nodes:
                    path_len = times[i][k] + times[k][j]
                    if path_len < times[i][j]:
                        times[i][j] = path_len if stage==1\
                                      else float('-inf')

def solution(times, time_limit):
    '''
    Function returns a list containing the maximum indexes of bunnies
    that can be rescued, sorted by lowest bunny worker ID.
        1. Find the time for reaching the first bunny.
        2. Find the time for reaching the exit from that bunny;
           if time exceeds, the path is not valid.
        3. If time allows, find the time from this bunny to the next 
           one; if time exceeds, the path is also not valid.
        4. If time allows, check if exit is reachable. 
        5. If so, then both bunnies are saved.
        6. We extend the logic to all bunnies by traversing the entire 
           graph while keeping track of the maximum set of saved bunnies.
    '''
    idx_bulkhead = len(times) - 1
    n_bunnies = idx_bulkhead - 1
    
    # If there's no bunnies to save from the original matrix.
    if n_bunnies == 0: 
        return []
        
    # Transform the original matrix in-place to DP table
    # leveraging the fact that Python is pass-by-reference.
    floyd_warshall(times)
    
    idx_start = 0
    range_bunnies = range(idx_start+1, idx_bulkhead)
    
    # Python 2.7 has no nonlocal closure.
    # Just allows accessing nonlocal variables, not rebinding them.
    # Use list's mutability as a workaround.
    bool_saved_all = []

    def get_curr_max_bunnies(curr_node, curr_time, visited_bunnies, saved_bunnies):
        '''
        Helper function for recursion.
        '''
        # We have found a way to save all, so exit early.
        if bool_saved_all: 
            return saved_bunnies
        elif len(saved_bunnies) == n_bunnies:
            bool_saved_all.append(True)
            return saved_bunnies
            
        curr_max_bunnies = saved_bunnies
        
        # Loop over the path to update the rescue list.
        for next_bunny in range_bunnies:
            if next_bunny in visited_bunnies: 
                continue
                
            new_visited_bunnies = visited_bunnies.copy()
            new_visited_bunnies.add(next_bunny)
            time_to_next_bunny = times[curr_node][next_bunny]
            time_to_escape = times[next_bunny][idx_bulkhead]

            if curr_time+time_to_next_bunny+time_to_escape > time_limit: 
                continue

            new_saved_bunnies = list(saved_bunnies)
            new_saved_bunnies.append(next_bunny-1)

            success_next_bunny = get_curr_max_bunnies(
                curr_node = next_bunny,
                curr_time = curr_time+time_to_next_bunny,
                visited_bunnies = new_visited_bunnies,
                saved_bunnies = new_saved_bunnies
            )
            
            # Only update when the new list is longer,
            # this will keep the lowest ID first when equal sizes.
            if len(success_next_bunny) > len(curr_max_bunnies): 
                curr_max_bunnies = success_next_bunny
        return curr_max_bunnies
        
    final_max_bunnies = get_curr_max_bunnies(
        curr_node = idx_start,
        curr_time = 0,
        visited_bunnies = set(),
        saved_bunnies = []
    )
    final_max_bunnies.sort()
    return final_max_bunnies
