
l1 = [6,7,8,"haha"]
#print(reversed(l1))
with open("my.txt", 'w') as writer:
    writer.write("some"+"\n")
    for o in reversed(l1):
        writer.write(str(o)+"\n")

with open("my.txt",'r') as reader:
    print(reader.read())


l2 = [1,2]
with open("text.txt", "w") as writer:
    writer.write("haha"+"\n")
    for l in l2:
        writer.write(str(l)+"\n")