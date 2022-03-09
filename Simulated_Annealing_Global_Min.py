#----------------------------------------------------------------------#
#                   Simulated Annealing Project                        #
#           SIAM Hundred-Dollar, Hundred-Digit Challenge               # 
#               (Written by Nick Trefethen - 2002)                     #
#        Question Number 4 -Find Complicated Function Global Minimum   #
#----------------------------------------------------------------------#
#
#----------------------------------------------------------------------#
#                         Presented by:                                #
#                Tomer Grossman & Oriel Somech                         #
#             Computer Science Students - 2'nd Year, CLB               #  
#----------------------------------------------------------------------#
#
#----------------------------------------------------------------------#
#                 !!  IMPORTANT PRE-RUNNING:  !!                       #  
#          Install frigidum & numpy packages on your IDE               #
#                      BEFORE Debbuging!                               #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
import frigidum    #Simulated Annealing Package - Make sure the package is installed on your IDE
import numpy as np #Math operations library - Make sure the package is installed on your IDE
import random      #random numbers calculations library
import math        #math geometric functions & arithmetic operations library

# Objective function
def math_func(X): 
  x, y = X 
  return (math.exp(math.sin(50 * x)) + math.sin(60 * math.exp(y)) + math.sin(70 * math.sin(x)) + math.sin(math.sin(80 * y)) - math.sin(10 * (x + y)) + 0.25 * (math.pow(x, 2) + math.pow(y, 2)))

# Get random float x,y parameters for begining point as initial current point
def random_begin():
    return np.random.random(2) 

# Move by small step from current point on objective funtcion
def random_little_move(x): 
    if np.random.random() < 0.5:
        return np.clip(x + np.array([0, 0.02 * (random.random() - 0.5)]), -4, 4)
    else:
        return np.clip(x + np.array([0.02 * (random.random() - 0.5), 0]), -4, 4)

# Move by big step from current point on objective funtcion
def random_large_move(x): 
    if np.random.random() < 0.5:
        return np.clip(x + np.array([0, 0.5 * (random.random() - 0.5)]), -4, 4)
    else:
        return np.clip(x + np.array([0.5 * (random.random() - 0.5), 0]), -4, 4)

# SA system method for finding global minimum
Simulated_Annealing = frigidum.sa(random_start=random_begin,  
                                  neighbours=[random_little_move, random_large_move],
                                  objective_function=math_func,T_start=10**2,
                                  T_stop=0.1,repeats=10**4,
                                  copy_state=frigidum.annealing.copy) 
#-----------------------------------------------------------------------#
#
#---------------------------------------------------------------------- #
#                               Credits:                                #
#                   Frigidum Author: Willem Hendrik                     #
#                   Numpy Author: Travis Oliphant                       #
#                   Challenge Author:  Nick Trefethen                   #
#                          All Right Reserved®                          #  
#---------------------------------------------------------------------- #