fo=open("foo.txt","w")
fo.write("python la mot ngon ngu lap trinh tuyet voi.\nMinh cung nghi nhu the !!\n")
fo.close()
fo= open("foo.txt","w")
print("ten cua file la:",fo.name)
print("file da duoc dong hay chua:",fo.closed)
print ("che do truy cap la:", fo.mode)
import imp
import osos.name("foo.txt","test2.txt")
import os
os.remove("text2.txt")

