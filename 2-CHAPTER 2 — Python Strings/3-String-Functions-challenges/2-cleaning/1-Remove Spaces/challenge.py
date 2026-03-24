#remove spaces from the left side
a=" salah"
print(a.lstrip())

#remove spaces from the right side
b="salah "    
print(b.rstrip()) 

#remove spaces from both sides  
c=" salah "
print(c.strip())

#check if the string is clean
d=" salah"
print(len(d))
print(len(d.strip()))
if len(d.strip())==len(d):
    print("the string is clean")
else:
    print("the string is not clean")
