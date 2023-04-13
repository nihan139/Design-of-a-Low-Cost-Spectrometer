import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

def main():

    count = 1
    
    while(count<3):
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
                    
                    
                
                   
                
                #plt.subplot(2, 1, 1)
                #plt.imshow(frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])])

                #plt.subplot(2, 1, 2)
                plt.plot(r_dist, color='r', label='red')
                plt.plot(g_dist, color='g', label='green')
                plt.plot(b_dist, color='b', label='blue')
                #plt.plot(i_dist, color='k', label='mean')
                #plt.plot(val_dist, color='c', label='value')
                plt.plot(hue_dist, color='k', label='hue')
                #plt.plot(sat_dist, color='r', label='sat')
                #plt.plot(lambda_dist, color='y', label='wavelength')
                #plt.legend(loc="upper left")
                plt.show()
                
                str1 = 'wavelength' + str(count) + '.csv'
                str2 = 'intensity' + str(count) + '.csv'
                str3 = 'merged' + str(count) + '.csv'
                str4 = 'wavelength_sorted' + str(count) + '.csv'

                    
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
        
        count = count + 1;
        print(count)

if __name__ == '__main__':
    main()