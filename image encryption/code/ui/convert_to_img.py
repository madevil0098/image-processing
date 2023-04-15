import csv
import numpy as np
import cv2

t={"0":[0,0,0],"1":[0,0,255],"2":[0,255,0],"3":[0,255,255],"4":[255,0,0],"5":[255,0,255],"6":[255,255,0],"7":[255,255,255]}
def change(ind,octa):
    for i in range(len(octa)):
        if octa[i][2]==read[ind]:
            octal_code=list(str(octa[i][0]))
            l2[len(l2):]=t[octal_code[0]],t[octal_code[0]],t[octal_code[0]]
            read[ind:ind+1]=t[octal_code[0]],t[octal_code[0]],t[octal_code[0]]    
            break
           


def convert_file(file_name):
    file=open(file_name,"r")
    global read,l2
    if ".csv" in file_name:
        read=str(list(csv.reader(file)))
        read=list(read)
        #print(len(read))
        l2=[]
        file2=open("C:\\Users\\MADEVIL\\OneDrive\\Desktop\\New folder\\code\\ui\\Book3.csv","r")
        read2=list(csv.reader(file2))
        i=0
        try:
            while True:
                change(i,read2)
                i=i+3
                """t1=threading.Thread(target=change,args=(i,read2))
                t1.start()
                t1.join()"""
        except Exception:
            pass
        finally:
            square=int(len(l2)**(1/2))
            print(len(l2),len(read),len(l2)/square)
            for i in range(0,len(l2),square):
                pass
            left=square-(len(l2)-(i))
            octal_code=list(str("200"))
            l2[len(l2):]=[t[octal_code[0]]]*left
            read[len(read):]=[t[octal_code[0]]]*left
            print(len(l2),len(read),square,left,len(l2)/square,len(l2)-1)
            l3=[]
            j=0
            for i in range(square,len(l2),square):
                temp=[]
                l3=l3+[l2[j:i]]
                j=i
            print(i)
            print(type(l3),len(l3),len(l3[0]),len(l3[0][0]))
            
            l4=np.array(l3,dtype=np.uint8)
            print(type(l4),l4.size,l4.ndim)
            cv2.imwrite(file_name+".jpg",l4)
            cv2.imshow("Image", l4)
            cv2.waitKey(10000) 
    else:
        read=str(file.readlines())
        read=list(read)
        #print(len(read),read)
        l2=[]
        file2=open("C:\\Users\\MADEVIL\\OneDrive\\Desktop\\New folder\\code\\ui\\Book3.csv","r")
        read2=list(csv.reader(file2))
        i=0
        try:
            while True:
                change(i,read2)
                i=i+3
                """t1=threading.Thread(target=change,args=(i,read2))
                t1.start()
                t1.join()"""
        except Exception:
            pass
        finally:
            square=int(len(l2)**(1/2))
            print(len(l2),len(read),len(l2)/square)
            for i in range(0,len(l2),square):
                pass
            left=square-(len(l2)-(i))
            octal_code=list(str("200"))
            l2[len(l2):]=[t[octal_code[0]]]*left
            read[len(read):]=[t[octal_code[0]]]*left
            print(len(l2),len(read),square,left,len(l2)/square,len(l2)-1)
            l3=[]
            j=0
            for i in range(square,len(l2),square):
                temp=[]
                l3=l3+[l2[j:i]]
                j=i
            print(i)
            print(type(l3),len(l3),len(l3[0]),len(l3[0][0]))
            l4=np.array(l3,dtype=np.uint8)
            print(type(l4),l4.size,l4.ndim)
            cv2.imwrite(file_name+".jpg",l4)
            cv2.imshow("Image", l4)
            cv2.waitKey(10000) 


if __name__=="__main__":
    convert_file("C:\\Users\\MADEVIL\\OneDrive\\Desktop\\DATA ANYLYSIS\\titanic.csv")