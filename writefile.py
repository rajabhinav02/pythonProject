
#with open('test.txt', 'r') as readfile:
    #values = readfile.readlines()
    #print(values)
    #reversed(values)

    #with open('test.txt', 'w') as writer:
       # for ou in reversed(values):
           # writer.write(ou)


testing = open('test.txt')

teline = testing.readline()

while teline!= '':
    print(teline)
    teline = testing.readline()

testing.close()

testing2 = open('test.txt')

for output in testing2.readlines():
    print(output)

testing2.close()

with open('test.txt', 'r') as testing3:
    values3 = testing3.readlines()

with open('test.txt', 'w') as testingg:
    for output2 in reversed(values3):
        testingg.write(output2)