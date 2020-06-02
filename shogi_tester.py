import random

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def random_test_data(data_in, data_out):
    '''
    Take out random data from test data. (and associated result)
    Input:
        - data_in (numpy.ndarray): input test data for model
        - data_out (numpy.ndarray): output test data for model
    
    Output:
        Tuple containing random input and output test data.
    '''

    # take out random integer in range of 0 to length of data
    length_of_data = len(data_out)
    random_index = random.randint(0, length_of_data-1)

    return (random_index, data_in[random_index], data_out[random_index])

