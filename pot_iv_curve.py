import serial as sr
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
import math
import struct

s = sr.Serial('COM3',9600);
plt.close('all');
plt.figure();
plt.ion();
plt.show();

voltage = []
current = []

unique_current = []
R1 = 220;
index = 1;



    
while True:
    a = s.readline();
    b = a.decode();
    c = b.rstrip();
    #print(type(c));
    d = float(c);
    #print(type(d));
    #print(d);
    
    if (index%2 ==0):
        current.append(d);
    else:
        voltage.append(d);

        
    index = index + 1;
    print(voltage);
    
     
    for x in current:
        # check if exists in unique_list or not
        if x not in unique_current:
            unique_current.append(x)
     
            # Create a file object for this file
            with open('current.csv', 'a') as fd:
                fd.write(str(x))
                fd.write("\n")
     
    print(unique_current)    
    
    if (len(voltage)==len(current)):
        plt.cla();
        plt.plot(voltage,current);
        plt.pause(0.01);
    


    