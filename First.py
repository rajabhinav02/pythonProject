print("hello")

b = 4

print(b)

print("{}{}".format("trying to ", b))

c, d, e, f, g = 7, 8, 9, "lol", "lamo"

print("{}{}".format(f, e))

print(f + g)

values = [1, 2, "okay", 3]
values.append("check")
print("#####", values)
values.insert(2,"lol")
print("#####", values)
values[1]=6
print("#####", values)
print(len(values))
#print(values[20])


print(values[1])
print(values[-1])

print("{}{}".format("checking", b))

hg = [1, 2, 3, 4]

if 1 in hg:
    print("1 is there")
else:
    print("1 is not there")

jk = [2, 3, 4, 5, 6]

for no in range(len(jk)):
    print(jk[no])

n = 2
l = 1

while l <= 10:
    print(n, "*", l, "=", n * l)
    l = l + 1


it = 10

while it > 4:

    if it == 8:
        it = it - 1
        continue

    if it == 6:
        break
    print(it)

    it = it - 1


summation = 0

for noo in range (1,10):
    summation = summation+noo

print("{}{}".format("sum is", summation))

jk = "jklihkdhjgfjgdjgj"
kl = "jkhkh"
print(jk[:4])
print (jk+kl)

ko = "afbdhkkd"
lo = 4

print("{}{}".format(ko,lo))


bor = [1,2,"kl", 8, 9.0]

for bo in bor:
    print(bo)