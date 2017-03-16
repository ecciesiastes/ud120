#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    import numpy as np
    import math
    type = np.dtype({'names': ['age', 'net_worth', 'error'],
                     'formats': [np.int16, np.float32, np.float32]}, align=True)
    data = np.zeros((len(ages)), dtype=type)

    for i in range(0, len(ages)):
        data[i]["age"] = ages[i][0]
        data[i]["net_worth"] = net_worths[i][0]
        data[i]["error"] = math.pow((net_worths[i][0] - predictions[i][0]), 2)

    data.sort(order='error')

    size = int(len(ages) * 0.9)

    cleaned_data = data[:size]

    return cleaned_data
