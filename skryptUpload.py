#!/usr/bin/python
import os
import csv
from numpy import matrix






nazwaPliku = ""
tytul = ""
kategoria = ""

# matrix = open('/home/pi/Skrypty/ytupload/wideo/nazwy.csv').read()
# print (matrix)
# matrix = [item.split() for item in matrix.split('\n')[:-1]]
# print("############################################")


a_file = open("/home/pi/Skrypty/ytupload/wideo/nazwy.csv")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

print(contents_split)
a_file.close()




matrix = contents_split



print ("Matrix[2}=",matrix[2])

x = len(matrix)
y = len(matrix[:0])
print ("X:{}".format(x))
print ("X:{}".format(y))




for xx in range(0,x):

    #print("Matrix:{}".format(matrix[xx]))
    

    print("NazwaPliku:{}".format(matrix[xx]))
    upload = ("python upload_video.py --file=/home/pi/Skrypty/ytupload/wideo/{} --title={} --category={} --privacyStatus={}".format({},"Test{}","{}","{}").format(matrix[xx],xx,22,"private"))
    print(upload)
    os.system(upload)
    
