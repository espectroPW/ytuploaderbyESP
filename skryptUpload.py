#!/usr/bin/python
import os
import csv
from numpy import matrix






nazwaPliku = ""
tytul = ""
kategoria = ""

matrix = open('/home/pi/Skrypty/ytupload/wideo/nazwy.csv').read()
print (matrix)
matrix = [item.split() for item in matrix.split('\n')[:-1]]
print("############################################")


print (matrix)
print (matrix[2])

print ("Matrix[2}=",matrix[2])


x = len(matrix)
y = len(matrix[:0])
print ("X:{}".format(x))
print ("X:{}".format(y))


print("############################################")


for xx in range(0,x):
    #print("Matrix:{}".format(matrix[xx]))
    print("NazwaPliku:{}".format(matrix[xx]))
 
    
    upload = ("python upload_video.py --file=/home/pi/Skrypty/ytupload/wideo/{} --title={} --category={} --privacyStatus={}".format({},"Test{}","{}","{}").format(matrix[xx],xx,22,"private"))
    print(upload)
    #os.system(upload)
    