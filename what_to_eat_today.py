import cv2
import glob
import random

def what_to_eat_today():                                                                                                
    read_path = "/home/mp913/Desktop/*jpg"                                                                              
    filenames = glob.glob(read_path)                                                                                    
    filenames.sort()                                                                                                    
    images = [cv2.imread(img) for img in filenames]                                                                     
                                                                                                                        
    while True:                                                                                                         
        for img in images:                                                                                              
                                                                                                                        
            delay = random.randint(1, 50)                                                                               
                                                                                                                        
            img = cv2.resize(img, (500,500))                                                                            
                                                                                                                        
            cv2.imshow("Food", img)                                                                                     
            k = cv2.waitKey(delay) &0xFF                                                                                
                                                                                                                        
            #press space to stop                                                                                        
            if k == 32:                                                                                                 
                                                                                                                        
                cv2.waitKey(0)                                                                                          
                                                                                                                        
            if k == 27:                                                                                                 
                exit("Byebye")                                                                                          
                                                                                                                        
                                                                                                                        
what_to_eat_today()                                                                                                     
