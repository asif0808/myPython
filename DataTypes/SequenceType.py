#sequence data types are str, bytes, bytearray, range
s="Hello World"
b=bytes([3,4,6,4,2,255])           #range of bytes amd bytearray is (0,256)
#shows error  ba=bytearray([4,3,6,-6,75])
ba=bytearray([4,3,6,6,75])
r=range(0,10)
print(s,type(s))
print(b,type(b))
print(ba,type(ba))
print(r,type(r))