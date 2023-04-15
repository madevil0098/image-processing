"""import csv
f=open("C:\\Users\\MADEVIL\\OneDrive\\Desktop\\New folder\\code\\ui\\Book2.csv","r")
r=list(csv.reader(f))
f.close()

for i in range(len(r)):
    
    r[i][0]=("0"*(3-len(r[i][0])))+r[i][0]
    
f=open("C:\\Users\\MADEVIL\\OneDrive\\Desktop\\New folder\\code\\ui\\Book3.csv","w",newline="\n")
t=csv.writer(f)
t.writerows(r)
f.close()"""


a=[1,2,3,4,5,6,8,9,6,5,4]
#a[5]=[[10]]+[[23]]+[[45]]
a[len(a):]=[[10],[23],[45]]*2

print(a)