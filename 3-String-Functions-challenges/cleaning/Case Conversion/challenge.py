#convert to lower case
a="salah GUEROUI"
print(a.lower())

#convert to upper case
b="salah gueroui"
print(b.upper())

#check if the string is equal to another string
c="SALAH"
d="salah"
print(c==d)

#check if the string is equal to another string before removing spaces and converting them to lower case
c="SALAH".lower()
d=" salah".lower()
print(c==d)

#check if the string is equal to another string after removing spaces and converting them to lower case
c="SALAH".lower().strip()
d=" salah".lower().strip()
print(c==d)