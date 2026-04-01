#Challenge 1
#Check if the username is not empty and the age is greater than or equal to 18.

username="salah"
age=25
print(username!="" and  age>=18)
print("============================================")
#Challenge 2
#Check if the password length is at least 8 characters and does not contain spaces.

password = "[PASSWORD]"
print(len(password) >= 8 and " " not in password)
print("============================================")
#Challenge 3
#Check if the email is not empty, contains "@" and ends with ".com".

email = "salah@gmail.com"
print(email != "" and "@" in email and email.endswith(".com"))
print("============================================")
#Challenge 4
#Check if the variable is a string and its length is greater than 5.

username1="salahhh"
print(username1 is not None and isinstance(username1, str) and len(username1) > 5)
print("============================================")
#Challenge 5
#Check if the user is either an admin or a moderator and either not banned or verified.

users=["salah","mohamed","ali"]
admins=["salah","mohamed"]
moderators=["ali"]
verified=["salah","mohamed","ali"]
banned=[]

user = "salah"

print(
    (user in admins or user in moderators)
    and
    (user not in banned or user in verified)
)








