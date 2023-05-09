#from distutils.command.clean import clean
#from string import printable
import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
   clean_samples = []
   if not ( type(loc) | type(scale) | type(upper_bound) | type(lower_bound) is type(2) or type(0.21)) :
       #raise TypeError ("only integers or floats are allowed!")
       print ("Only integers or floats are allowed!")
       return None
   
   if(lower_bound> upper_bound):
       print ("lower bound must be <= upper_bound!")
       return None
       
   samples = np.random.normal(loc,scale,100)
   for i in samples:
       if (upper_bound >= i and i >= lower_bound):
           clean_samples = np.append(clean_samples,i)

   print(lower_bound)
   print(upper_bound)
   return (np.mean(clean_samples), np.std(clean_samples))



   
   
   return None


if __name__ == "__main__":
    print(gaussian_analysis(1,2,0,10))

    pass
