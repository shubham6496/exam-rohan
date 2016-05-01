# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:08:17 2016

@author: Hp
"""

#import scipy
#from scipy import array as np
import matplotlib.pyplot as plt
import numpy as np
Z=np.array([[0,0,0,0,0,0],
            [0,1,2,3,1,0],
            [0,0,1,2,1,0],
            [0,1,0,2,3,0],
            [0,2,3,0,1,0],
            [0,0,0,0,0,0]])  # Given matrix
print Z
print Z.shape

#def compute_neighbours(Z):
#    rows,cols=len(Z),len(Z[0])
#    N=[[0,]*(cols)for k in range(rows)]
#COUNTING
for i in range (1,4):
    for j in range (1,4):
          r1=Z[i-1,j-1]   #neighbouring element
            
          r2=Z[i,j-1]     #neighbouring element
             
          r3=Z[i+1,j-1]   #neighbouring element
            
          r4=Z[i-1,j]     #neighbouring element
             
          r5=Z[i+1,j]     #neighbouring element
           
          r6=Z[i-1,j+1]   #neighbouring element
            
          r7=Z[i,j+1]     #neighbouring element
            
          r8=Z[i+1,j+1]   #neighbouring element 
          
          m=[r1,r2,r3,r4,r5,r6,r7,r8]   # Array of neighbouring element
          print m
          
          for l in range(8):
              b=0   #initial condition for bare earth
              g=0   #initial condition for grass
              p=0   #initial condition for prey
              q=0   #initial condition for predator
              
              if m[l]==0:   
                  b=b+1
              if m[l]==1:
                  g=g+1
              if m[l]==2:
                  p=p+1
              if m[l]==3:
                  q=q+1
                  
          if Z[i,j]==0 and g>0:  # If bare earth element is surrounded by more than bare earth element, then bare earth turns to grass
              Z[i,j]=1
          if Z[i,j]==2 and g<2:  # If prey element is surrounded by less than two grass element, then prey turns to bare earth
              Z[i,j]=0
          if Z[i,j]==3 and p<2:  # If preator element is surrounded by less  than two prey element, then predator turns to grass
              Z[i,j]=1
          if Z[i,j]==1 and p>1:  # If grass element is surrounded by more than one prey element, then grass turns to bare earth
              Z[i,j]=0
          if Z[i,j]==0 and g>2 and p>1:  # If bare earth element is surrounded by more than two grass element and more than one prey element, then bare earth turns to prey
              Z[i,j]=2
print Z
plt.imshow(Z)
plt.colorbar()
# return N   