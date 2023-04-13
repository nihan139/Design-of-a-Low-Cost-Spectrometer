import serial as sr
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd

s = sr.Serial('COM3',9600);
plt.close('all');
plt.figure("I-V Characteristics");
plt.ion();
plt.show();

voltage = []
current = []

unique_current = []
unique_current.append(0)
R1 = 220;
index = 1;
tolerance = 0.5;




def frame_capture(file_num):    
    cap = cv2.VideoCapture(1)
    roi_selected = False
    
    
    while(True):
        ret, frame = cap.read()
        
        k = cv2.waitKey(1)
        
        if k & 0xFF == ord('s') and roi_selected == True:
            shape = cropped.shape
            r_dist = []
            b_dist = []
            g_dist = []
            i_dist = []
            
            hue_dist = []
            sat_dist = []
            val_dist = []
            
            lambda_dist = []
            
            for i in range(shape[1]):
                r_val = np.mean(cropped[:, i][:, 2])
                b_val = np.mean(cropped[:, i][:, 0])
                g_val = np.mean(cropped[:, i][:, 1])
                i_val = (r_val + b_val + g_val) / 3
                
                hue = np.mean(img_hsv[:, i][:, 0])
                sat = np.mean(img_hsv[:, i][:, 1])
                val = np.mean(img_hsv[:, i][:, 2])
                
                wavelength = 700-(300/150)*hue

                r_dist.append(r_val)
                g_dist.append(g_val)
                b_dist.append(b_val)
                i_dist.append(i_val)
                
                hue_dist.append(hue)
                sat_dist.append(sat)
                val_dist.append(val)
                
                lambda_dist.append(wavelength)
                
                
            
            str1 = 'wavelength' + str(file_num) + '.csv'
            str2 = 'intensity' + str(file_num) + '.csv'
            str3 = 'merged' + str(file_num) + '.csv'
            str4 = 'wavelength_sorted' + str(file_num) + '.csv'

                
            df1 = pd.DataFrame(lambda_dist, columns=["Wavelength(nm)"])
            df1.to_csv(str1, index=False)
            
            df2 = pd.DataFrame(val_dist, columns=["Intensity"])
            df2.to_csv(str2, index=False)
            
            
            data1=pd.read_csv(str2,index_col=0)
            data2=pd.read_csv(str1,index_col = 0)
            
            data1.reset_index(inplace=True)
            data1.reset_index(inplace=True)
            data2.reset_index(inplace=True)
            data2.reset_index(inplace=True)
            
            
            df_merged=data1.merge(data2,on='index',how='right')
            df_merged.to_csv(str3)

            sorted_df = df_merged.sort_values(by=["Wavelength(nm)"],ascending=True);
            sorted_df.to_csv(str4, index=False)
            
        elif k & 0xFF == ord('r'):
            r = cv2.selectROI(frame)
            roi_selected = True
            
        elif k & 0xFF == ord('q'):
            break
        
        else:
            if roi_selected:
                cropped = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
                cv2.imshow('roi', cropped)
                img_hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
            else:
                cv2.imshow('frame', frame)
        
    cap.release()
    cv2.destroyAllWindows()
    



count = 1;
    
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
    #print(voltage);
    
    
     
    for x in current:
        # check if exists in unique_list or not
        if x not in unique_current:
            if(x-unique_current[-1]> tolerance):
                unique_current.append(x)
                print(unique_current)
     
                # Create a file object for this file
                with open('current.csv', 'a') as fd:
                    fd.write(str(x))
                    fd.write("\n")
                    frame_capture(count)
                    count = count + 1;
    
        
    
    if (len(voltage)==len(current)):
        plt.cla();
        plt.plot(voltage,current);
        plt.pause(0.01);
    




