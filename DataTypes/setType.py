#set and frozenset are two types in set category
#set is predefined class treated as set datatype
#set doesnt follow insertion order and it neglects all the duplicate values
#a set type is both mutable and immutable
a=set() #creating empty set
print(a,type(a))
b={3,4,6,2,99}
print(b,type(b))
c={3,2,5,2,8,2,"Hello","world","Hello","hello"}
print(c)
#frozenset
#f=frozenset(3,54,4) shows error because it only accepts itterable objects
f=frozenset("Hello")
print(f)
l=frozenset([3,4,2,"Hello"])
print(l)
