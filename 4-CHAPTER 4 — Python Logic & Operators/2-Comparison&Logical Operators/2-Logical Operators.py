print(10 < 5 and 10 > 15)
print(10 > 5 or 10 < 15)
print(10 > 5 and 10 < 15)
print(10 > 5 or 10 < 15)

#or
cpu_usage=70
memory_usage=95
print(cpu_usage>90 or memory_usage>90)

#and
email="[EMAIL_ADDRESS]"
password="[PASSWORD]"
print(email=="[EMAIL_ADDRESS]" and password=="[PASSWORD]")

#not
print(not(10>5))
print(not(10<5))
print(not True)
print(not False)
print(not not True)

name=""
print(name)
print(not name)
print(not 0)

print("--------------------------")
login=False
guest=True
banned=False
print(not banned and (guest or login))
