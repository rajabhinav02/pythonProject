

l1= [1,2,3]
file= open("filenew.txt", "w")
#file= open("filenew.txt", "r+") -- r+ for both read and write

for lines in l1:
    file.write(str(lines) + "\n")


#read

#1st way to read
file= open("filenew.txt", "r")

#print(str(file.read()))
#print(str(file.readlines()))

#2nd way to read
#file= open("filenew.txt")

#data = file.readline()

#while data != '':
    #print(data)
    #data = file.readline()

#print("nothing")

for d in file:
    print (d.readline())


file.close()

#xpath exercise

#//table[@id='product']//td[text()='Python Programming Language ']/following-sibling::td