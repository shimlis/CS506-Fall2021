def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    
    return res
    

def jaccard_dist(x, y):
    if len(x) == 0:
        return 0
    
    inter = set(y).intersection(x)
    union = set(y).union(x)

    return 1 - (inter/union)

#helper function
def vector_prodcut(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

def cosine_sim(x, y):
    return vector_prodcut(x,y) / ( (vector_prodcut(x,x) **.5) * (vector_prodcut(y,y) ** .5) )
    

