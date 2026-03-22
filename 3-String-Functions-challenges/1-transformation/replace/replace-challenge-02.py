raw_data = "968-Maria, ( D@t@ Engineer );;   27y.."

clean= raw_data\
    .replace("968-","")\
    .replace(",","")\
    .replace(" (","")\
    .replace("@","a")\
    .replace(" )","")\
    .replace(";;  ","")\
    .replace("y..","")\
    .strip()

parts=clean.split()

name=parts[0].lower()
role=" ".join(parts[1:3]).lower()
age=parts[-1]

print(f"name: {name} | role: {role} | age: {age} ")

