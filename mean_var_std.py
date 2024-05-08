import numpy as np

def calculate(list):

    answer = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }


    if len(list)<9:
        raise ValueError("List must contain nine numbers.") 

    numpArray = np.array(list)

    matrix = numpArray.reshape((3,3))

    #mean
    answer['mean'] = [matrix.mean(0).tolist(),matrix.mean(1).tolist(),matrix.mean()]

    #variance
    answer['variance'] = [matrix.var(0).tolist(),matrix.var(1).tolist(),matrix.var()]

    #standard deviation
    answer['standard deviation'] = [matrix.std(0).tolist(),matrix.std(1).tolist(),matrix.std()]

    #max
    answer['max'] = [matrix.max(0).tolist(),matrix.max(1).tolist(),matrix.max()]

    #min
    answer['min'] = [matrix.min(0).tolist(),matrix.min(1).tolist(),matrix.min()]

    #sum
    answer['sum'] = [matrix.sum(0).tolist(),matrix.sum(1).tolist(),matrix.sum()]

    
    return answer
