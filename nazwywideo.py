import os, csv

f=open("nazwy.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("/home/pi/Skrypty/ytupload/wideo"):
    for filename in files:
        w.writerow([filename])