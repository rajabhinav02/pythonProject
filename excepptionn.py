

items = 0

#if items != 2:
   # raise Exception("count wrong")

if items != 2:
    pass

assert(items == 0)

try:
    with open("test.txt", 'r') as trying:

        tes= trying.readlines()
        print(tes)
        reversed(tes)
        for ou in reversed(tes):
            print(ou)

    with open("test.txt", 'w') as writing:
        for out in reversed(tes):
            writing.write(out)



except:

    tesi = open("test.txt")

    reading = tesi.readline()

    while reading != '':
        print(reading)
        reading = tesi.readline()

finally:
    print("tesi.close()")