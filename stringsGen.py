# stringsGen
import numpy as np


# part of the StringuX attributes.
def convert_to_string(unique):
    # generate a string of a fixed length
    result = ["A"] * 7
    i = 6
    cnt = 0
    tmp = [" "] * 7
    # convert unique value from right to left into an alphabetic string in result
    while unique > 0:
        rem = unique % 26
        tmp[i] = chr(ord('A') + rem)
        unique = unique // 26
        i -= 1
        cnt += 1

    # This could be implemented more elegantly in python, but where's the fun in that?
    # Not certain this loop is necessary, since lots of student-written scripts don't include it...
    for j in range(cnt + 1):
        result[j] = tmp[i]
        i += 1

    return ''.join(result) + ("x" * 45)


# generate strings attributes stringu1 and stringu2
def string_u(unique_arr):
    stringu = np.chararray(0)  # allocate char array
    stringu = stringu.astype('U52')  # set size to allow for 52 char string
    for i in range(len(unique_arr)):  # fill the array with the random strings
        stringu = np.append(stringu, convert_to_string(unique_arr[i]))  # to size maxtuples
        if i % 1000 == 0:
            print('Record: ' + str(i))

    return stringu


def stringFour(maxtuples):
    # STRING4 DATA
    string4 = np.chararray(0)
    string4 = string4.astype('U52')
    # create a matching sized set of TENKTUP by appending the cycle of four,
    # maxtuples must be divisible by 4 or the output will error, since the
    # arrays will not be of equal lengths.  
    for i in range(maxtuples // 4):
        string4 = np.append(string4, "AAAA" + ('x' * 48))
        string4 = np.append(string4, "HHHH" + ('x' * 48))
        string4 = np.append(string4, "OOOO" + ('x' * 48))
        string4 = np.append(string4, "VVVV" + ('x' * 48))
    return string4

