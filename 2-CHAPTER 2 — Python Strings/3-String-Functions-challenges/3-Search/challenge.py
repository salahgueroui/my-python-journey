phone_number = "+49-123-4567"
#check if the string starts with "+49" and ends with "4567"
print(phone_number.startswith("+49"))
print(phone_number.endswith("4567"))

#check if the string contains "123"
print(phone_number.find("123"))

#if we have big not clean data 
phone1="+49-0176-123-4567"
phone2="49-0176-123-4567"
phone3="0049-176-123-4567"

print(phone1.startswith("0176"))

#this is not good way to make the namber without "+49"
print(phone1[4:])
print(phone2[3:])
print(phone3[5:])

#this is good way to make the namber without "+49"
print (phone1[phone1.find("-")+1:])
print (phone2[phone2.find("-")+1:])
print (phone3[phone3.find("-")+1:])
