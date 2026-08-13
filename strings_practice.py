full_name = " Mohammad Shanawaz "

print(full_name.strip()) #remove spaces

print(full_name.upper().strip())
#uppercase letters

print(full_name[0:4])
#Moha

print(full_name[::-1])
#zawanahs dammahom

name_length = len(full_name.strip())
print(name_length)
# which calculates len of string removing spaces

print(f"my name has {name_length} characters")