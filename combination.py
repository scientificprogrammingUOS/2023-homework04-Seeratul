import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a1,a2,axis = 0):
    # delete the NotImplementedError when you write your function.
    try: 
         a1 = np.squeeze(a1)
         a2 = np.squeeze(a2)
         return np.concatenate((a1,a2),axis)

    except:
        print ("The combination appears to be impossible!")
        return None


if __name__ == "__main__":
    #use this for your own testing!
    a1 = np.ones((2,2))
    a2 = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    print(combination(a1,a2))
    pass
