import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a1,a2,axis = 0):
    # delete the NotImplementedError when you write your function.
    try: 
         return np.concatenate(a1,a2,axis)

    except:
        print ("The combination appears to be impossible!")
        return None


if __name__ == "__main__":
    # use this for your own testing!

    pass
