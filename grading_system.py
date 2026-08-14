score = int(input("Enter your score(0-100): "))
print("================")
print("Grade of a score")
print("================")

if score >= 90:
    print("grade A")
elif 80 <= score <= 89:
    print("grade B")
elif 70 <= score <= 79:
    print("grade C")
elif 60 <= score <= 69:
    print("grade D")
else:
    print("grade F")

print("================")