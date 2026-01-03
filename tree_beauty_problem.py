import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def build_tree(n, par):
    children = [[] for _ in range (n+1)]
    
    for i in range(1, n+1):
        parent = par[i-1]
        if parent != 0:
            children[parent].append(i)
    
    return children

def get_subtree_nodes(node, children, visited):
    
    visited.add(node)
    subtree = [node]
    
    for child in children[node]:
        if child not in visited:
            subtree.extend(get_subtree_nodes(child, children, visited))
        
    return subtree

def count_good_pairs(nodes, a):
    count = 0
    n = len(nodes)
    
    for i in range(n):
        for j in range(i+1, n):
            node_i = nodes[i]
            node_j = nodes[j]
            
            val_i = a[node_i - 1]
            val_j = a[node_j - 1]
            
            product = val_i * val_j
            if is_perfect_square(product):
                count +=1
                
    return count

def get_ans(n, par, a):
    '''
    Docstring for get_ans
    
    :param n: number of nodes
    :param par: parent array (par[0] should be 0 for root node)
    :param a: values at each node
    '''
    
    MOD = 10**9 + 7
    children = build_tree(n, par)
    
    total_beauty = 0
    
    for node in range(1, n+1):
        visited = set()
        subtree_nodes = get_subtree_nodes(node, children, visited)

        beauty = count_good_pairs(subtree_nodes, a)
        
        total_beauty += beauty
        
    return total_beauty % MOD


def test_case_1():
    """
    Tree:     1(2)
             / \
          2(3)  3(6)
          / \
       4(12) 5(27)
    """
    n = 5
    par = [0, 1, 1, 2, 2]
    a = [2, 3, 6, 12, 27]
    
    result = get_ans(n, par, a)
    print(f"Test Case 1: {result}")
    print(f"Expected: 6")
    print(f"Match: {result == 6}\n")
    
test_case_1()