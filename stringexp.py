

str1 = " testing the test "

str2 = "testo"

if str2 in str1:
    print("Good")
else:
    print ("Bad")

str3= (str1.split("t"))
print(str3)

print(str3[1])

str4=(str1.lstrip())
print(str4)
print(str1.rstrip())

