# dataGen.py
# Djernaes/Ku
# CS487 "Scalable" Wisconsin Benchmark Implementation Project

# need stringsGen.py as a dependency
import numpy as np
import pandas as pd
from stringsGen import string_u, stringFour


# generate 'maxtuples' per given input
def dataGenerator(maxtuples):
    # Uniques
    unique_1 = np.arange(0, maxtuples)
    unique_3 = np.arange(0, maxtuples)
    unique2 = np.arange(0, maxtuples)  # unique2 (id numbers 0 to size-1)
    unique1 = np.random.permutation(unique_1)  # unique1 is a random ordering of numbers from 0 to size-1
    unique3 = np.random.permutation(unique_3)  # randomized unique1
    # Raw integers
    two = unique1 % 2
    four = unique1 % 4
    ten = unique1 % 10
    twenty = unique1 % 20
    # Percentages
    onePercent = unique1 % 100
    tenPercent = unique1 % 10
    twentyPercent = unique1 % 5
    fiftyPercent = unique1 % 2
    evenOnePercent = onePercent * 2
    oddOnePercent = (onePercent * 2) + 1

    stringu1 = string_u(unique1)  # see stringsGen.py for defs
    stringu2 = string_u(unique2)  # see stringsGen.py for defs

    string4 = stringFour(maxtuples)  # see stringsGen.py for defs

    # assemble attributes for dataframe export
    df = {'unique1': unique1, 'unique2': unique2, 'two': two, 'four': four, 'ten': ten,
          'twenty': twenty, 'onePercent': onePercent, 'tenPercent': tenPercent, 'twentyPercent': twentyPercent,
          'fiftyPercent': fiftyPercent, 'unique3': unique3, 'evenOnePercent': evenOnePercent,
          'oddOnePercent': oddOnePercent, 'stringu1': stringu1, 'stringu2': stringu2, 'string4': string4}
    df1 = pd.DataFrame(data=df)

    return df1


"""  main()  """
# NOTE: maxtuples must be divisible by 4, otherwise program 
# will error. This is due to string4's attribute structure.
# 10K, 100K, 1M will all work. 
maxtuples = 1000
finaltup = dataGenerator(maxtuples)

""" test output, print to screen """
# print(testTup)

# export to CSV file
# Rename output file with desired title 
""" uncomment the next line to output to file """
# finaltup.to_csv('testTuples.csv')

finaltup.to_csv('tenmiltup.csv')
print("file complete")
