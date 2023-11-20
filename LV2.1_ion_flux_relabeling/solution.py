def get_parent_node(h, converter):
    '''
    Helper function to get the parent index for a converter.
        Parameters:
            h (int): The height of the perfect tree.
            converter (int): Positive integer representing 
                different flux converter.
        Returns:
            prev_node (int): The label of the converter that 
                sits on top of the respective converter, 
                or -1 if there is no such converter.
    '''
    # Initialize values.
    # Current node starts as the maximum indexes 
    # we can have based on the height.
    # subtree will be the number of elements we have for a node.
    prev_node = -1
    curr_node = 2**h-1
    subtree = 2**h-1
    
    # Tackle root node.
    if converter == curr_node:
        return prev_node
        
    # Traverse the tree if the height > 1.
    while subtree > 1:
        # Current node becomes previous node when traversal starts
        # since there is no match for the current node.
        prev_node = curr_node
        # The subtree elements halve when going down a layer.
        subtree = subtree//2
        # Update left_node and right_node accordingly.
        left_node = curr_node-subtree-1
        right_node = curr_node-1
        
        if converter == left_node or converter == right_node:
            return prev_node
        # Go left if converter < left_node otherwise go right.
        curr_node = left_node if converter < left_node else right_node

    # If no match at all, return -1.
    # (Although all values in q are constrainted between 2 and 2^h-1,
    # including this for function safety.)
    return -1


def solution(h, q):
    '''
    Function solves the labels for the converters that sit on 
        top of the respective converters.
        Parameters:
            h (int): The height of the perfect tree.
            q (list): A list of positive integers representing 
                different flux converters.
        Returns:
            (list): A list of integers where each element is 
                the label of the converter that sits on top 
                of the respective converter in q, or -1 
                if there is no such converter.
    '''
    return [get_parent_node(h, converter) for converter in q]

