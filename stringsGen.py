#stringsGen
import numpy as np
import pandas as pd
import string
import random

# part of the StringuX attributes. The string attribute is completed in 
# two steps. first generate the random part of the string (randomString())
# then tack on the string of Xs to the end (fullString()). 
def randomString(stringLength = 7):
    # generate a string of a fixed length
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def fullString():
    # append 45 Xs to the string. Split into to 
    trailingX ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # 45 Xs
    return "{}{}".format(randomString(7),trailingX)             # concatenate output


# generate strings attributes stringu1 and stringu2
def string_u(maxtuples):            
    stringu = np.chararray(0)           # allocate char array
    stringu = stringu.astype('U52')     # set size to allow for 52 char string
    for i in range(maxtuples):          # fill the array with the random strings 
        stringu = np.append(stringu, fullString())  # to size maxtuples

    return stringu

def stringFour(maxtuples):
    #STRING4 DATA
    string4 = np.chararray(0)
    string4 = string4.astype('U52')
    #create a matching sized set of TENKTUP by appending the cycle of four, 
    # maxtuples must be divisible by 4 or the output will error, since the
    # arrays will not be of equal lengths.  
    for i in range(maxtuples//4):
        string4 = np.append(string4,"AAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        string4 = np.append(string4,"HHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        string4 = np.append(string4,"OOOOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        string4 = np.append(string4,"VVVVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    return string4

#convert to pandas dataframe for ease of CSV file creation
#string4 = pd.DataFrame(string4)
#string4.to_csv('string_4.csv')

#print(string_u(8))
