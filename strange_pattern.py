import numpy as np

# implement the function strange pattern

def strange_pattern(dims):
    boolarray = np.zeros((dims[0], dims[1]), dtype=bool)
    i = 0;
    while (i < dims[0]):
        boolarray[i][-i%3::3] = True
        i+= 1
    return boolarray


if __name__ == "__main__":
    print(strange_pattern((6,8)))
